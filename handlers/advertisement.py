from flask import request, Blueprint
from utils.responses import ApiResponses
from validators.validators import ApiValidators

advertisement = Blueprint("advertisement", __name__)


@advertisement.route("/api/v1/advertisement", methods=["GET"])
def get():
    creationDate = request.args.get["creationDate"]
    title = request.args.get("title")
    tags = request.args.get("tags")
    price = request.args.get("price")

    if not title or not tags:
        return ApiResponses.badRequestMessage("Parâmetro querystring 'title' ou 'tags' está faltando.")

    if price and not isinstance(price, float):
        return ApiResponses.badRequestMessage("invalid data type of price parameter, ex: 103.5 must be integer")

    if creationDate and not ApiValidators.isDateISO8601(creationDate):
        return ApiResponses.badRequestMessage("Parâmetro creationDate incorreto")

    if creationDate and not ApiValidators.isDateISO8601(creationDate):
        return ApiResponses.badRequestMessage("invalid format of creationDate parameter, ex: 2016-11-14")

    creationDate = ApiValidators.formattedDate(creationDate)

    return ApiResponses.successMessage(item="caculatedValues")


@advertisement.route("/api/v1/advertisement", methods=["POST"])
def post():
    title = request.json["title"]
    description = request.json["desciption"]


@advertisement.route("/api/v1/advertisement", methods=["PATCH"])
def patch():
    queryStringDtDate = request.args.get("date")


@advertisement.route("/api/v1/advertisement", methods=["DELETE"])
def delete():
    queryStringDtDate = request.args.get("date")
    return ApiResponses.successMessage(message="Rota deletar anúncio ainda a ser implementada")

