from flask import Blueprint, render_template, jsonify, request
from .models import db, ExampleModel

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/generate', methods=['GET'])
def generate_random_number():
    import random
    random_number = random.randint(1, 1000)
    return jsonify({"random_number": random_number})


@main.route('/api', methods=['GET'])
def api_usage():
    api_key = request.args.get('api_key')
    if api_key:
        return jsonify({"api_key": api_key})
    return jsonify({"error": "API key is missing"}), 400
