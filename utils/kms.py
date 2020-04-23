from base64 import b64encode, b64decode
from utils.configs import kmsClient, kmsKeyId


class ApiKms(object):

    @classmethod
    def encrypt(cls, string):
        cipher = kmsClient.encrypt(KeyId=kmsKeyId, Plaintext=str(string))
        return b64encode(cipher["CiphertextBlob"]).decode()

    @classmethod
    def decrypt(cls, encodedCipher):
        plainPassword = kmsClient.decrypt(CiphertextBlob=bytes(b64decode(encodedCipher)))
        return plainPassword["Plaintext"].decode()
