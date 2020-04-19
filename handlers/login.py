from flask import request, Blueprint
from flask_login import LoginManager, login_user
from models.user import User
from utils.responses import ApiResponses
from validators.validators import ApiValidators
from utils.kms import ApiKms

login = Blueprint("login", __name__)
login_manager = LoginManager()


@login.route("/api/v1/login", methods=["GET"])
def get():
    queryStringtaxId = request.args.get("taxId")

    taxId, errors = ApiValidators.validateTaxId(queryStringtaxId)

    if len(errors) > 0:
        return ApiResponses.badRequestMessage(errors)
    try:
        user = User.queryByTaxId(taxId)
        return ApiResponses.successMessage(message="Usuário {} logado".format(user.fullName))
    except Exception as error:
        return ApiResponses.badRequestMessage("Não foi possível verificar usuário logado, {}".format(error))


@login.route("/api/v1/login", methods=["POST"])
def post():
    try:
        taxId = request.json.get("taxId")
        password = request.json.get("password")
    except:
        return ApiResponses.badRequestMessage("Parâmetros taxId e password faltantes")

    taxId, errors = ApiValidators.validateTaxId(taxId)

    if len(errors) > 0:
        return ApiResponses.badRequestMessage(errors)

    user = User.queryByTaxId(taxId)
    if not user:
        return ApiResponses.badRequestMessage("Usuário {} inválido!".format(taxId))

    passwordHash = User.getPasswordTaxId(taxId)

    if password != ApiKms.decrypt(passwordHash):
        return ApiResponses.badRequestMessage("senha incorreta!")

    try:
        if password == ApiKms.decrypt(passwordHash):
            return ApiResponses.successMessage(item="Usuário {} logado com sucesso".format(taxId))
    except Exception as error:
        return ApiResponses.badRequestMessage("erro ao verificar usuário, {}".format(error))
