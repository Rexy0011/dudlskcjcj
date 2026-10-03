# Use official Playwright base image
FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy

WORKDIR /app

# Upgrade pip first
RUN pip install --upgrade pip

# Copy dependencies and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Ensure matching Chromium binary is downloaded inside the image
RUN playwright install chromium
RUN playwright install-deps chromium

# Copy application source code
COPY . .

# Execution command
CMD ["python", "gen.py"]
