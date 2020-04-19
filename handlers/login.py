from flask import request, Blueprint
from flask_login import LoginManager, login_user

from utils.responses import ApiResponses

login = Blueprint("login", __name__)
login_manager = LoginManager()


@login.route("/api/v1/login", methods=["GET"])
def get():
    username = request.args.get("username")
    password = request.args.get("password")
    taxId = request.args.get("taxId")

    return ApiResponses.successMessage("message", "login")


@login.route("/api/v1/login", methods=["POST"])
def post():
    taxId = request.json.get("taxId")
    password = request.json.get("password")
    email = request.json.get("email")

    login_user(user)
