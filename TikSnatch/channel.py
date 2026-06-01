from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError  # Ensure this is imported
from .video import Video

class Channel:
    def __init__(self, username):
        self.username = username
        self.name = None
        self.channel_id = None
        self.videos = []

    def get(self, cookies=None):
        # Fetches & parses channel details
        info = self._fetch_info(cookies)
        self._parse_info(info)

    def _fetch_info(self, cookies):
        url = f"https://www.tiktok.com/@{self.username}"
        
        ydl_opts = {
            'extract_flat': True,
            'quiet': True,
            'no_warnings': True,
            'skip_download': True,
        }

        if cookies:
            ydl_opts['cookiefile'] = cookies.cookie_file
        
        with YoutubeDL(ydl_opts) as ydl:
            try:
                return ydl.extract_info(url, download=False)
            except DownloadError as e:
                # Catch empty channel exception and pass a fallback indicator
                if "This account does not have any videos posted" in str(e):
                    return {"is_empty_channel": True}
                raise e

    def _parse_info(self, info):
        if not info:
            return

        # Handle empty channels gracefully with safe fallbacks
        if info.get("is_empty_channel"):
            self.name = self.username  # Fallback display name to username
            self.channel_id = "Unknown"
            self.videos = []
            return

        if 'entries' in info:
            videos = info['entries']

            if not videos:
                return  

            # Safeguard extraction in case fields are missing
            self.channel_id = videos[0].get("uploader_id", "Unknown")
            self.name = videos[0].get("channel", self.username)

            for video in videos:
                if not video.get("url") or not video.get("timestamp"):
                    continue  

                self.videos.append(Video(
                    channel = self,
                    id = video["id"],
                    url = video["url"],
                    timestamp = video["timestamp"],
                    title=video.get("title", None),
                    description=video.get("description", None)
                ))