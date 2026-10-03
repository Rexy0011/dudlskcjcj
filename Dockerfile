FROM python:3.10-slim

# Install system dependencies and Chromium
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    libglib2.0-0 \
    libnss3 \
    libgconf-2-4 \
    libfontconfig1 \
    && rm -rf /var/lib/apt-lists/*

# Set working directory
WORKDIR /app

# Copy application files
COPY . .

# Install Python requirements
RUN pip install --no-cache-dir -r requirements.txt

# Set Chromium path environment variable (optional but helpful)
ENV CHROME_BIN=/usr/bin/chromium

CMD ["python", "main.py"]
