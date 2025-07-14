# TikSnatch

**TikSnatch** is an automated tool to download and archive all public videos from a TikTok user. It periodically checks the specified profile and saves any new uploads — ideal for backups, research, or offline access.

## 🚀 Features

- 🔁 Automatically checks for new videos every `X` minutes
- 📥 Downloads all public videos from a given TikTok username
- 🗂️ Saves files by user and upload date
- 🔧 Easy configuration via command-line or config file
- 🧪 Perfect for archivists, researchers, or content watchers

## Usage

TikSnatch can be run using Python 3 or the pre-built docker image.

### Docker
ToDo

### Python
You can run TikSnatch directly using Python 3

#### Installation
```
git clone https://github.com/robinmeis/tiksnatch.git
cd tiksnatch
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Run
Make sure your virtual environment is activated before starting TikSnatch.
```
source venv/bin/activate
python tiksnatch.py --username some_tiktok_user
```

#### Commandline options
TikSnatch offers several command line options:
```bash
python3 tiksnatch.py --help
usage: tiksnatch.py [-h] --username USERNAME [--interval INTERVAL] [--download-dir DOWNLOAD_DIR] [--max-initial-downloads MAX_INITIAL_DOWNLOADS]

TikSnatch - TikTok video monitor

options:
  -h, --help            show this help message and exit
  --username USERNAME   TikTok username to monitor [env var: TIKSNATCH_USERNAME]
  --interval INTERVAL   Check interval in minutes [env var: TIKSNATCH_INTERVAL]
  --download-dir DOWNLOAD_DIR
                        Directory to save videos [env var: TIKSNATCH_DOWNLOAD_DIR]
  --max-initial-downloads MAX_INITIAL_DOWNLOADS
                        Limit on first run [env var: TIKSNATCH_MAX_INITIAL]

 In general, command-line values override environment variables which override defaults.
```