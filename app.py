from flask import Flask, render_template, url_for, request
from flask_cors import CORS
import jinja2
from datetime import datetime
#from db import session
#import models

#Создаю объект типа Flask, в котором основным файлом будет app.py
app = Flask(__name__)
CORS(app)

# Грузит основную страницу
@app.route('/')
def index():
    return render_template("index.html")

# Обрабатывает фидбэки от работадателей
@app.route('/handle_data', methods=['POST'])
def handle_data():
    job_name = request.form['job_name']
    job_email = request.form['job_email']
    job_subject = request.form['job_subject']
    job_message = request.form['job_message']
    return render_template("index.html")
    # your code
    # return a response




#Запуск файла, как Flask-приложение
if __name__ == "__main__":
    app.run(debug=True)