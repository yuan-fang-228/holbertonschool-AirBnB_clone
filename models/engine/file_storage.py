#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage():
    """
        a class that serializes and deserializes between JSON and instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
            sets the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + "." + obj.id
        self. __objects[key] = obj

    def save(self):
        """
            serialize __objects to the JSON file
        """
        my_obj = {}
        for key in self.__objects:
            my_obj[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as myfile:
            json.dump(my_obj, myfile)

    def reload(self):
        """
            deserializes the JSON file to __objects
        """
        classes = {"BaseModel": BaseModel}
        try:
            with open(self.__file_path) as myfile:
                jsondict = json.load(myfile)
                for key in jsondict:
                    classname = jsondict[key]["__class__"]
                    self.__objects[key] = classes[classname](**jsondict[key])
        except FileNotFoundError:
            pass
