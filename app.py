from flask import Flask, render_template, url_for, request
from flask_cors import CORS
import jinja2

import db
from db import session
from models import FeedBack, Work, Type
#Создаю объект типа Flask, в котором основным файлом будет app.py
app = Flask(__name__)
CORS(app)
#создать все таблицы из Models
db.init()

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
    response = FeedBack.create(name = job_name, email = job_email, subject = job_subject, message = job_message)
    return render_template("index.html")
    # your code
    # return a response

# Flask 6 functions
# / - index.html
# POST /feedback - to send email
# /admin if not singed in, redirect to /admin/login, else to /admin/dashboard
# /admin/login
# /admin/dashboard
# /admin/works

# FASTAPI
# GET /api/works -> list of works
# POST /api/works -> to add work
# DELETE /api/work/:id -> to delete work
# PATCH /api/work/:id -> to edit


#Запуск файла, как Flask-приложение
if __name__ == "__main__":
    app.run(debug=True)