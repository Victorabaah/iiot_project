# Lightweight Python base image
FROM python:3.11-slim

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Ensure logs appear immediately
ENV PYTHONUNBUFFERED=1

# Set working directory inside container
WORKDIR /app

# Copy dependency file first for better layer caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# App listens on port 8080
EXPOSE 8080

# Run with Gunicorn for a more production-like setup
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]