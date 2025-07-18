#!/usr/bin/env python3
"""
TikTok Channel Monitor
This script monitors a TikTok channel for new videos, downloads them, and logs details.
"""

import os
import csv
import time
import hashlib
import datetime
import signal
import configargparse
from yt_dlp import YoutubeDL

shutdown_requested = False

def handle_shutdown_signal(signum, frame):
    global shutdown_requested
    print(f"\nReceived signal {signum}. Shutting down...")
    shutdown_requested = True

def get_config():
    parser = configargparse.ArgParser(
        description="TikSnatch - TikTok video monitor",
        default_config_files=[]
    )

    parser.add('--username', env_var='TIKSNATCH_USERNAME', required=True, help='TikTok username to monitor')
    parser.add('--interval', env_var='TIKSNATCH_INTERVAL', type=int, default=5, help='Check interval in minutes')
    parser.add('--download-dir', env_var='TIKSNATCH_DOWNLOAD_DIR', default='downloads', help='Directory to save videos')
    parser.add('--max-initial-downloads', env_var='TIKSNATCH_MAX_INITIAL', type=int, default=10, help='Limit on first run')

    return parser.parse_args()

args = get_config()
CHANNEL_USERNAME = args.username
CHECK_INTERVAL = args.interval*60
DOWNLOAD_DIR = args.download_dir
MAX_INITIAL_DOWNLOADS = args.max_initial_downloads
LOG_FILE = os.path.join(DOWNLOAD_DIR, "videos.csv")

# Ensure download directory exists
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def wait():
    print(f"Sleeping for {CHECK_INTERVAL} seconds until next check at {(datetime.datetime.now() + datetime.timedelta(seconds=CHECK_INTERVAL)).strftime('%Y-%m-%d %H:%M:%S')}")
    sleep_interval = 5  # seconds
    slept = 0
    while slept < CHECK_INTERVAL and not shutdown_requested:
        time.sleep(sleep_interval)
        slept += sleep_interval

def calculate_sha256(file_path):
    """Calculate SHA256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def get_downloaded_video_ids():
    """Get list of already downloaded video IDs from log file."""
    if not os.path.exists(LOG_FILE):
        return set()
    
    video_ids = set()
    with open(LOG_FILE, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        # Skip header if file exists and has content
        if os.path.getsize(LOG_FILE) > 0:
            next(reader, None)  # Skip header
        for row in reader:
            if len(row) > 2:  # Ensure row has enough elements
                video_ids.add(row[2])  # video_id is at index 2
    return video_ids

def log_video(video_data, file_path):
    """Log video details to CSV file. Properly escapes all fields including caption."""
    file_exists = os.path.exists(LOG_FILE) and os.path.getsize(LOG_FILE) > 0
    
    timestamp_video = video_data.get('timestamp', datetime.datetime.now().isoformat())
    timestamp_download = datetime.datetime.now().isoformat()
    video_id = video_data.get('id', '')
    caption = video_data.get('title', '')
    filename = os.path.basename(file_path)
    file_hash = calculate_sha256(file_path)
    
    with open(LOG_FILE, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)  # Quote all fields for maximum safety
        # Write header if file doesn't exist
        if not file_exists:
            writer.writerow(['timestamp_video', 'timestamp_download', 'channel_name', 'video_id', 
                             'caption', 'filename', 'sha256_hash'])
        writer.writerow([timestamp_video, timestamp_download, CHANNEL_USERNAME, video_id, 
                         caption, filename, file_hash])

def get_tiktok_videos(username, limit=None):
    """Get TikTok videos using yt-dlp."""
    url = f"https://www.tiktok.com/@{username}"
    
    # Configure yt-dlp
    ydl_opts = {
        'extract_flat': True,
        'quiet': True,
        'no_warnings': True,
        'skip_download': True
    }
    
    with YoutubeDL(ydl_opts) as ydl:
        # Get video information
        info = ydl.extract_info(url, download=False)
        if 'entries' in info:
            videos = info['entries']
            # Sort by upload date if available
            if videos and 'upload_date' in videos[0]:
                videos.sort(key=lambda x: x.get('upload_date', ''), reverse=True)
            
            if limit:
                return videos[:limit]
            return videos
        return []

def download_video(video_info):
    """Download a TikTok video using yt-dlp."""
    video_id = video_info.get('id', '')
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"{timestamp}_{video_id}.mp4"
    file_path = os.path.join(DOWNLOAD_DIR, file_name)
    
    # Configure yt-dlp for download
    ydl_opts = {
        'quiet': False,
        'no_warnings': True,
        'outtmpl': file_path,
        'format': 'best'
    }
    
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_info['url']])
        
        # Create a metadata dict for logging
        video_data = {
            'id': video_id,
            'timestamp': datetime.datetime.fromtimestamp(
                int(video_info.get('timestamp', time.time()))
            ).isoformat() if 'timestamp' in video_info else datetime.datetime.now().isoformat(),
            'title': video_info.get('title', '')
        }
        
        print(f"Downloaded video: {file_name}")
        return file_path, video_data
    except Exception as e:
        print(f"Error downloading video {video_id}: {e}")
        return None, None

def main():
    # Keep track of downloaded videos
    downloaded_ids = get_downloaded_video_ids()
    print(f"Found {len(downloaded_ids)} previously downloaded videos in log file")
    
    # First run flag
    first_run = True
    
    while not shutdown_requested:
        try:
            print(f"Checking for new videos from @{CHANNEL_USERNAME} at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            
            # Get videos
            if first_run:
                videos = get_tiktok_videos(CHANNEL_USERNAME, MAX_INITIAL_DOWNLOADS)
                first_run = False
            else:
                videos = get_tiktok_videos(CHANNEL_USERNAME)
            
            if not videos:
                print("No videos found or error fetching videos")
                wait()
                continue
            
            # Check for new videos
            new_videos = 0
            for video in videos:
                video_id = video.get('id', '')
                
                if video_id and video_id not in downloaded_ids:
                    print(f"New video found: {video_id}")
                    file_path, video_data = download_video(video)
                    
                    if file_path and video_data:
                        log_video(video_data, file_path)
                        downloaded_ids.add(video_id)
                        new_videos += 1
            
            if new_videos > 0:
                print(f"Downloaded {new_videos} new videos")
            else:
                print(f"No new videos found")
            
            # Wait for next check
            wait()
        
        except Exception as e:
            print(f"Error: {e}")
            wait()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, handle_shutdown_signal)
    signal.signal(signal.SIGTERM, handle_shutdown_signal)
    main()
