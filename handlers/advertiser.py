from flask import request, Blueprint
from models.advertiser import Advertiser
from utils.responses import ApiResponses
from validators.authentication import authenticated
from validators.validators import ApiValidators

advertiser = Blueprint("advertiser", __name__)


@advertiser.route("/api/v1/advertiser", methods=["GET"])
@authenticated
def get():
    queryStringTaxId = request.args.get("taxId")
    queryStringEmail = request.args.get("email")

    taxId, errors = ApiValidators.validateTaxId(taxId=queryStringTaxId)

    if len(errors) > 0:
        return ApiResponses.badRequestMessage(errors)

    if queryStringTaxId:
        advertiser = Advertiser.queryByTaxId(taxId)
        return ApiResponses.successMessage(item=advertiser)

    if queryStringEmail and queryStringTaxId:
        email = ApiValidators.validateEmail(queryStringEmail)
        taxId = ApiValidators.validateTaxId(queryStringTaxId)
        advertiser = Advertiser.queryByTaxIdAndEmail(taxId, email)
        return ApiResponses.successMessage(item=advertiser)

    if Advertiser.exists():
        advertiser = Advertiser.queryByTaxId(taxId=queryStringTaxId)
        return ApiResponses.successMessage(Advertiser.json(advertiser))

    if not queryStringEmail and not queryStringTaxId:
        advertisers = Advertiser.scanAll()
        return ApiResponses.successMessage(item=advertisers)


@advertiser.route("/api/v1/advertiser", methods=["POST"])
@authenticated
def post():

    fullName = request.json["fullName"]
    companyName = request.json["companyName"]
    taxId = request.json["taxId"]
    email = request.json["email"]
    phoneNumber = request.json["phoneNumber"]

    taxId, errors = ApiValidators.validateTaxId(taxId)
    email, errors = ApiValidators.validateEmail(email)
    companyName, errors = ApiValidators.validateCompanyName(companyName)
    phoneNumber, errors =ApiValidators.validatePhone(phoneNumber)

    if len(errors) > 0:
        return ApiResponses.badRequestMessage(errors)

    try:
        Advertiser.newItem(
            fullName=fullName,
            companyName=companyName,
            taxId=taxId,
            email=email,
            phoneNumber=phoneNumber
        )
        return ApiResponses.successMessage(
            message="sucesso",
            item="Empresa '{}' foi registrada".format(companyName)
        )
    except Exception as error:
        return ApiResponses.badRequestMessage("{}".format(error))


@advertiser.route("/api/v1/advertiser", methods=["PATCH"])
@authenticated
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

    try:
        Advertiser.updateItem(**items)
        return ApiResponses.successMessage(
            message="sucesso",
            item="Empresa '{}' foi atualizada".format(companyName)
        )
    except Exception as error:
        return ApiResponses.badRequestMessage("{}".format(error))


@advertiser.route("/api/v1/advertiser", methods=["DELETE"])
@authenticated
def delete():
    queryStringTaxId = request.args.get("taxId")
    queryStringEmail = request.args.get("email")

    taxId = ApiValidators.validateTaxId(queryStringTaxId)
    email = ApiValidators.validateEmail(queryStringEmail)
    try:
        advertiser = Advertiser.deleteItem(taxId, email)
        return ApiResponses.successMessage(message="Empresa deletada com sucesso", item=Advertiser.json(advertiser))
    except Exception as error:
        return ApiResponses.badRequestMessage("Não foi possível deletar empresa {0}, {1}".format(taxId, error))
