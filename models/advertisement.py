from datetime import datetime
from utils.configs import region
from pynamodb.models import Model
from pynamodb.attributes import UTCDateTimeAttribute, UnicodeAttribute, UnicodeSetAttribute, NumberAttribute


class Advertisement(Model):

    class Meta:
        table_name = "atnap_advertisement"
        region = region

    title = UnicodeAttribute(null=False)
    advertiserTaxId = UnicodeAttribute(null=False, hash_key=True)
    category = UnicodeAttribute(null=False, range_key=True)
    phoneNumber = UnicodeAttribute(null=False)
    whatsAppApi = UnicodeAttribute(null=False)
    picturesUrl = UnicodeAttribute(null=True)
    socialMedia = UnicodeAttribute(null=True)
    description = UnicodeAttribute(null=False)
    tags = UnicodeSetAttribute(null=True)
    price = NumberAttribute(null=False)
    created = UTCDateTimeAttribute(null=False, default=datetime.now())
    updated = UTCDateTimeAttribute(null=True)
    deletedBy = UnicodeAttribute(null=True)

    @classmethod
    def newItem(cls, title, category, description, phoneNumber,
                price, socialMedia, advertiserTaxId, whatsAppApi,
                tags=None, picturesUrl=None):
        advertisement = Advertisement(
            title=title,
            category=category,
            description=description,
            tags=tags,
            price=price,
            advertiserTaxId=advertiserTaxId,
            phoneNumber=phoneNumber,
            picturesUrl=picturesUrl,
            whatsAppApi=whatsAppApi,
            socialMedia=socialMedia,
        )
        return advertisement.save()

    @classmethod
    def deleteItem(cls, taxId, email):
        advertisement = Advertisement(
            taxId=taxId,
            email=email
        )
        return advertisement.delete()

    @classmethod
    def updateItem(cls, **kwargs):
        user = Advertisement.get(
            kwargs.get("advertiserTaxId"),
        )
        user.refresh()
        user.update(actions=[
            Advertisement.phoneNumber.set(kwargs.get("phoneNumber")) or Advertisement.phoneNumber,
            Advertisement.updated.set(datetime.now())
        ])

    @classmethod
    def detailedAdvertisement(cls, advertisement):
        return {
            "fullName": advertisement.fullName,
            "companyName": advertisement.companyName,
            "taxId": advertisement.taxId,
            "email": advertisement.email,
            "phoneNumber": advertisement.phoneNumber,
            "created": advertisement.created.strftime("%Y-%m-%d"),
        }

    @classmethod
    def createTable(cls):
        if not Advertisement.exists():
            Advertisement.create_table(
                read_capacity_units=10,
                write_capacity_units=10,
                wait=True
            )

    @classmethod
    def queryByTaxId(cls, taxId):
        queryResult = []
        for item in Advertisement.query(taxId):
            queryResult.append(cls.json(item))

        return queryResult

    @classmethod
    def dropTable(cls):
        if Advertisement.exists():
            Advertisement.delete_table()

    @classmethod
    def tableDefinitions(cls):
        if Advertisement.exists():
            return Advertisement.describe_table()

    @classmethod
    def json(cls, advertisement):
        return {
            "title": advertisement.title,
            "companyName": advertisement.description,
            "taxId": advertisement.advertiserTaxId,
            "whatsAppApi": advertisement.whatsAppApi,
            "phoneNumber": advertisement.phoneNumber,
            "price": advertisement.price,
            "created": advertisement.created.strftime("%Y-%m-%d"),
        }
