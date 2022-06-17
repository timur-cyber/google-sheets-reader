from typing import Dict

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy_utils import database_exists, create_database

from config import POSTGRESQL


def get_engine(user, passwd, host, port, db):
    """
    Функция для получения движка СУБД
    :param user: str
    :param passwd: str
    :param host: str
    :param port: int
    :param db: str
    :return: sqlalchemy.engine.base.Engine
    """
    url = f"postgresql://{user}:{passwd}@{host}:{port}/{db}"
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url, pool_size=50, echo=False)
    return engine


def get_engine_with_config(conf: Dict):
    """
    Функция для получения движка СУБД из конфига с настройками
    :param conf: dict
    :return: sqlalchemy.engine.base.Engine
    """
    try:
        return get_engine(
            conf['pguser'],
            conf['pgpasswd'],
            conf['pghost'],
            conf['pgport'],
            conf['pgdb']
        )
    except KeyError:
        return None


def get_session():
    """
    Функция для получения объекта сессии СУБД
    :return: sqlalchemy.orm.session.Session
    """
    engine = get_engine_with_config(POSTGRESQL)
    session = sessionmaker(bind=engine)()
    return session


engine = get_engine_with_config(POSTGRESQL)
Base = declarative_base(bind=engine)


class Records(Base):
    """
    Класс для создания таблицы записей в БД
    """
    __tablename__ = 'records'

    id = Column(Integer, primary_key=True)
    num = Column(Integer, nullable=False)
    order_num = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    price_rub = Column(Integer, nullable=False)
    date = Column(String, nullable=False)

    def __repr__(self):
        return f'Запись №{self.id} | Заказ №{self.order_num}.'
