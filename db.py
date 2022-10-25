import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# Подключение к базе данных
# Пример: dialect+driver://username:password@host:port/database
engine = create_engine("postgresql://postgres:12345678@localhost:5432/cv", pool_size=10, max_overflow=20)


# Сессия для обращения к базе данных в каждом потоке (scoped_session)
session = scoped_session(sessionmaker(bind=engine))
base = declarative_base()
base.query = session.query_property()

# Инициализировать все модели
def init():

    import models

    # Создать все таблицы
    base.metadata.create_all(bind=engine)