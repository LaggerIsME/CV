from flask import Flask, render_template, url_for, request
from flask_cors import CORS
import jinja2
from datetime import datetime
#from db import session
#import models
#Создаю объект типа Flask, в котором основным файлом будет app.py
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/handle_data', methods=['POST'])
def handle_data():
    sender_name = request.form['sender_name']
    #sender_surname = request.form['']
    return render_template("index.html")
    # your code
    # return a response

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/register', methods=['POST'])
def response_register():
    return {"status": "success", "response": 200}
@app.route('/login')
def login():
    return render_template("login.html")
@app.route('/register', methods=['POST'])
def response_login():
    return {"status": "success", "response": 300}




#Запуск файла, как Flask-приложение
if __name__ == "__main__":
    app.run(debug=True)