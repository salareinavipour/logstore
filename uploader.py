#!/usr/bin/python3
import boto3, os, datetime, logging
from botocore.exceptions import ClientError
from os.path import isfile, join

bucket_name = os.environ['BUCKET_NAME']
logs_path = os.environ['LOGS_PATH']
prefix = os.environ['PREFIX']
session = boto3.Session(
aws_access_key_id=os.environ['AWS_ACCESS_KEY'],
aws_secret_access_key=os.environ['AWS_SECRET_KEY'],
region_name=os.environ['AWS_REGION']
)

if __name__ == "__main__":
    os.listdir(logs_path)
    log_files = [f for f in os.listdir(logs_path) if isfile(join(logs_path, f))]
    s3 = session.resource('s3', endpoint_url=os.environ['ENDPOINT_URL']).Bucket(bucket_name)
    for log in log_files:
        try:
            s3.upload_file(f'{logs_path}{log}', f'{prefix}/{log}')
        except ClientError as e:
            logging.error(e)
        else:
            print(f'File {log} in {logs_path} has been uploaded.')