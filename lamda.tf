resource "aws_lambda_function" "this" {
  function_name = var.lambda_name
  role          = aws_iam_role.lambda.arn
  runtime       = "python3.11"
  handler       = "lambda_function.lambda_handler"
  filename      = var.lambda_zip_path

  timeout      = 300
  memory_size = 128

  vpc_config {
    subnet_ids         = [aws_subnet.private.id]
    security_group_ids = [aws_security_group.lambda.id]
  }

  environment {
    variables = {
      RETENTION_DAYS = "365"
    }
  }
}
