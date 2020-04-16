from flask import request, Blueprint
from utils.responses import ApiResponses
from validators.validators import ApiValidators

advertisement = Blueprint("advertisement", __name__)


@advertisement.route("/api/v1/advertisement", methods=["GET"])
def get():
    cdbRate = request.json["cdbRate"]
    investmentDate = request.json["investmentDate"]
    currentDate = request.json["currentDate"]

    if not cdbRate:
        return ApiResponses.badRequestMessage("missing cdbRate parameter")

    if cdbRate and not isinstance(cdbRate, float):
        return ApiResponses.badRequestMessage("invalid data type of cdbRate parameter, ex: 103.5 must be integer")

    if not investmentDate:
        return ApiResponses.badRequestMessage("missing investmentDate parameter")

    if not currentDate:
        return ApiResponses.badRequestMessage("missing currentDate parameter")

    if investmentDate and not ApiValidators.isDateISO8601(investmentDate):
        return ApiResponses.badRequestMessage("invalid format of investmentDate parameter, ex: 2016-11-14")

    if currentDate and not ApiValidators.isDateISO8601(currentDate):
        return ApiResponses.badRequestMessage("invalid format of currentDate parameter, ex: 2016-12-26")

    investmentDate = ApiValidators.formattedDate(investmentDate)
    currentDate = ApiValidators.formattedDate(currentDate)

    return ApiResponses.successMessage(item="caculatedValues")


@advertisement.route("/api/v1/advertisement", methodos=["POST"])
def post():
    title = request.json["title"]
    description = request.json["desciption"]


@advertisement.route("/api/v1/advertisement", methods=["PATCH"])
def patch():
    queryStringDtDate = request.args.get("date")


@advertisement.route("/api/v1/advertisement", methods=["DELETE"])
def delete():
    queryStringDtDate = request.args.get("date")
