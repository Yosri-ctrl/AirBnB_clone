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

    def do_destroy(self, arg):
        """
    Deletes an instance based on the class name and id
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
            del objects[args]
            storage.save()

    def do_all(self, arg):
        """
    Prints all string representation of all instances
        """
        objs = []
        arg = arg.split()
        if arg and arg[0] not in HBNBCommand.dict.keys():
            print("** class doesn't exist **")
            return
        if len(arg) == 0:
            objs = [i.__str__() for i in storage.all().values()]
        else:
            for objects in storage.all().values():
                if arg[0] in objects.__class__.__name__:
                    objs.append(objects.__str__())
        print(objs)

    def default(self, line):
        line = line.split(".")
        if line[1] == "all()":
            return self.do_all(line[0])

    def do_update(self, arg):
        """
    Updates an instance based on the class name and id by adding or updating
        """
        arg = arg.split()
        try:
            h = arg[0] + "." + arg[1]
        except:
            pass
        objects = storage.all()
        if len(arg) is 0:
            print("** class name missing **")
        elif len(arg) == 1 and arg[0] in self.dict.keys():
            print("** instance id missing **")
        elif arg[0] not in self.dict.keys():
            print("** class doesn't exist **")
        elif h not in objects.keys():
            print("** no instance found **")
        elif len(arg) <= 2:
            print("** attribute name missing **")
        elif len(arg) <= 3:
            print("** value missing **")
        else:
            setattr(objects[h], arg[2], arg[3])
            storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
