from sqlalchemy import Column, Integer, Text, String, LargeBinary, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
# Более удобная отправка запросов
from db import base, session
from flask_security import UserMixin, RoleMixin


class BaseModel(base):
    __abstract__ = True


# Таблица с запросами найма на работу
class FeedBack(BaseModel):
    __tablename__ = "feedbacks"
    # Индивидуальный идентификатор ответа, является основным ключем
    id = Column(Integer, primary_key=True)
    # Информация о отправителе
    name = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    subject = Column(String(200), nullable=False)
    # Используется Text, так как может быть много информации
    message = Column(Text, nullable=False)


# Таблица с информацией о моих работах


# Flask Secuirity
# Таблица, чтоб были мэни-ту-мэни отношения между User и Role
class RolesUsers(BaseModel):
    __tablename__ = 'roles_users'
    id = Column(Integer(), primary_key=True)
    user_id = Column('user_id', Integer(), ForeignKey('user.id'))
    role_id = Column('role_id', Integer(), ForeignKey('role.id'))


class Role(BaseModel, RoleMixin):
    __tablename__ = 'role'
    id = Column(Integer(), primary_key=True)
    name = Column(String(80), unique=True)
    description = Column(String(255))


class User(BaseModel, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    username = Column(String(255))
    password = Column(String(255))
    last_login_at = Column(DateTime())
    current_login_at = Column(DateTime())
    last_login_ip = Column(String(100))
    current_login_ip = Column(String(100))
    login_count = Column(Integer)
    active = Column(Boolean())
    confirmed_at = Column(DateTime())
    roles = relationship('Role', secondary='roles_users',
                         backref=backref('users', lazy='dynamic'))


