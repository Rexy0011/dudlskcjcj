FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    libglib2.0-0 \
    libnss3 \
    libgconf-2-4 \
    libfontconfig1 \
    && rm -rf /var/lib/apt-lists/*

WORKDIR /app
COPY . .

# Install Python requirements
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright's browser binary inside the image
RUN playwright install chromium

# Set default binary environment variable
ENV CHROME_BIN=/usr/bin/chromium

# Start Command
CMD ["python", "gen.py"]
