import json

from sqlalchemy import Column, Integer, Text, String, LargeBinary, ForeignKey
from sqlalchemy_mixins import AllFeaturesMixin

from db import base, session


class BaseModel(base, AllFeaturesMixin):
    __abstract__ = True

class FeedBack(BaseModel):
    #Индивидуальный идентификатор ответа, является основным ключем
    feedback_id = Column(Integer, primary_key=True)
    #Информация о отправителе
    name = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    subject = Column(String(200), nullable=False)
    #Используется Text, так как может быть много информации
    message = Column(Text, nullable=False)

class Work(BaseModel):
    id = Column(Integer, primary_key=True)
    img = Column(LargeBinary, nullable=False)  # LargeBinary
    project = Column(String(200), nullable=False)
    type = Column(String(200), nullable=False)
    type_id = Column(Integer, ForeignKey("types.id"))

class Type(BaseModel):
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)

# Model Work(BaseModel):
# Model User(BaseModel):
    #username
    #password

BaseModel.set_session(session)
