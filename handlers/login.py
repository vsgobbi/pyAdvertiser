from flask import request, Blueprint, session
from flask_login import LoginManager
from models.user import User
from utils.responses import ApiResponses
from validators.authentication import authenticated, validCredentials, allowedUser, validateUser
from validators.validators import ApiValidators

login = Blueprint("login", __name__)
login_manager = LoginManager()


@login.route("/api/v1/login", methods=["GET"])
@authenticated
@allowedUser
def get():
    queryStringtaxId = request.args.get("taxId")

    taxId, errors = ApiValidators.validateTaxId(queryStringtaxId)

    if len(errors) > 0:
        return ApiResponses.badRequestMessage(errors)

    try:
        user = validateUser(taxId)
        return ApiResponses.successMessage(item="Usuário {} logado".format(user.fullName))
    except:
        return ApiResponses.badRequestMessage("Usuário inválido!")


@login.route("/api/v1/login", methods=["POST"])
def post():
    try:
        taxId = request.json.get("taxId")
        password = request.json.get("password")
    except:
        return ApiResponses.badRequestMessage("Parâmetros 'taxId' e 'password' necessários")

    taxId, errors = ApiValidators.validateTaxId(taxId)

    if len(errors) > 0:
        return ApiResponses.badRequestMessage(errors)

    user = validateUser(taxId)

    if validCredentials(user, taxId, password):
        session["loggedin"] = True
        session["user"] = User.json(user)
        return ApiResponses.successMessage(item="Usuário {} logado com sucesso".format(taxId))

    return ApiResponses.badRequestMessage("Senha incorreta!")
