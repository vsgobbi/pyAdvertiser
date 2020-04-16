from datetime import datetime
from utils.configs import region
from pynamodb.models import Model
from pynamodb.attributes import UTCDateTimeAttribute, UnicodeAttribute, UnicodeSetAttribute, NumberAttribute


class Advertisement(object, Model):

    class Meta:
        table_name = "advertisement"
        region = region

    created = UTCDateTimeAttribute(null=False, default=datetime.now())
    updated = UTCDateTimeAttribute(null=True)
    deletedBy = UnicodeAttribute()
    title = UnicodeAttribute(null=False, hash_key=True)
    category = UnicodeAttribute(null=False, range_key=True)
    description = UnicodeAttribute(null=False)
    tags = UnicodeSetAttribute(null=False)
    price = NumberAttribute(null=False)
