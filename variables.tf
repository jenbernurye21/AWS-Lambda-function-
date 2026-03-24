variable "region" {
  default = "us-east-1"
}

variable "lambda_name" {
  default = "delete-old-ec2-snapshots"
}

variable "lambda_zip_path" {
  default = "snapshot_cleanup.zip"
}
