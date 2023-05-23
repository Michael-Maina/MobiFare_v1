#!/usr/bin/env python3

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.users import User


classes = {'User': User}

class DBstorage:

    __session = None
    __engine = None

    def __init__(self):
        username = getenv('username')
        password = getenv('password')
        host = getenv('host')
        db = getenv('db')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(username, password, host, db), pool_pre_ping=True)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                print(objs)
                print()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj):
        self.__session.delete(obj)
        self.save()

    def reload(self):
        Base.metadata.create_all(self.__engine)
        self.__session = sesh()
