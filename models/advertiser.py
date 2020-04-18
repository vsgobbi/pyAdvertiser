from pynamodb.models import Model
from pynamodb.attributes import UTCDateTimeAttribute, UnicodeAttribute
from datetime import datetime
from utils.configs import region


class Advertiser(Model):

    class Meta:
        table_name = "atnap_advertiser"
        region = region

    created = UTCDateTimeAttribute(null=False, default=datetime.now())
    updated = UTCDateTimeAttribute(null=True)
    fullName = UnicodeAttribute(null=False)
    companyName = UnicodeAttribute(null=False)
    taxId = UnicodeAttribute(null=False, hash_key=True)
    email = UnicodeAttribute(null=False, range_key=True)
    phoneNumber = UnicodeAttribute(null=False)

    @classmethod
    def newItem(cls, fullName, companyName, taxId, email, phoneNumber):
        advertiser = Advertiser(
            fullName=fullName,
            companyName=companyName,
            taxId=taxId,
            phoneNumber=phoneNumber,
            email=email,
        )
        return advertiser.save()

    @classmethod
    def updateItem(cls, **kwargs):
        advertiser = Advertiser.get(
            kwargs.get("taxId"),
            kwargs.get("email"),
        )
        advertiser.refresh()
        advertiser.update(actions=[
            Advertiser.fullName.set(kwargs.get("fullName")) or Advertiser.fullName,
            Advertiser.companyName.set(kwargs.get("companyName")) or Advertiser.companyName,
            Advertiser.phoneNumber.set(kwargs.get("phoneNumber")) or Advertiser.phoneNumber,
            Advertiser.updated.set(datetime.now())
        ])

    @classmethod
    def deleteItem(cls, taxId, email):
        advertiser = Advertiser(
            taxId=taxId,
            email=email
        )
        return advertiser.delete()

    @classmethod
    def createTable(cls):
        if not Advertiser.exists():
            Advertiser.create_table(
                read_capacity_units=10,
                write_capacity_units=10,
                wait=True
            )

    @classmethod
    def dropTable(cls):
        if Advertiser.exists():
            Advertiser.delete_table()

    @classmethod
    def tableDefinitions(cls):
        if Advertiser.exists():
            return Advertiser.describe_table()

    @classmethod
    def queryByTaxIdAndEmail(cls, taxId, email):
        return Advertiser.get(taxId, email)

    @classmethod
    def queryByTaxId(cls, taxId):
        for item in Advertiser.query(taxId):
            return item

    @classmethod
    def json(cls, advertiser):
        return {
            "fullName": Advertiser.fullName,
            "companyName": advertiser.companyName,
            "taxId": advertiser.taxId,
            "email": advertiser.email,
            "phoneNumber": advertiser.phoneNumber,
            "created": advertiser.created.strftime("%Y-%m-%d"),
        }
