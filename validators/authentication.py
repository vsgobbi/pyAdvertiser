from flask import session
from functools import wraps
from models.user import User
from utils.kms import ApiKms
from utils.responses import ApiResponses


def validCredentials(user, taxId, password):
    return user.taxId == taxId and password == ApiKms.decrypt(user.passwordHash)


def validLoggedUser(taxId):
    return session.get("user")["taxId"] == taxId


def validateUser(taxId):
    user = User.queryUserByTaxId(taxId)

    if not user:
        return ApiResponses.notFoundMessage(message="Usuário não existe")

    if user.taxId != taxId:
        return ApiResponses.badRequestMessage(error="Usuário {} não encontrado!".format(taxId))

    return user


def authenticated(func):
    @wraps(wrapped=func)
    def wrapper(*args, **kwargs):
        if not session.get("loggedin"):
            return ApiResponses.forbiddenMessage(message="login necessário")

        return func(*args, **kwargs)
    return wrapper


def allowedUser(func):
    @wraps(wrapped=func)
    def wrapper(*args, **kwargs):
        wrapper.bla = "bla bla"
        user = session.get("user")
        if not user:
            return ApiResponses.notFoundMessage(message="Usuário não encontrado")

        if "owner" not in user.get("permissions"):
            return ApiResponses.forbiddenMessage(message="Você não possui permissões suficientes")

        return func(*args, **kwargs)
    return wrapper