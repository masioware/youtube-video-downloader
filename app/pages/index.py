from flask import Blueprint, render_template

index_bp = Blueprint("Home", __name__)


@index_bp.route("/")
def index():
    return render_template("index.html")


def init(app):
    app.register_blueprint(index_bp)
