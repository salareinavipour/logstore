#!/usr/bin/python3
import boto3, os, datetime
from os.path import isfile, join

bucket_name = os.environ['BUCKET_NAME']
logs_path = os.environ['LOGS_PATH']
session = boto3.Session(
aws_access_key_id=os.environ['AWS_ACCESS_KEY'],
aws_secret_access_key=os.environ['AWS_SECRET_KEY'],
region_name=os.environ['AWS_REGION']
)

if __name__ == "__main__":
    os.listdir(logs_path)
    log_files = [f for f in os.listdir(logs_path) if isfile(join(logs_path, f))]
    print(log_files)
    s3 = session.resource('s3')
    for log in log_files:
        object = s3.Object(bucket_name, f"{logs_path}/{log}")
        result = object.put(Body=f"{datetime.date.today()}-{log}")
        res = result.get('ResponseMetadata')
        if res.get('HTTPStatusCode') == 200:
            print('File Uploaded Successfully')
        else:
            print('File Not Uploaded')