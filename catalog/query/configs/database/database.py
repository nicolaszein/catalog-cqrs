from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session

from catalog.settings import QUERY_DATABASE_URL


class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):
        self.__metadata = MetaData()
        self.__engine = create_engine(QUERY_DATABASE_URL)
        self.__session = scoped_session(sessionmaker(bind=self.__engine))

    @property
    def metadata(self):
        return self.__metadata

    @property
    def session(self):
        return self.__session
