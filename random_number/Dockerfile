FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY config.py .
COPY random_number/random_number.py .
CMD ["python", "random_number.py"]
