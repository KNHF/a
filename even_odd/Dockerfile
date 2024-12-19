# Use the official Python image from the Docker Hub
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install MySQLdb dependencies
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential

RUN pip install mysqlclient

# Copy the application code into the container
COPY . .

# Set the environment variable for Flask
ENV FLASK_APP=even_odd.even_odd:create_app

# Expose the port the app runs on
EXPOSE 8002

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=8002"]
