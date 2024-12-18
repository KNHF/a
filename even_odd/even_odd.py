from flask import Flask, jsonify, render_template
from app.models import db, ExampleModel
from flask_migrate import Migrate
import requests
import config

app = Flask(__name__, template_folder='../app/templates',
            static_folder='../app/static')
app.config.from_object(config.DevelopmentConfig)

random_microservice_url = "http://random_number:8001/generate"


def call_random_microservie():
    response = requests.get(random_microservice_url)
    return response.json().get("random_number")


@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")


@app.route("/check", methods=['GET'])
def check_even_odd():
    random_number = call_random_microservie()
    result = "even" if random_number % 2 == 0 else "odd"
    return render_template("check_result.html", random_number=random_number, result=result)


if __name__ == "__main__":
    app.run(port=8002)
