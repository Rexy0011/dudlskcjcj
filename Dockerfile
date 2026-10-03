# Use Playwright's official Docker image (includes Python 3.10 and Chromium with all system dependencies)
FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy

WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Run application
CMD ["python", "gen.py"]
