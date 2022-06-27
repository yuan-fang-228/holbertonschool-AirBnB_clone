#!/usr/bin/python3

from datetime import datetime
from uuid import uuid4


class BaseModel():
    """
        Base class for the Airbnb project
    """
    def __init__(self, *args, **kwargs):
        """
            initialises a BaseModel instance
        """
        dateformat = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, dateformat)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
            returns the string of a BaseModel instance
        """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
            changes the updated_at time of an instance
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
            returns a dict repr of an instance
        """
        my_dict = {}
        my_dict["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if type(value) is datetime:
                my_dict[key] = value.isoformat()
            else:
                my_dict[key] = value
        return my_dict
