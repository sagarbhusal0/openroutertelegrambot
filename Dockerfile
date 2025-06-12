# Use the official Python base image
FROM python:3.11-slim

# Set a working directory
WORKDIR /app

# Install pip dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all app files
COPY . .

# Expose the app port
EXPOSE 8626

# Set environment variables if needed (example)
# ENV SOME_ENV=some_value

# Start the app (replace main.py and app:app with your entrypoint if different)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8626"]