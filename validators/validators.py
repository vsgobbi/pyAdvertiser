from datetime import datetime


class ApiValidators(object):

    @classmethod
    def isDate(cls, date):
        try:
            datetime.strptime(date, "%d/%m/%Y")
            return True
        except:
            return False

    @classmethod
    def formattedDate(cls, date):
        try:
            return cls.toISO8601(date)
        except:
            return {"error": "invalid date format"}

    @classmethod
    def toISO8601(cls, date):
        return datetime.strptime(date, "%Y-%m-%d")

    @classmethod
    def isDateISO8601(cls, date):
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return True
        except:
            return False

    @classmethod
    def unformattedDate(cls, date):
        try:
            unfarmattedDate = date.strftime("%d/%m/%Y")
            return unfarmattedDate
        except Exception as err:
            return "Couldn't format date from ISO8601 format, {}".format(err)
