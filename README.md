# 🎬 TikSnatch

**TikSnatch** is an automated tool based on yt-dlp to download and archive all public videos from a TikTok user. It periodically checks the specified profile and saves any new uploads — ideal for backups, archiving, or offline access.

## 🚀 Features

- 🔁 Automatically checks for new videos every `X` minutes
- 📥 Downloads all public videos from a given TikTok username
- 🔧 Easy configuration via command-line or environment variables

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

| Variable                     | Description                                   | Default         |
|------------------------------|-----------------------------------------------|-----------------|
| `TIKSNATCH_USERNAME`         | TikTok username to monitor                    | *(required)*    |
| `TIKSNATCH_INTERVAL`         | Check interval in minutes                     | `5`             |
| `TIKSNATCH_DOWNLOAD_DIR`     | Path inside the container to save videos      | `/app/downloads`|
| `SINCE `                     | Only download videos since date (YYYY-MM-DD)  | `None`          |


```bash
docker run -d --name tiksnatch \
  -v "$(pwd)/downloads:/app/downloads" \
  -e TIKSNATCH_USERNAME=someuser \
  robinmeis/tiksnatch:latest
```

#### ❤️‍🔥 Liveness Probe Support

TikSnatch includes built-in support for container liveness checks. It automatically updates an internal timestamp file during normal operation. This allows orchestration systems like Kubernetes to verify that the process is still healthy (see example below).

A shell script named `liveness_check.sh` is included in the Docker image and can be used to perform the actual check. It exits with status `0` if the process is considered healthy, or `1` if overdue or stuck.

```yaml
livenessProbe:
  exec:
    command:
      - /bin/sh
      - -c
      - /app/liveness_check.sh
  initialDelaySeconds: 60
  periodSeconds: 60
  failureThreshold: 3
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
usage: tiksnatch.py [-h] --username USERNAME [--interval INTERVAL] [--download-dir DOWNLOAD_DIR] [--run-once] [--since SINCE]

TikSnatch - TikTok video monitor & downloader

options:
  -h, --help            show this help message and exit
  --username USERNAME   TikTok username to monitor [env var: TIKSNATCH_USERNAME]
  --interval INTERVAL   Check interval in minutes [env var: TIKSNATCH_INTERVAL]
  --download-dir DOWNLOAD_DIR
                        Directory to save videos [env var: TIKSNATCH_DOWNLOAD_DIR]
  --run-once            Downlaod once and exit. Disables permanent monitoring
  --since SINCE         Only download videos published on or after this date (YYYY-MM-DD) [env var: SINCE]

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
