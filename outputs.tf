output "lambda_function_name" {
  value = aws_lambda_function.this.function_name
}

output "vpc_id" {
  value = aws_vpc.this.id
}
