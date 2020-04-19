from flask import Response, jsonify


class ApiResponses(object):
    Response.headers = {"application/json"}

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
