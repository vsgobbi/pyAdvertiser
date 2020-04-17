import boto3
from base64 import b64encode, b64decode


class ApiKms(object):

    kmsClient = boto3.client("kms", "us-east-1")
    keyId = "the aws ksm generated key id"

    @classmethod
    def encrypt(cls, string):
        cipher = cls.kmsClient.encrypt(KeyId=cls.keyId, Plaintext=str(string))
        return b64encode(cipher["CiphertextBlob"])

    @classmethod
    def decrypt(cls, encodedCipher):
        plainPassword = cls.kmsClient.decrypt(CiphertextBlob=bytes(b64decode(encodedCipher)))
        return plainPassword["Plaintext"].decode()
