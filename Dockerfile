# Use full Python 3.10 image (Debian-based)
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy only requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all app files
COPY . .

# Expose Flask port
EXPOSE 5000

# Run using Flask development server (simple version)
# CMD ["python", "app.py"]

# 🚀 Recommended: Run with Gunicorn (production-grade WSGI server)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
