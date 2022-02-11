# Logstore

This project create a S3 bucket that holds logs and then archives them using Glacier.
We used Terraform for IaC and we're going to use Ansible to deploy logstore Python scripts onto EC2 Instances.
Cronjobs then run these scripts every night to upload logs to the bucket.
After a day, lifecycle rules of the bucket will move them to `ONEZONE_IA` and after a week to `Glacier` so We can have them in cold-storage.

## ToDo
* Add Ansible Playbooks.
* Add uploader script.