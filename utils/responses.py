from flask import Response, jsonify, make_response


class ApiResponses(object):
    response = Response()
    # Response.headers = {"application/json"}
    response.headers.add("Content-Type", "application/json")
    response.headers.add("Access-Control-Allow-Origin", "*")

    Response.headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
    }

    @classmethod
    def badRequestMessage(cls, error):
        return jsonify({"erro": error}), 400

    @classmethod
    def successMessage(cls, message=None, item=None):
        if message:
            return jsonify({message: item}), 200
        return jsonify({"sucesso": item}), 200

    @classmethod
    def notFoundMessage(cls, message):
        return jsonify({"erro": message}), 404

    @classmethod
    def forbiddenMessage(cls, message):
        return jsonify({"acesso negado": message}), 401