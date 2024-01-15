#!/usr/bin/python3
""" Define a class BaseModel that defines  all common attributes
    /methods for other classes
"""
import uuid
from datetime import datetime


class BaseModel():
    """ Class attributes """
    def __init__(self, *args, **kwargs):
        """ Instantiates a new model """
        from models import storage
        if kwargs:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ Returns a string representation of an instance """
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return ('[{}] ({}) {}'.format(cls, self.id, self.__dict__))

    def save(self):
        """ Updates the attribute updated_at when the instance has changed """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Converts instance into dictionary format """
        dic = {}
        dic.update(self.__dict__)
        data = {'__class__': (str(type(self)).split('.')[-1]).split('\'')[0]}
        dic.update(data)
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return (dic)
