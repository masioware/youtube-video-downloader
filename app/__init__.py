from flask import Flask

from app.api import video
from app.pages import index


def create_app():
    app = Flask(__name__)

    index.init(app)
    video.init(app)

    return app
