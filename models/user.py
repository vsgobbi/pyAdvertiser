from uuid import uuid4
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
    phoneNumber = UnicodeAttribute(null=False)
    passwordHash = UnicodeAttribute(null=False)
    taxId = UnicodeAttribute(null=False, hash_key=True,)
    id = UnicodeAttribute(null=False, default_for_new=str(uuid4())[:16])
    email = UnicodeAttribute(null=False, range_key=True)
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
        user = User.get(
            kwargs.get("taxId"),
            kwargs.get("email"),
        )
        user.refresh()
        user.update(actions=[
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
            return User.delete_table()

    @classmethod
    def tableDefinitions(cls):
        if User.exists():
            return User.describe_table()

    @classmethod
    def queryByTaxIdAndEmail(cls, taxId, email):
        return User.get(taxId, email)

    @classmethod
    def queryByTaxId(cls, taxId):
        queryResult = []
        for item in User.query(taxId):
            queryResult.append(cls.json(item))

        return queryResult

    @classmethod
    def queryUserByTaxId(cls, taxId):
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
    def json(cls, user):
        return {
            "fullName": user.fullName,
            "taxId": user.taxId,
            "email": user.email,
            "phoneNumber": user.phoneNumber,
            "created": user.created.strftime("%Y-%m-%d"),
        }
