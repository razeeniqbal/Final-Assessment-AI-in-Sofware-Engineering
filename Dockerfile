# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy all files from the current directory to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your Flask app runs on
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
