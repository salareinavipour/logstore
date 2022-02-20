# Logstore

This project creates an S3 bucket that holds logs and then archives them using Glacier.
We used Terraform for IaC and we're going to use Ansible to deploy log store Python scripts onto EC2 Instances.
Cronjobs then run these scripts every night to upload logs to the bucket.
After a day, the lifecycle rules of the bucket will move them to `ONEZONE_IA` and after a week to `Glacier` so We can have them in cold storage.

## Pre-req

You need these pre-requisites in the machine you're using the script in:
* You need Python 3 and pip
* Run `pip install boto3`

For the machine that you use to create the bucket, `Terrafom` must be installed.

An AWS account with preferred permissions.

## How to use this

1. Clone this repo and then populate the secrets with your credentials.
2. Run `terrafom plan` and then `terrafom apply`
3. After the creation use the bucket name from the output.
4. Set environment variables in the machine that you want to store its logs.
5. Copy `uploader.py` into that machine and copy it into `/usr/loca/bin`.
6. Make the script executable.
7. Use `crontab -e` to create the cronjob and then schedule it for the time you want.

## ToDo

* Add Ansible Playbooks.
* Add uploader script.