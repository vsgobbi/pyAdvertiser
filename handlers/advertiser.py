from flask import request, Blueprint
from models.advertiser import Advertiser
from utils.responses import ApiResponses

advertiser = Blueprint("advertiser", __name__)


@advertiser.route("/api/v1/advertiser", methods=["GET"])
def get():
    queryStringTaxId = request.args.get("taxId")

    if not queryStringTaxId:
        return ApiResponses.badRequestMessage("missing taxId query string parameter")

    if Advertiser.exists():
        advertiser = Advertiser.queryByTaxId(taxId=queryStringTaxId)
        return ApiResponses.successMessage(Advertiser.json(advertiser))


@advertiser.route("/api/v1/advertiser", methods=["POST"])
def post():
    fullName = request.json["fullName"]
    companyName = request.json["companyName"]


@advertiser.route("/api/v1/advertiser", methods=["PATCH"])
def patch():
    items = {}
    allowedKeys = ["taxId", "fullName", "companyName", "phoneNumber"]

    taxId = request.json.get("taxId")
    fullName = request.json.get("fullName")
    companyName = request.json.get("companyName")
    email = request.json.get("email")
    phoneNumber = request.json.get("phoneNumber")

    for key in request.json.keys:
        if key in allowedKeys:
            items.update({request.json.keys: request.json[key]})

    Advertiser.updateItem(**items)


@advertiser.route("/api/v1/advertiser", methods=["DELETE"])
def delete():
    queryStringDtDate = request.args.get("dtDate")
