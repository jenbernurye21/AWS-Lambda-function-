terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "6.21.0"
    }
  }
  backend "s3" {
    bucket = "jenber-bucket-taining-boa"
    key =    "dev-jen/jenberkey/terraform.tfstate"
    encrypt = true
    region = "us-east-1"
    dynamodb_table = "jenberDYDB"

  }
}
