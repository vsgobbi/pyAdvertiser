# AWS Configurations
import boto3
from uuid import uuid4
import os

# PynamoDB region:
region = "us-east-1"

# KMS configs:
try:
    kmsClient = boto3.client("kms", "us-east-1")
    kmsKeyId = os.environ["KMS_KEY_ID"]
    print(kmsKeyId)
except Exception as error:
    print("Set KMS key id as environment variable before using it!, {}".format(error))

sessionSecretKey = "{0}-{1}".format(uuid4(), uuid4())
