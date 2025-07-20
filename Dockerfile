FROM python:3.11-slim

# Metadata
LABEL org.opencontainers.image.source="https://github.com/robinmeis/tiksnatch"
LABEL org.opencontainers.image.licenses="MIT"

# Default volume
VOLUME /app/downloads

# Create app directory
WORKDIR /app
COPY requirements.txt tiksnatch.py ./

# Install Python requirements
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Set the entry point
ENTRYPOINT ["python", "-u", "tiksnatch.py"]
