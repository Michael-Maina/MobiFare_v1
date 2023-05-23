#!/usr/bin/env python3


import uuid
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import orm

Base = declarative_base()

class BaseModel:

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        else:
            if not 'id' in kwargs.keys():
                self.id = str(uuid.uuid4())
            if 'created_at' in kwargs.keys() and 'updated_at' in kwargs.keys():
                kwargs['updated_at'] = datetime.strptime(
                    kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
                kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            else:
                kwargs['created_at'] = datetime.now()
                kwargs['created_at'] = datetime.now()
            if '__class__' in kwargs.keys():
                del kwargs['__class__']
            self.__dict__.update(kwargs)


    def save(self):
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()
