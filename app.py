from flask import Flask
from utils.responses import ApiResponses
from handlers.advertiser import advertiser
from handlers.advertisement import advertisement
from handlers.register import register
from handlers.login import login, login_manager

app = Flask(__name__)
app.secret_key = b'some secret word'
app.register_blueprint(advertiser)
app.register_blueprint(advertisement)
app.register_blueprint(register)
app.register_blueprint(login)
login_manager.init_app(app)


@app.route("/", methods=["GET"])
def home():
    return ApiResponses.successMessage(
        "message",
        "Our API is working!"
    )


@app.route("/api/v1", methods=["GET"])
def get():
    return ApiResponses.successMessage(
        "message",
        "API v1 working!"
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
