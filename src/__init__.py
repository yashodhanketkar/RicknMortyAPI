from typing import Tuple

from flask import Flask, render_template
from flask_cors import CORS

# from .routes.home import _home
from .routes.ricknmortyapi import _api
from .util.logger import logger_app
from .util.set_config import configure


def error_handler(err: int) -> Tuple[dict, int]:
    status, message = str(err)[:3], str(err)[4:]
    status = int(status)
    return {
        "status": status,
        "message": message,
    }, status


def create_app() -> Flask:
    app = Flask(__name__, instance_relative_config=True, static_folder="./dist/assets", template_folder="./dist")
    cors = CORS(app)  # noqa
    app.config["CORS_HEADERS"] = "Content-Type"

    app.after_request(logger_app)

    # common errors add others in similar fashion or provide other handler function.
    app.register_error_handler(401, error_handler)
    app.register_error_handler(403, error_handler)
    app.register_error_handler(405, error_handler)
    app.register_error_handler(500, error_handler)

    with app.app_context():
        configure()

    @app.route("/", methods=["GET"])
    @app.route("/<path:path>")
    def root(path=None):
        return render_template("index.html")

    # app.register_blueprint(_home)
    app.register_blueprint(_api)

    return app
