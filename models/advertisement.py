from datetime import datetime
from utils.configs import region
from pynamodb.models import Model
from pynamodb.attributes import UTCDateTimeAttribute, UnicodeAttribute, UnicodeSetAttribute, NumberAttribute


class Advertisement(object, Model):

    class Meta:
        table_name = "atnap_advertisement"
        region = region

    created = UTCDateTimeAttribute(null=False, default=datetime.now())
    updated = UTCDateTimeAttribute(null=True)
    deletedBy = UnicodeAttribute()
    title = UnicodeAttribute(null=False, hash_key=True)
    category = UnicodeAttribute(null=False, range_key=True)
    picturesUrl = UnicodeAttribute(null=True)
    description = UnicodeAttribute(null=False)
    tags = UnicodeSetAttribute(null=False)
    price = NumberAttribute(null=False)

    @classmethod
    def newItem(cls, fullName, companyName, taxId, email, phoneNumber):
        advertiser = Advertisement(
            fullName=fullName,
            companyName=companyName,
            taxId=taxId,
            phoneNumber=phoneNumber,
            email=email,
        )
        return advertiser.save()

    @classmethod
    def deleteItem(cls, taxId, email):
        advertiser = Advertisement(
            taxId=taxId,
            email=email
        )
        return advertiser.delete()

    @classmethod
    def detailedAdvertisement(cls, advertiser):
        return {
            "fullName": Advertisement.fullName,
            "companyName": advertiser.companyName,
            "taxId": advertiser.taxId,
            "email": advertiser.email,
            "phoneNumber": advertiser.phoneNumber,
            "created": advertiser.created.strftime("%Y-%m-%d"),
        }

    @classmethod
    def json(cls, advertiser):
        return {
            "fullName": Advertisement.fullName,
            "companyName": advertiser.companyName,
            "taxId": advertiser.taxId,
            "email": advertiser.email,
            "phoneNumber": advertiser.phoneNumber,
            "created": advertiser.created.strftime("%Y-%m-%d"),
        }
