# Use the official Alpine Linux image with Python 3.9
FROM python:3.9-alpine
# Set environment variables
ENV PYTHONUNBUFFERED=1 \
 APP_HOME=/app
# Create the working directory
WORKDIR $APP_HOME
# Install dependencies
RUN apk update && apk add --no-cache \
 build-base\
 libffi-dev \
 openssl-dev\
 python3-dev\
 postgresql-dev \
 && pip install --upgrade pip
# Copy requirements.txt
COPY requirements.txt.
# Install Python dependencies
RUN pip install -r requirements.txt
# Copy application code
COPY . .
# Expose application port
EXPOSED 8000
# Define a volume for data persistence
VOLUME /app/data
# Configure Gunicorn as application server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
