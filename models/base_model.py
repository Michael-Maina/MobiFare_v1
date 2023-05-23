#!/usr/bin/env python3


import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class BaseModel():

    id = Column(String(60), default=uuid.uuid4, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__ (self):
        self.id = uuid.uuid4()
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()


    def save(self):
        from models import storage
        self.updated_at = datetime.datetime.now()
        storage.new(self)
        storage.save()

    def __repr__(self):
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__,
                                         self.id, self.__dict__)
