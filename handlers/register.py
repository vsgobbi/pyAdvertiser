from flask import request, Blueprint

register = Blueprint("register", __name__)


@register.route("/api/v1/register", methods=["GET"])
def get():
    username = request.args.get("username")
    password = request.args.get("password")
    taxId = request.args.get("taxId")


@register.route("/api/v1/register", methods=["POST"])
def post():
    taxId = request.json.get("taxId")
    password = request.json.get("password")
    fullName = request.json.get("fullName")
    companyName = request.json.get("companyName")
    email = request.json.get("email")
    phoneNumber = request.json.get("phoneNumber")
