import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# Подключение к базе данных
# Пример: dialect+driver://username:password@host:port/database
engine: sqlalchemy.engine.base.Engine = create_engine("postgresql://postgres:12345678@localhost:5432/cv")
# Сессия для обращения к базе данных в каждом потоке (scoped_session), autocommit = True ОБЯЗАТЕЛЬНО
# поскольку библиотека без этого не будет сохранять изменения
session: sqlalchemy.orm.scoped_session = scoped_session(sessionmaker(bind=engine, autocommit=True))
base = declarative_base()

# Инициализировать все модели
def init():

    import models

    # Создать все таблицы
    base.metadata.create_all(bind=engine)