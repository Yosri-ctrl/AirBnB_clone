#!/usr/bin/python3
"""
Base module is the base class for all other classes
"""
from datetime import datetime
import uuid


class BaseModel():
    """
    BaseModule
    id: string - assign with an uuid when an instance is created
    created_at: datetime - assign with the current datetime when an instance is created
    updated_at: datetime - assign with the current datetime when an instance is created
    and it will be updated every time you change your object
    """
    id = str(uuid.uuid4())
    created_at = str(datetime.now())
    updated_at = str(datetime.now())

    def __str__(self):
        return "{} ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        BaseModel.updated_at = str(datetime.now())

    def to_dict(self):
        return {"__class__": type(self).__name__, "id": self.id, "created_at": self.created_at, "updated_at": self.updated_at, self.__dict__}
