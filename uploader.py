#!/usr/bin/python3
import boto3, os, logging
from botocore.exceptions import ClientError
from os.path import isfile, join

bucket_name = os.environ['BUCKET_NAME']
logs_path = os.environ['LOGS_PATH'] # e.g: /var/log/nginx
sub_dir = os.environ['SUB_DIR'] # This is the sub directory in S3 bucket(e.g. s3://bucket2342/nginx)
session = boto3.Session(
aws_access_key_id=os.environ['AWS_ACCESS_KEY'],
aws_secret_access_key=os.environ['AWS_SECRET_KEY'],
region_name=os.environ['AWS_REGION']
)

if __name__ == "__main__":
    os.listdir(logs_path)
    log_files = [f for f in os.listdir(logs_path) if isfile(join(logs_path, f))]
    s3 = session.resource('s3').Bucket(bucket_name)
    for log in log_files:
        try:
            s3.upload_file(f'{logs_path}/{log}', f'{sub_dir}/{log}')
        except ClientError as e:
            logging.error(e)
        else:
            print(f'File {log} in {logs_path} has been uploaded.')