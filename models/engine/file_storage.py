#!/usr/bin/python3
"""
"""
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review
import models
import json


class FileStorage():
    """
    """
    dict = {'BaseModel': BaseModel,
            'User': User,
            'Amenity': Amenity,
            'City': City,
            'Place': Place,
            'Review': Review,
            'State': State}
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        """
        return self.__objects

    def new(self, obj):
        """
        """
        self.__objects["{}.{}".format(str(type(obj).__name__), obj.id)] = obj

    def save(self):
        """
        """
        dic = {}
        for id, objs in self.__objects.items():
            dic[id] = objs.to_dict()
        with open(self.__file_path, mode="w") as f:
            json.dump(dic, f)

    def reload(self):
        """
        """
        try:
            with open(self.__file_path, mode="r+") as f:
                obj = json.load(f)
            for i, j in obj.items():
                a = FileStorage.dict[j["__class__"]](**j)
                self.__objects[i] = a
        except FileNotFoundError:
            pass
