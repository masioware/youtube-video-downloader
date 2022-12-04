from io import BytesIO

from flask import Blueprint, request, send_file
from pytube import YouTube

download_bp = Blueprint("Download", __name__)


@download_bp.route("/download", methods=["POST"])
def download():
    url = request.form.get("url")

    buffer = BytesIO()

    yt = YouTube(url)
    yt.streams.filter(
        progressive=True,
        file_extension="mp4"
    ).order_by("resolution").desc().first().stream_to_buffer(buffer)

    buffer.seek(0)

    return send_file(
        buffer,
        download_name=f"{yt.title}.mp4",
        mimetype="video/mp4",
        as_attachment=True
    )


def init(app):
    app.register_blueprint(download_bp)
