#!/usr/bin/python3
"""
creating console to manipulate classes
"""
import cmd
from shlex import split
from os import sys
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review
import re


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    dict = {'BaseModel': BaseModel,
            'User': User,
            'Amenity': Amenity,
            'City': City,
            'Place': Place,
            'Review': Review,
            'State': State}

    def do_quit(self, arg):
        """
    press quit to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
    handle the EOF
        """

        print()
        return True

    def emptyline(self):
        """

    execute nothing if a line is empty

        """
        pass

    def do_create(self, arg):
        """
    create a new instance and print the id
        """
        if len(arg) is 0:
            print("** class name missing **")
        elif arg not in self.dict.keys():
            print("** class doesn't exist **")

        else:

            created = self.dict[arg]()
            created.save()

            print(created.id)

    def do_show(self, arg):
        """
    print the string representation based on class name and id
        """
        arg = arg.split()
        try:
            args = arg[0] + "." + arg[1]
        except:
            pass
        objects = storage.all()
        if len(arg) is 0:
            print("** class name missing **")
        elif len(arg) == 1 and arg[0] in self.dict.keys():
            print("** instance id missing **")
        elif arg[0] not in self.dict.keys():
            print("** class doesn't exist **")
        elif args not in objects:
            print("** no instance found **")
        else:
            print(objects[args])

    