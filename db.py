import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# Подключение к базе данных
engine: sqlalchemy.engine.base.Engine = create_engine("postgresql://postgres:5432/site")
# Сессия для обращения к базе данных в каждом потоке (scoped_session)
session: sqlalchemy.orm.scoped_session = scoped_session(sessionmaker(bind=engine))
base = declarative_base()