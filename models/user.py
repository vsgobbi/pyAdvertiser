from pynamodb.models import Model
from pynamodb.attributes import UTCDateTimeAttribute, UnicodeAttribute
from datetime import datetime

from utils.configs import region
from utils.kms import ApiKms


class User(Model):

    class Meta:
        table_name = "atnap_user"
        region = region

    fullName = UnicodeAttribute(null=False)
    email = UnicodeAttribute(null=False, range_key=True)
    phoneNumber = UnicodeAttribute(null=False)
    passwordHash = UnicodeAttribute(null=False)
    taxId = UnicodeAttribute(null=False)
    id = UnicodeAttribute(null=False, hash_key=True)
    created = UTCDateTimeAttribute(null=False, default=datetime.now())
    updated = UTCDateTimeAttribute(null=True)

    @classmethod
    def newItem(cls, fullName, password, taxId, email, phoneNumber):
        user = User(
            fullName=fullName,
            passwordHash=ApiKms.encrypt(password),
            taxId=taxId,
            phoneNumber=phoneNumber,
            email=email,
        )
        return user.save()

    @classmethod
    def updateItem(cls, **kwargs):
        advertiser = User.get(
            kwargs.get("taxId"),
            kwargs.get("email"),
        )
        advertiser.refresh()
        advertiser.update(actions=[
            User.fullName.set(kwargs.get("fullName")) or User.fullName,
            User.phoneNumber.set(kwargs.get("phoneNumber")) or User.phoneNumber,
            User.updated.set(datetime.now())
        ])

    @classmethod
    def deleteItem(cls, taxId, email):
        user = User(
            taxId=taxId,
            email=email
        )
        return user.delete()

    @classmethod
    def createTable(cls):
        if not User.exists():
            User.create_table(
                read_capacity_units=10,
                write_capacity_units=10,
                wait=True
            )

    @classmethod
    def dropTable(cls):
        if User.exists():
            User.delete_table()

    @classmethod
    def tableDefinitions(cls):
        if User.exists():
            return User.describe_table()

    @classmethod
    def queryByTaxIdAndEmail(cls, taxId, email):
        return User.get(taxId, email)

    @classmethod
    def queryByTaxId(cls, taxId):
        for item in User.query(taxId):
            return item

    @classmethod
    def getPasswordHashByEmail(cls, email):
        for item in User.query(email):
            return item.passwordHash

    @classmethod
    def getPasswordTaxId(cls, taxId):
        for item in User.query(taxId):
            return item.passwordHash

    @classmethod
    def json(cls, advertiser):
        return {
            "fullName": User.fullName,
            "taxId": advertiser.taxId,
            "email": advertiser.email,
            "phoneNumber": advertiser.phoneNumber,
            "created": advertiser.created.strftime("%Y-%m-%d"),
        }
