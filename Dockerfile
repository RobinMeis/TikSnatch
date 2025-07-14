FROM python:3.11-slim

# Create app directory
WORKDIR /app

# Install Python requirements
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy your app
COPY . .

# Set the entry point
ENTRYPOINT ["python", "-u", "tiksnatch.py"]
