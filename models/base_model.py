#!/usr/bin/python3
"""
Class BaseModel
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    Base class for the Airbnb project
    """
    def __init__(self, *args, **kwargs):
        """
        Initialises a BaseModel instance
        """
        dateformat = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, dateformat)
                elif key != "__class__":
                    self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """
        Returns the string of a BaseModel instance
        """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        Changes the updated_at time of an instance
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        """
        my_dict = {}
        my_dict["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if type(value) is datetime:
                my_dict[key] = value.isoformat()
            else:
                my_dict[key] = value
        return my_dict
