# 🎬 TikSnatch

**TikSnatch** is an automated tool to download and archive all public videos from a TikTok user. It periodically checks the specified profile and saves any new uploads — ideal for backups, research, or offline access.

## 🚀 Features

- 🔁 Automatically checks for new videos every `X` minutes
- 📥 Downloads all public videos from a given TikTok username
- 🗂️ Saves files by user and upload date
- 🔧 Easy configuration via command-line or config file
- 🧪 Perfect for archivists, researchers, or content watchers

## ⚙️ Usage

TikSnatch can be run using Python 3 or the pre-built docker image.

### 🐳 Docker

TikSnatch is also available as a Docker image, which is ideal for running it in a containerized environment.

#### 🧪 Basic example

```bash
docker run --rm \
  -v "$(pwd)/downloads:/app/downloads" \
  -e TIKSNATCH_USERNAME=some_tiktok_user \
  robinmeis/tiksnatch:latest
```

This command:
- Mounts the local `./downloads` folder into the container
- Sets the username via environment variable
- Pulls and runs the latest Docker image

> Replace `"$(pwd)/downloads"` with the desired absolute path on your system.

#### ⚙️ Supported Environment Variables

| Variable                     | Description                                 | Default         |
|------------------------------|---------------------------------------------|-----------------|
| `TIKSNATCH_USERNAME`         | TikTok username to monitor                  | *(required)*    |
| `TIKSNATCH_INTERVAL`         | Check interval in minutes                   | `5`             |
| `TIKSNATCH_DOWNLOAD_DIR`     | Path inside the container to save videos    | `/app/downloads`|
| `TIKSNATCH_MAX_INITIAL`      | Max number of videos to fetch on first run  | `10`            |

#### 🧩 Example with all variables

```bash
docker run --rm \
  -v "$(pwd)/downloads:/app/downloads" \
  -e TIKSNATCH_USERNAME=someuser \
  -e TIKSNATCH_INTERVAL=10 \
  -e TIKSNATCH_DOWNLOAD_DIR=/app/downloads \
  -e TIKSNATCH_MAX_INITIAL=20 \
  robinmeis/tiksnatch:latest
```

You can also run it with `--detach` (`-d`) to keep it running in the background:

```bash
docker run -d --name tiksnatch \
  -v "$(pwd)/downloads:/app/downloads" \
  -e TIKSNATCH_USERNAME=someuser \
  robinmeis/tiksnatch:latest
```

### 🐍 Python

You can run TikSnatch directly using Python 3.

#### 🧪 Installation

```bash
git clone https://github.com/robinmeis/tiksnatch.git
cd tiksnatch
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### ▶️ Run

Make sure your virtual environment is activated before starting TikSnatch.

```bash
source venv/bin/activate
python tiksnatch.py --username some_tiktok_user
```

#### 📖 Command-line options

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

## 🌐 Proxy Support

TikSnatch (via `yt-dlp`) supports routing all HTTPS traffic through a proxy using the standard `HTTPS_PROXY` environment variable.

This allows you to run TikSnatch behind a firewall, VPN, or through a SOCKS proxy (e.g. Tor).

### ✅ Supported proxy formats

| Scheme         | Description                           |
|----------------|---------------------------------------|
| `http://`      | Standard HTTP proxy                   |
| `socks5://`    | SOCKS5 proxy                          |
| `socks5h://`   | SOCKS5 with remote DNS (e.g. Tor)     |
| `socks4://`    | SOCKS4 proxy                          |

### 🧪 Example (Linux/macOS)

```bash
export HTTPS_PROXY=socks5h://127.0.0.1:9050
python tiksnatch.py --username someuser
```

### 🐳 Example with Docker

```bash
docker run --rm \
  -v "$(pwd)/downloads:/app/downloads" \
  -e TIKSNATCH_USERNAME=someuser \
  -e HTTPS_PROXY=socks5h://127.0.0.1:9050 \
  robinmeis/tiksnatch:latest
```

> TikSnatch does not manage proxy configuration itself — it simply respects the `HTTPS_PROXY` environment variable.
