</> Bash
Deployment Commands

terraform init

terraform plan

terraform apply



Diagram
┌──────────────────────────────┐
│        EventBridge Rule      │
│   (Daily Schedule - UTC)     │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│        AWS Lambda Function   │
│  - Python 3.11               │
│  - Snapshot Cleanup Logic    │
│  - IAM Role Attached         │
└──────────────┬───────────────┘
               │
     Runs inside VPC
               │
┌──────────────▼───────────────┐
│            VPC               │
│  ┌────────────────────────┐ │
│  │     Private Subnet      │ │
│  │  - No Public Internet   │ │
│  │  - Lambda ENI           │ │
│  └────────────────────────┘ │
└──────────────┬───────────────┘
               │
     VPC Endpoint / NAT
               │
┌──────────────▼───────────────┐
│           EC2 API            │
│   - DescribeSnapshots       │
│   - DeleteSnapshot          │
└──────────────────────────────┘
