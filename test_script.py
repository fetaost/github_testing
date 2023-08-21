import boto3
import os

AWS_REGION = os.getenv("AWS_REGION", "eu-west-1")
STAGE = os.getenv("STAGE", "staging")
LAKE_BUCKET = f"datalake.combify.{AWS_REGION}.{STAGE}"
s3 = boto3.client("s3")


def upload_to_s3(key, file):
    with open(file, "rb") as f:
        s3.upload_fileobj(f, LAKE_BUCKET, key, ExtraArgs={"ACL": "private"})


with open("dumb_test.txt", "w") as f:
    f.write("This is a test")

upload_to_s3("dumb_test/dumb_test.txt", "dumb_test.txt")
