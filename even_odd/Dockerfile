FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY config.py .
COPY even_odd/even_odd.py .
CMD ["python", "even_odd.py"]
