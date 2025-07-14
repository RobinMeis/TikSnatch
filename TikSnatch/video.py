from datetime import datetime

class Video:
    def __init__(self, url, timestamp, title, description):
        self.url = url
        self.timestamp = datetime.fromtimestamp(timestamp)
        self.title = title
        self.description = description

    def __str__(self):
        return (
            f"Video:\n"
            f"  Title      : {self.title or '-'}\n"
            f"  URL        : {self.url}\n"
            f"  Timestamp  : {self.timestamp.isoformat()}\n"
            f"  Description: {self.description or '-'}"
        )

    def __repr__(self):
        return f"Video(title={self.title!r}, url={self.url!r})"