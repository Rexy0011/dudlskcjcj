FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy

WORKDIR /app

# Upgrade pip
RUN pip install --upgrade pip

# Install system Chromium binary and dependencies for nodriver
RUN apt-get update && apt-get install -y \
    chromium-browser \
    || apt-get install -y chromium \
    && rm -rf /var/lib/apt-lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy remaining source code
COPY . .

# Set start command
CMD ["python", "gen.py"]
