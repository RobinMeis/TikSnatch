from yt_dlp import YoutubeDL
from os import path
from hashlib import sha256
from datetime import datetime

from .exceptions import VideoNotDownloaded

class Video:
    def __init__(self, channel, id, url, timestamp, title, description):
        self.channel = channel
        self.id = id
        self.url = url
        self.timestamp = datetime.fromtimestamp(timestamp)
        self.timestamp_download = None
        self.title = title
        self.description = description
        self.filepath = None
        self.sha256_hash = None

    def calculate_sha256(self):
        """Calculate SHA256 hash of a file."""

        if self.filepath is None:
            raise VideoNotDownloaded

        sha256_hash = sha256()
        with open(self.filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        self.sha256_hash = sha256_hash.hexdigest()

    def download(self, output_directory):
        """Download a TikTok video using yt-dlp."""
        timestamp = self.timestamp.strftime("%Y-%m-%d_%H%M%S")
        file_name = f"{timestamp}_{self.channel.username}_{self.id}.mp4"
        self.filepath = path.join(output_directory, file_name)
        
        # Configure yt-dlp for download
        ydl_opts = {
            'quiet': False,
            'no_warnings': True,
            'outtmpl': self.filepath,
            'format': 'best'
        }
        
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.url])

        self.timestamp_download = datetime.now()
        self.calculate_sha256()

    def __str__(self):
        return (
            f"Video:\n"
            f"  ID         : {self.id or '-'}\n"
            f"  Title      : {self.title or '-'}\n"
            f"  URL        : {self.url}\n"
            f"  Timestamp  : {self.timestamp.isoformat()}\n"
            f"  Description: {self.description or '-'}\n"
            f"  SHA256 Hash: {self.sha256_hash or '-'}"
        )

    def __repr__(self):
        return f"Video(title={self.title!r}, url={self.url!r})"