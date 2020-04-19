# AWS Configurations
import boto3

# PynamoDB region:
region = "us-east-1"

kmsClient = boto3.client("kms", "us-east-1")
keyId = "bff7ac3a-3ce6-40c9-825b-884d59bf84e2"
