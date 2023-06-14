#!/usr/bin/env python3


import uuid
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
import datetime
from sqlalchemy import orm

Base = declarative_base()

class BaseModel():


    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__ (self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at") is None:
                self.created_at = datetime.datetime.utcnow()

            if kwargs.get("updated_at") is None:
                self.updated_at = datetime.datetime.utcnow()

            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.utcnow()
            self.updated_at = self.created_at

    def save(self):
        from models import storage
        self.updated_at = datetime.datetime.now()
        storage.new(self)
        storage.save()

    def __repr__(self):
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__,
                                         self.id, self.__dict__)

    def to_dict(self):
        new_dict = self.__dict__.copy()
        del new_dict["_sa_instance_state"]
        if 'password' in new_dict:
            del new_dict["password"]

        return new_dict
