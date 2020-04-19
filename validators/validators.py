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
        if not password:
            return "Senha inválida"

        if not isinstance(password, str):
            return "Senha deve ser do tipo texto"

        if len(password) < 6 or len(password) > 12:
            return "Senha deve conter de 6 a 12 dígitos alphanumerico"

    @classmethod
    def validateUsername(cls, username):
        if not username:
            return "Usuário deve ser obrigatório"

        if not isinstance(username, str):
            return "Usuário deve ser do tipo texto"

        if len(username) < 6 or len(username) > 20:
            return "Usuário deve conter de 6 a 20 dígitos alphanumerico"

    @classmethod
    def validateTaxId(cls, taxId):
        cpfRegex = r"[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}"
        cnpjRegex = r"[0-9]{2}\.?[0-9]{3}\.?[0-9]{3}\/?[0-9]{4}\-?[0-9]{2}"
        if not taxId:
            return "CNPJ ou CPF obrigatório"

        if not match(cpfRegex, taxId) or not match(cnpjRegex, taxId):
            return "CPF ou CNPJ inválido! Campo deve ser formatado como: '33.549.327/0001-76'"

    @classmethod
    def validateEmail(cls, email):
        if not email:
            return "Campo email obrigatório"

        if not match(r"[^@]+@[^@]+\.[^@]+", email):
            return "E-mail inválido, por favor, insira como exemplo: fulano@algo.com"

    @classmethod
    def validateZipCode(cls, zipCode):
        zipCodeExpression = r"^[0-9]{5}-[0-9]{3}$"
        if not match(zipCodeExpression, zipCode):
            return "CEP inválido, exemplo: 04159-040"

    @classmethod
    def validatePhone(cls, phoneNumber):
        phoneNumberExpression = r"^[0-9]{11}$"
        if not phoneNumber:
            return "Campo celular obrigatório"

        if not match(phoneNumberExpression, phoneNumber):
            return "Celular inválido, insira como exemplo: 18997133400"

    @classmethod
    def validateStreetLine(cls, streetLine):
        if not streetLine:
            return "Campo endereço obrigatório"

        if len(streetLine) < 3 or len(streetLine) > 30:
            return "Campo endereço inválido, insira como exemplo: Avenida das Letras, 282"

    @classmethod
    def validateCity(cls, city):
        if not city:
            return "Campo cidade obrigatório"

        if len(city) < 3 or len(city) > 20:
            return "Campo cidade inválido, insira como exemplo: Adamantina"
