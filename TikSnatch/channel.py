from yt_dlp import YoutubeDL
from .video import Video

class Channel:
    def __init__(self, username):
        self.username = username
        self.name = None
        self.channel_id = None
        self.videos = []

    def get(self):
        # Fetches & parses channel details
        info = self._fetch_info()
        self._parse_info(info)

    def _fetch_info(self):
        # Downloads channel details
        url = f"https://www.tiktok.com/@{self.username}"
        
        # Configure yt-dlp
        ydl_opts = {
            'extract_flat': True,
            'quiet': True,
            'no_warnings': True,
            'skip_download': True
        }
        
        with YoutubeDL(ydl_opts) as ydl:
            return ydl.extract_info(url, download=False)

    def _parse_info(self, info):
        # Parses channel details
        if info and 'entries' in info:
            videos = info['entries']

            if not videos:
                return  # No videos found

            self.channel_id = videos[0]["uploader_id"]
            self.name = videos[0]["channel"]

            for video in videos:
                if not video.get("url") or not video.get("timestamp"):
                    continue  # Skip broken/incomplete videos

                self.videos.append(Video(
                    channel = self,
                    id = video["id"],
                    url = video["url"],
                    timestamp = video["timestamp"],
                    title=video.get("title", None),
                    description=video.get("description", None)
                )) 

    def __repr__(self):
        return (
            f"<Channel(username='{self.username}', "
            f"name='{self.name}', "
            f"channel_id='{self.channel_id}', "
            f"videos={len(self.videos)})>"
        )

    def __str__(self):
        return (
            f"Channel: {self.name or self.username}\n"
            f"Username: @{self.username}\n"
            f"Channel ID: {self.channel_id}\n"
            f"Videos: {len(self.videos)}"
        )