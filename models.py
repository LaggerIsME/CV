import json

from sqlalchemy import Column, Integer, Text, String, LargeBinary, Boolean, Table, ForeignKey
from sqlalchemy.orm import relationship, backref
# Более удобная отправка запросов
from sqlalchemy_mixins import AllFeaturesMixin
from db import base, session
from flask_security import UserMixin, RoleMixin


class BaseModel(base, AllFeaturesMixin):
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
class Work(BaseModel):
    __tablename__ = "works"
    id = Column(Integer, primary_key=True)
    img = Column(LargeBinary, nullable=False)  # LargeBinary
    project = Column(String(200), nullable=False)
    type = Column(String(200), nullable=False)


# Flask Secuirity
"""
roles_users = Table('roles_users', Column('user_id', Integer, ForeignKey('user.id')), Column('role_id', Integer, ForeignKey('role.id')))


class User(BaseModel, UserMixin):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    password = Column(String(200), nullable=False)
    active = Column(Boolean)
    roles = relationship('Role', secondary=roles_users,
                         backref=backref('users'), lazy='dynamic')


class Role(BaseModel, RoleMixin):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False, unique=True)
"""

# Условие, чтоб все работало правильно из документации Allfeaturesmixin
BaseModel.set_session(session)
