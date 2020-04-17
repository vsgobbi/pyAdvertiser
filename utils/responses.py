from flask import Response, jsonify


class ApiResponses(object):
    Response.headers = {"application/json"}

    @classmethod
    def badRequestMessage(cls, error):
        return jsonify({"error": error}), 400

    @classmethod
    def successMessage(cls, message=None, item=None):
        if message:
            return jsonify({message: item}), 200
        return jsonify(item), 200

    @classmethod
    def notFoundMessage(cls, message):
        return jsonify({"error": message}), 404
