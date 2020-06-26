#!/usr/bin/python3
import cmd
from os import sys
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    dict = {'BaseModel': BaseModel}
    def do_quit(self, arg):
        """
    press quit to exit the program
        """
        sys.exit(0)

    def do_EOF(self, arg):
        """
    handle the EOF
        """
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()