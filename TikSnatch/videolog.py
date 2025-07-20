import os
import csv

class VideoLog:
    def __init__(self, logfile="videos.csv"):
        self.logfile = logfile
        self.video_ids = set()

    def read(self):
        """Get list of already downloaded video IDs from log file."""
        self.video_ids = set()

        if not os.path.exists(self.logfile):
            return
        
        with open(self.logfile, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            # Skip header if file exists and has content
            if os.path.getsize(self.logfile) > 0:
                next(reader, None)  # Skip header
            for row in reader:
                if len(row) > 3:  # Ensure row has enough elements
                    self.video_ids.add(row[3])  # video_id is at index 2

    def logVideo(self, video):
        """Log video details to CSV file. Properly escapes all fields including caption."""
        file_exists = os.path.exists(self.logfile) and os.path.getsize(self.logfile) > 0
        
        with open(self.logfile, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)  # Quote all fields for maximum safety
            # Write header if file doesn't exist
            if not file_exists:
                writer.writerow(['timestamp_video', 'timestamp_download', 'channel_name', 'video_id', 
                                'description', 'filename', 'url', 'sha256_hash'])
            writer.writerow([video.timestamp, video.timestamp_download, video.channel.username, video.id, 
                            video.description, video.filepath, video.url, video.sha256_hash])
            
    def checkVideo(self, video):
        """Checks if a video has alread been downloaded"""
        return video.id in self.video_ids