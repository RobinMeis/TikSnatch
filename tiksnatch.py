import configargparse
import time
import datetime
import signal
import os

from TikSnatch.channel import Channel
from TikSnatch.videolog import VideoLog

shutdown_requested = False

def handle_shutdown_signal(signum, frame):
    global shutdown_requested
    print(f"\nReceived signal {signum}. Shutting down...")
    shutdown_requested = True

def get_config():
    parser = configargparse.ArgParser(
        description="TikSnatch - TikTok video monitor & downloader",
        default_config_files=[]
    )

    parser.add('--username', env_var='TIKSNATCH_USERNAME', required=True, help='TikTok username to monitor')
    parser.add('--interval', env_var='TIKSNATCH_INTERVAL', type=int, default=5, help='Check interval in minutes')
    parser.add('--download-dir', env_var='TIKSNATCH_DOWNLOAD_DIR', default='downloads', help='Directory to save videos')
    parser.add('--run-once', action='store_true', help='Downlaod once and exit. Disables permanent monitoring')
    parser.add('--since', env_var='SINCE', type=str, help='Only download videos published on or after this date (YYYY-MM-DD)')

    return parser.parse_args()

def wait(delay):
    print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Sleeping for {delay} minutes until next check at {(datetime.datetime.now() + datetime.timedelta(minutes=delay)).strftime('%Y-%m-%d %H:%M:%S')}")
    delay *= 60
    sleep_interval = 5  # seconds
    slept = 0
    while slept < delay and not shutdown_requested:
        time.sleep(sleep_interval)
        slept += sleep_interval

config = get_config()

download_dir = config.download_dir
logfile = os.path.join(download_dir, "videos.csv")

since_date = None
if config.since:
    try:
        since_date = datetime.datetime.strptime(config.since, "%Y-%m-%d")
    except ValueError:
        print(f"Invalid date format for --since: {config.since}. Use YYYY-MM-DD.")
        exit(1)

videolog = VideoLog(logfile)
channel = Channel(config.username)

signal.signal(signal.SIGINT, handle_shutdown_signal)
signal.signal(signal.SIGTERM, handle_shutdown_signal)

while not shutdown_requested:
    videolog.read()
    print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Checking channel for videos...")
    channel.get()

    for video in channel.videos:
        if since_date and video.timestamp < since_date: # Skip videos that have been uploaded before since_date
            continue

        if videolog.checkVideo(video): # Skip if video has already been downloaded
            continue

        # Download the video
        print(video)
        video.download(download_dir)

        # Log video to logfile
        videolog.logVideo(video)

    if config.run_once: # Exit if run once is enabled
        break

    wait(config.interval)