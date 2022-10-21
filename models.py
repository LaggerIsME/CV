import json

from sqlalchemy import Column, Integer, Text, String
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




BaseModel.set_session(session)
