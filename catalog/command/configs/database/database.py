from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session

from catalog.settings import COMMAND_DATABASE_URL


metadata = MetaData()

engine = create_engine(COMMAND_DATABASE_URL)
Session = scoped_session(sessionmaker(bind=engine))


class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):
        self.__metadata = MetaData()
        self.__engine = create_engine(COMMAND_DATABASE_URL)
        self.__session = Session

    @property
    def metadata(self):
        return self.__metadata

    @property
    def session(self):
        return self.__session
