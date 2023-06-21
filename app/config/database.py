import os
from typing import Any
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm.session import sessionmaker

class Database(DeclarativeBase):
    __BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    __DB_NAME = "X9.100-187-2008.db"
    __DB_URL = f"sqlite:///{os.path.join(__BASE_DIR, __DB_NAME)}"

    def engine(self):
        return create_engine(url=self.__DB_URL, echo=True)
    def session(self):
        return sessionmaker(bind=self.engine())()
	