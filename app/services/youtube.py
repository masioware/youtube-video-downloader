from io import BytesIO

from pytube import YouTube


class Downloader:
    def __init__(self, url):
        self.video = YouTube(url)

    def get_streams(self, filters, order_by):
        return self.video.streams.filter(**filters).order_by(order_by)

    def get_video_info(self, streams):
        resolutions = [stream.resolution for stream in streams]

        return {
            "title": self.video.title,
            "length": self.video.length,
            "thumbnail": self.video.thumbnail_url,
            "resolutions": resolutions
        }

    def get_stream_by_resolution(self, resolution, streams):
        return streams.filter(resolution=resolution).desc().first()

    def get_highest_resolution_stream(self, streams):
        return streams.desc().first()

    def download(self, stream):
        buffer = BytesIO()

        stream.stream_to_buffer(buffer)

        buffer.seek(0)

        return buffer
