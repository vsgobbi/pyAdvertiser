from flask import request, Blueprint

login = Blueprint("login", __name__)


@login.route("/api/v1/login", methods=["GET"])
def get():
    username = request.args.get("username")
    password = request.args.get("password")
    taxId = request.args.get("taxId")


@login.route("/api/v1/login", methods=["POST"])
def post():
    taxId = request.json.get("taxId")
    password = request.json.get("password")

