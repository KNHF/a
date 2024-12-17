import os
from flask import Blueprint, render_template, jsonify
from flask import Flask
main = Blueprint('main', __name__)

# این تابع یک روت تعریف می‌کند که در زمان درخواست گت به آدرس ریشه اجرا می‌شود

app = Flask(__name__, template_folder='templates')


@main.route("/", methods=['GET'])
def home():
    print("Current working directory:", os.getcwd())
    print("Template folder:", app.template_folder)
    # نمایش یک فایل HTML
    return render_template('index.html')

# این تابع یک روت تعریف می‌کند که در زمان درخواست گت به آدرس هلو اجرا می‌شود


@main.route("/hello", methods=['GET'])
def hello_microservice():
    # یک پیام به صورت جیسون برمی‌گرداند
    message = {"message": "Hello from the microservice! This is GeeksForGeeks"}
    return jsonify(message)
