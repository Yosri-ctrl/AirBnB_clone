#!/usr/bin/python3
import cmd
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    def do_quit(self, arg):
        """
    press quit to exit the program
        """
        return True

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()