from datetime import datetime
from re import match


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

    @classmethod
    def validatePassword(cls, password):
        errors = []
        if not password:
            errors.append("Senha inválida")

        if not isinstance(password, str):
            errors.append("Senha deve ser do tipo texto")

        if len(password) < 6 or len(password) > 12:
            errors.append("Senha deve conter de 6 a 12 dígitos alphanumerico")

        return password, errors

    @classmethod
    def validateUsername(cls, username):
        errors = []
        if not username:
            errors.append("Usuário deve ser obrigatório")

        if not isinstance(username, str):
            errors.append("Usuário deve ser do tipo texto")

        if len(username) < 6 or len(username) > 20:
            errors.append("Usuário deve conter de 6 a 20 dígitos alphanumerico")

        return username, errors
    
    @classmethod
    def validateCompanyName(cls, companyName):
        errors = []
        if not companyName:
            errors.append("Nome da empresa deve ser obrigatório")

        if companyName and not isinstance(companyName, str):
            errors.append("Nome da empresa deve ser do tipo texto")

        if companyName and (len(companyName) < 3 or len(companyName) > 20):
            errors.append("Nome da empresa de 3 a 20 dígitos alphanumerico")

        return companyName, errors

    @classmethod
    def validateTaxId(cls, taxId):
        errors = []
        if not taxId:
            errors.append("CNPJ ou CPF obrigatório")

        if taxId and not isinstance(taxId, str):
            errors.append("CNPJ ou CPF deve ser do tipo texto, exemplo: '33.549.327/0001-76'")
            return taxId, errors
        if taxId and not match(
            "([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})",
            taxId
        ):
            errors.append("CPF ou CNPJ inválido! Campo deve ser formatado como: '33.549.327/0001-76'")

        return taxId, errors

    @classmethod
    def validateEmail(cls, email):
        errors = []
        if not email:
            errors.append("Campo email obrigatório")

        if not match(r"[^@]+@[^@]+\.[^@]+", email):
            errors.append("E-mail inválido, por favor, insira como exemplo: fulano@algo.com")

        return email, errors

    @classmethod
    def validateZipCode(cls, zipCode):
        errors = []
        zipCodeExpression = r"^[0-9]{5}-[0-9]{3}$"

        if not zipCode:
            errors.append("Campo CEP obrigatório")

        if not match(zipCodeExpression, zipCode):
            errors.append("CEP inválido, exemplo: 04159-040")

        return zipCode, errors

    @classmethod
    def validatePhone(cls, phoneNumber):
        errors = []
        phoneNumberExpression = r"^[0-9]{11}$"
        if not phoneNumber:
            errors.append("Campo celular obrigatório")

        if not match(phoneNumberExpression, phoneNumber):
            errors.append("Celular inválido, insira como exemplo: 18997133400")

        return phoneNumber, errors

    @classmethod
    def validateStreetLine(cls, streetLine):
        errors = []
        if not streetLine:
            errors.append("Campo endereço obrigatório")

        if len(streetLine) < 3 or len(streetLine) > 30:
            errors.append("Campo endereço inválido, insira como exemplo: Avenida das Letras, 282")

        return streetLine, errors

    @classmethod
    def validateCity(cls, city):
        errors = []
        if not city:
            errors.append("Campo cidade obrigatório")

        if len(city) < 3 or len(city) > 20:
            errors.append("Campo cidade inválido, insira como exemplo: Adamantina")

        return city, errors