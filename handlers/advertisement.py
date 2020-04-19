from flask import request, Blueprint

from models.advertisement import Advertisement
from utils.responses import ApiResponses
from validators.validators import ApiValidators

advertisement = Blueprint("advertisement", __name__)


@advertisement.route("/api/v1/advertisement", methods=["GET"])
def get():
    title = request.args.get("title")
    tags = request.args.get("tags")
    price = request.args.get("price")
    creationDate = request.args.get("creationDate")
    taxId = request.args.get("taxId")

    if taxId:
        advertisement = Advertisement.queryByTaxId(taxId)
        return ApiResponses.successMessage(item=advertisement)

    if not title or not tags:
        return ApiResponses.badRequestMessage("Parâmetro querystring 'title' ou 'tags' está faltando.")

    if price and not isinstance(price, float):
        return ApiResponses.badRequestMessage("Campo 'price' inválido, ex: 103.5 deve ser do tipo inteiro.")

    if creationDate and not ApiValidators.isDateISO8601(creationDate):
        return ApiResponses.badRequestMessage("Parâmetro 'creationDate' incorreto, ex: '2016-11-14'.")

    return ApiResponses.successMessage(item="caculatedValues")


@advertisement.route("/api/v1/advertisement", methods=["POST"])
def post():
    title = request.json["title"]
    description = request.json["desciption"]
    advertiserTaxId = request.json["advertiserTaxId"]
    price = request.json["price"]
    category = request.json["category"]
    phoneNumber = request.json["phoneNumber"]
    tags = request.json["tags"]
    picturesUrl = request.json["picturesUrl"]

    if phoneNumber:
        whatsAppApi = "https://wa.me/{phoneNumber}?text=Ol%C3%A1," \
                      "%20gostaria%20de%20saber%20mais%20sobre%20o%20portal%20ATNAP".format(phoneNumber=phoneNumber),

    try:
        advertisement = Advertisement.newItem(
            title=title,
            description=description,
            price=int(price),
            category=category,
            advertiserTaxId=advertiserTaxId,
            phoneNumber=phoneNumber,
            socialMedia="none",
            whatsAppApi=whatsAppApi if whatsAppApi else "none",
            tags=[tags],
            picturesUrl=picturesUrl
        )
        return ApiResponses.successMessage(item=advertisement)
    except:
        return ApiResponses.badRequestMessage("Erro ao criar anúncio!")

@advertisement.route("/api/v1/advertisement", methods=["PATCH"])
def patch():
    queryStringDtDate = request.args.get("date")


@advertisement.route("/api/v1/advertisement", methods=["DELETE"])
def delete():
    queryStringDtDate = request.args.get("date")
    return ApiResponses.successMessage(message="Rota deletar anúncio ainda a ser implementada")

