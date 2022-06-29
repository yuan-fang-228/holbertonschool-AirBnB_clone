#!/usr/bin/python3
"""File storage"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {"BaseModel": BaseModel, "User": User, "State": State, "City": City,
           "Amenity": Amenity, "Place": Place, "Review": Review}


class FileStorage():
    """a class that serializes and deserializes between JSON and instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets the object with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file"""
        my_obj = {}
        for key in self.__objects:
            my_obj[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as myfile:
            json.dump(my_obj, myfile)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as myfile:
                jsondict = json.load(myfile)
                for key in jsondict:
                    classname = jsondict[key]["__class__"]
                    self.__objects[key] = classes[classname](**jsondict[key])
        except FileNotFoundError:
            pass
