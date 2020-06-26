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
    
    f = "%Y-%m-%dT%H:%M:%S.%f"
    def __init__(self, *args, **kwargs):
        """
        """
        if kwargs is not None:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            for i, j in kwargs.items():
                if (i == "created_at" or i == "updated_at"):
                    j = datetime.strptime(j, self.f)
                    setattr(self, i, j)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()

    def __str__(self):
        """
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        """
        self.created_at = datetime.now().isoformat("T")
        self.updated_at = datetime.now().isoformat("T")
        dict = self.__dict__
        dict.update({'__class__': type(self).__name__})
        return dict
