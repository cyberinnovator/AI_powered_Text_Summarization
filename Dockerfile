# Use lightweight Python 3.10 slim base (Debian-based)
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Install required system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    libxml2-dev \
    libxslt1-dev \
    libffi-dev \
    libssl-dev \
    python3-dev \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements.txt to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app into the container
COPY . .

# Expose the port Flask/Gunicorn will run on
EXPOSE 5000

# Run the app using Gunicorn (production-ready)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
