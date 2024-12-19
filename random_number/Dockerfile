FROM python:3.11-slim

WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Set the environment variable for Flask app
ENV FLASK_APP=random_number:create_app

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=8001"]
