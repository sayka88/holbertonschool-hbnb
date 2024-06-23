
# Copy application code
COPY . .

# Expose application port
EXPOSED 8000

# Define a volume for data persistence
VOLUME /app/data

# Configure Gunicorn as application server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
