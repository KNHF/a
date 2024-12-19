# api_gateway/Dockerfile
FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=api_gateway.api_gateway:create_app

CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
