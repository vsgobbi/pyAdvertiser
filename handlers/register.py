from flask import request, Blueprint
from models.user import User
from utils.responses import ApiResponses
from validators.validators import ApiValidators

register = Blueprint("register", __name__)


@register.route("/api/v1/register", methods=["GET"])
def get():
    # Logged in:
    queryStringtaxId = request.args.get("taxId")
    queryStringemail = request.args.get("email")
    taxId, errors = ApiValidators.validateTaxId(queryStringtaxId)

    if len(errors) > 0:
        return ApiResponses.badRequestMessage(errors)

    user = User.queryByTaxIdAndEmail(taxId, queryStringemail)
    item = User.json(user)
    return ApiResponses.successMessage(item)


@register.route("/api/v1/register", methods=["POST"])
def post():
    taxId = request.json.get("taxId")
    password = request.json.get("password")
    fullName = request.json.get("fullName")
    email = request.json.get("email")
    phoneNumber = request.json.get("phoneNumber")

    taxId, errors = ApiValidators.validateTaxId(taxId)
    email, errors = ApiValidators.validateEmail(email)
    password, errors = ApiValidators.validatePassword(password)
    phoneNumber, errors = ApiValidators.validatePhone(phoneNumber)
    fullName, errors = ApiValidators.validateUsername(fullName)

    if len(errors) > 0:
        return ApiResponses.badRequestMessage(errors)

    try:
        User.newItem(
            fullName,
            password,
            taxId,
            email,
            phoneNumber
        )
        return ApiResponses.successMessage(message="sucesso", item="novo usuário registrado")
    except Exception as error:
        return ApiResponses.badRequestMessage("Não foi possível criar usuário, {}".format(error))


@register.route("/api/v1/register", methods=["DELETE"])
def delete():
    return ApiResponses.successMessage(message="Rota deletar usuário ainda a ser implementada")
