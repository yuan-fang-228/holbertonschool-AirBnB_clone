#!/usr/bin/python3

from datetime import datetime
from uuid import uuid4


class BaseModel():
    """
        Base class for the Airbnb project
    """
    def __init__(self):
        """
            initialises a BaseModel instance
        """
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
