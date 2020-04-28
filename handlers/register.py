from flask import request, Blueprint, session
from models.user import User
from utils.responses import ApiResponses
from validators.authentication import authenticated, allowedUser, validateUser, validLoggedUser
from validators.validators import ApiValidators

register = Blueprint("register", __name__)


@register.route("/api/v1/register", methods=["GET"])
@authenticated
@allowedUser
def get():
    queryStringtaxId = request.args.get("taxId")
    taxId, errors = ApiValidators.validateTaxId(queryStringtaxId)

    if len(errors) > 0:
        return ApiResponses.badRequestMessage(errors)

    if not validLoggedUser(taxId):
        return ApiResponses.forbiddenMessage("Cadastro inválido!")

    try:
        validLoggedUser(taxId)
        user = validateUser(taxId)
        return ApiResponses.successMessage(item=User.json(user))
    except:
        return ApiResponses.badRequestMessage("Usuário inválido!")


@register.route("/api/v1/register", methods=["POST"])
def post():
    taxId = request.json.get("taxId")
    password = request.json.get("password")
    fullName = request.json.get("fullName")
    email = request.json.get("email")
    phoneNumber = request.json.get("phoneNumber")
    permissions = request.json.get("permissions")

    taxId, errors = ApiValidators.validateTaxId(taxId)
    email, errors = ApiValidators.validateEmail(email)
    password, errors = ApiValidators.validatePassword(password)
    permissions, errors = ApiValidators.validatePermissions(permissions)
    phoneNumber, errors = ApiValidators.validatePhone(phoneNumber)
    fullName, errors = ApiValidators.validateUsername(fullName)

    if len(errors) > 0:
        return ApiResponses.badRequestMessage(errors)

    if session.get("loggedin"):
        return ApiResponses.badRequestMessage(error="Usuário já logado")

    user = User.queryUserByTaxId(taxId)
    if user:
        return ApiResponses.badRequestMessage(error="Usuário já existe, verifique sua conta...")

    try:
        User.newItem(
            fullName,
            password,
            taxId,
            email,
            phoneNumber,
            permissions
        )
        return ApiResponses.successMessage(message="sucesso", item="Usuário '{}' foi registrado".format(fullName))
    except Exception as error:
        return ApiResponses.badRequestMessage("Não foi possível criar usuário, {}".format(error))


@register.route("/api/v1/register", methods=["DELETE"])
@authenticated
@allowedUser
def delete():

    queryStringtaxId = request.args.get("taxId")
    taxId, errors = ApiValidators.validateTaxId(queryStringtaxId)

    if len(errors) > 0:
        return ApiResponses.badRequestMessage(errors)

    user = User.queryUserByTaxId(taxId)
    if user:
        user.delete()
        return ApiResponses.successMessage(message="Usuário deletado com sucesso", item=User.json(user))

    return ApiResponses.notFoundMessage("Usuário não encontrado")
