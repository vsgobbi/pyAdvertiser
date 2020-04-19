from flask import request, Blueprint
from models.user import User
from utils.responses import ApiResponses
from validators.validators import ApiValidators

register = Blueprint("register", __name__)


@register.route("/api/v1/register", methods=["GET"])
def get():
    # Logged in:
    taxId = request.args.get("taxId")
    email = request.args.get("email")
    taxId = ApiValidators.validateTaxId(taxId)

    user = User.queryByTaxIdAndEmail(taxId, email)
    item = User.json(user)
    return ApiResponses.successMessage(item)


@register.route("/api/v1/register", methods=["POST"])
def post():
    taxId = request.json.get("taxId")
    password = request.json.get("password")
    fullName = request.json.get("fullName")
    email = request.json.get("email")
    phoneNumber = request.json.get("phoneNumber")

    ApiValidators.validateEmail(email)
    ApiValidators.validatePassword(password)
    ApiValidators.validatePhone(phoneNumber)
    ApiValidators.validateTaxId(taxId)
    ApiValidators.validateUsername(fullName)
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
def get():
    return ApiResponses.successMessage(message="Rota deletar usuário ainda a ser implementada")
