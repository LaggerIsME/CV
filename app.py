from flask import Flask, render_template, url_for, request
from flask_cors import CORS
import jinja2
from flask_login import login_required
from flask_security.datastore import SQLAlchemySessionUserDatastore
from flask_security import Security, utils
import db
from db import session
from models import FeedBack, User, Role
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

# Очистка сессии после каждого входа
session.clear()

# Создаю проект Flask, в котором основным файлом будет app.py
app = Flask(__name__)
CORS(app)

# Flask Security
app.config['SECRET_KEY'] = 'kapez-secure'
app.config['SECURITY_PASSWORD_HASH'] = 'pbkdf2_sha512'
app.config['SECURITY_PASSWORD_SALT'] = 'salt-secure'

# user_datastore = SQLAlchemySessionUserDatastore(session,User, Role), если SQLAlchemy
# user_datastore = SQLAlchemyUserDatastore(session, User, Role), если Flask-SQLAlchemy
user_datastore = SQLAlchemySessionUserDatastore(session, User, Role)
security = Security(app, user_datastore)

# Flask Admin
admin = Admin(app, name="Resume", template_mode="bootstrap4", )

# добавляем редакцию таблиц на админ панельку
admin.add_view(ModelView(FeedBack, session, name="FeedBack"))
admin.add_view(ModelView(User, session))
admin.add_view(ModelView(Role, session))


# Вход в админ панель
@app.before_first_request
def before_first_request():

    # Создание юзеров
    user_datastore.find_or_create_role(name='admin', description='Administrator')
    user_datastore.find_or_create_role(name='end-user', description='End user')

    # Создание двух юзеров, если они не существуют
    # In each case, use Flask-Security utility function to encrypt the password.
    encrypted_password = utils.hash_password('password')
    if not user_datastore.get_user('someone@example.com'):
        user_datastore.create_user(email='someone@example.com', password=encrypted_password)
    if not user_datastore.get_user('admin@example.com'):
        user_datastore.create_user(email='admin@example.com', password=encrypted_password)

    #сохранить изменения
    session.commit()

    user_datastore.add_role_to_user('someone@example.com', 'end-user')
    user_datastore.add_role_to_user('admin@example.com', 'admin')
    session.commit()

    # Чтоб перекидывало на login, а не сразу на admin-панель
    endpoint = 'admin.index'
    url = url_for(endpoint)
    admin_index = app.view_functions.pop(endpoint)
    @app.route(url, endpoint=endpoint)
    @login_required
    def secure_admin_index():
        return admin_index()


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
    response = FeedBack(name=job_name, email=job_email, subject=job_subject, message=job_message)
    session.add(response)
    session.commit()
    return render_template("index.html")


# Запуск файла, как Flask-приложение
if __name__ == "__main__":
    db.init()
    app.run(debug=True)
