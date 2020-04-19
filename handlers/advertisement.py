from flask import request, Blueprint, jsonify
from models.advertisement import Advertisement
from utils.responses import ApiResponses
from validators.validators import ApiValidators

advertisement = Blueprint("advertisement", __name__)


@advertisement.route("/api/v1/advertisement", methods=["GET"])
def get():
    queryStringTaxId = request.args.get("taxId")
    queryStringCategory = request.args.get("category")
    title = request.args.get("title")
    tags = request.args.get("tags")
    price = request.args.get("price")
    creationDate = request.args.get("creationDate")

    taxId, errors = ApiValidators.validateTaxId(taxId=queryStringTaxId)

    if len(errors) > 0:
        return ApiResponses.badRequestMessage(errors)

    if queryStringTaxId:
        advertisement = Advertisement.queryByTaxId(taxId)
        return ApiResponses.successMessage(item=advertisement)

    if not title or not tags:
        return ApiResponses.badRequestMessage("Parâmetro querystring 'title' ou 'tags' está faltando.")

    if price and not isinstance(price, float):
        return ApiResponses.badRequestMessage("Campo 'price' inválido, ex: 103.5 deve ser do tipo inteiro.")

    if creationDate and not ApiValidators.isDateISO8601(creationDate):
        return ApiResponses.badRequestMessage("Parâmetro 'creationDate' incorreto, ex: '2016-11-14'.")

    return ApiResponses.badRequestMessage("Não foi possível fazer requisição")


@advertisement.route("/api/v1/advertisement", methods=["POST"])
def post():

    title = request.json.get("title")
    category = request.json.get("category")
    description = request.json.get("description")
    price = request.json.get("price")
    tags = request.json.get("tags")
    phoneNumber = request.json.get("phoneNumber")

    tags, errors = ApiValidators.validateTags(tags)
    price, errors = ApiValidators.validatePrice(price)
    phoneNumber, errors =ApiValidators.validatePhone(phoneNumber)

    if len(errors) > 0:
        return ApiResponses.badRequestMessage(errors)

    whatsAppApi = "None"

    if phoneNumber:
        whatsAppApi = "https://wa.me/{}?text=Ol%C3%A1," \
                      "%20gostaria%20de%20saber%20mais%20sobre%20o%20portal%20ATNAP".format(phoneNumber)

    try:
        Advertisement.newItem(
            title=title,
            description=description,
            price=price,
            category=category,
            advertiserTaxId="06.990.590/0001-23",
            phoneNumber=phoneNumber,
            whatsAppApi=whatsAppApi,
            tags=tags,
        )
        return ApiResponses.successMessage(message="sucesso", item="Anúncio '{}' foi registrado".format(title))
    except Exception as error:
        return ApiResponses.badRequestMessage("Erro ao criar anúncio! {}".format(error))


@advertisement.route("/api/v1/advertisement", methods=["PATCH"])
def patch():
    queryStringDtDate = request.args.get("date")


@advertisement.route("/api/v1/advertisement", methods=["DELETE"])
def delete():
    queryStringDtDate = request.args.get("date")
    return ApiResponses.successMessage(message="Rota deletar anúncio ainda a ser implementada")

