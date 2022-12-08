from flask import Blueprint, request, send_file, jsonify

from app.services.youtube import Downloader

video_bp = Blueprint("Video", __name__)


@video_bp.route("/download", methods=["POST"])
def download():
    url = request.form.get("url")
    resolution = request.form.get("resolution")

    downloader = Downloader(url)

    streams = downloader.get_streams({
        "progressive": True,
        "file_extension": "mp4"
    }, order_by="resolution")

    video_info = downloader.get_video_info(streams)

    stream = downloader.get_stream_by_resolution(resolution, streams)

    buffer = downloader.download(stream)

    return send_file(
        buffer,
        download_name=f"{video_info['title']}.mp4",
        mimetype="video/mp4",
        as_attachment=True
    )


@video_bp.route("/video_info", methods=["GET"])
def get_video_info():
    url = request.args.get("url")

    downloader = Downloader(url)
    streams = downloader.get_streams({
        "progressive": True,
        "file_extension": "mp4"
    }, order_by="resolution")

    video_info = downloader.get_video_info(streams)

    return jsonify(
        title=video_info["title"],
        length=video_info["length"],
        thumbnail=video_info["thumbnail"],
        resolutions=video_info["resolutions"]
    )


def init(app):
    app.register_blueprint(video_bp)
