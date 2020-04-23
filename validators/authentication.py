from flask import session
from functools import wraps
from utils.kms import ApiKms


def validCredentials(user, taxId, password):
    return user.taxId == taxId and password == ApiKms.decrypt(user.passwordHash)


def authenticated(func):
    @wraps(wrapped=func)
    def wrapper(*args, **kwargs):
        if not session.get("loggedin"):
            return {'Login!', 401, {'WWW-Authenticate': 'Basic realm="Login!"'}}

        return func(*args, **kwargs)
    return wrapper
