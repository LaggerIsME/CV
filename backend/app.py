from flask import Flask, render_template
import jinja2

#Создаю объект типа Flask, в котором основным файлом будет app.py
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


#Запуск файла, как Flask-приложение
if __name__ == "__main__":
    app.run(debug=True)