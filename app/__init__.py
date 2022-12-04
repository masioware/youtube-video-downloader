from flask import Flask

from app.api import download
from app.pages import index


def create_app():
    app = Flask(__name__)

    index.init(app)
    download.init(app)

    return app
