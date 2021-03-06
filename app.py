from flask import Flask
from utils.configs import sessionSecretKey
from utils.responses import ApiResponses
from handlers.advertiser import advertiser
from handlers.advertisement import advertisement
from handlers.register import register
from handlers.login import login, login_manager
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.register_blueprint(advertiser)
app.register_blueprint(advertisement)
app.register_blueprint(register)
app.register_blueprint(login)
login_manager.init_app(app)
cors = CORS(app)

app.config["CORS_HEADERS"] = "Content-Type"
app.config["SECRET_KEY"] = sessionSecretKey


@cross_origin()
@app.route("/", methods=["GET"])
def home():
    return ApiResponses.successMessage(
        item="Bem-vindo(a) ao portal ATNAP"
    )


@app.route("/api/v1", methods=["GET"])
def get():
    return ApiResponses.successMessage(
        item="Bem-vindo(a) a API v1 da ATNAP!"
    )


@app.route("/api/v1", methods=["POST"])
def post():
    return ApiResponses.badRequestMessage("Rota inválida")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
