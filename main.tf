resource "aws_s3_bucket" "logs" {
  bucket = "logs"
}

resource "aws_s3_object" "laravel-logs-dir" {
  bucket = aws_s3_bucket.logs.bucket
  acl    = "private"
  key    = "laravel/"
  source = "/dev/null"
}

resource "aws_s3_bucket_acl" "logs_acl" {
  bucket = aws_s3_bucket.logs.bucket
  acl    = "private"
}

resource "aws_s3_bucket_lifecycle_configuration" "logs-config" {
  bucket = aws_s3_bucket.logs.bucket

  rule {
    id = "log"

    expiration {
      days = 30
    }

    filter {
      and {
        prefix = "laravel/"

        tags = {
          rule      = "log"
          autoclean = "true"
        }
      }
    }

    status = "Enabled"

    transition {
      days          = 1
      storage_class = "ONEZONE_IA"
    }

    transition {
      days          = 7
      storage_class = "GLACIER"
    }
  }
}