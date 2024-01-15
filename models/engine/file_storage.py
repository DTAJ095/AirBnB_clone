#!/usr/bin/python3
""" Define a class FileStorage that serializes instances to
    a JSON file and deserializes JSON file to instances
"""
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place


class FileStorage():
    """ This class manages the storage of hbnb models in JSON format """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ Returns the dictionary of current models in the storage """
        return (FileStorage.__objects)

    def new(self, obj):
        """ Adds new objects to the storage """
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """ Saves storage dict to file """
        with open(FileStorage.__file_path, 'w') as f:
            tmp = {}
            tmp.update(FileStorage.__objects)
            for key, value in tmp.items():
                tmp[key] = value.to_dict()
            json.dump(tmp, f)

    def reload(self):
        """ Reloads storage dict from file """
        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity, 'Review': Review
        }
        try:
            tmp = {}
            with open(FileStorage.__file_path, 'r') as f:
                tmp = json.load(f)
                for key, value in tmp.items():
                    self.all()[key] = classes[value['__class__']](**value)
        except FileNotFoundError:
            pass
