#!/usr/bin/python3
"""Console for holbertonschool-AirBnB_clone"""


import cmd
import sys
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {"BaseModel": BaseModel, "User": User, "State": State, "City": City,
           "Amenity": Amenity, "Place": Place, "Review": Review}


class HBNBCommand(cmd.Cmd):
    """
    our cmd loop interpreter
    """
    intro = 'Welcome to the shell. Type help or ? to list commands.\n'
    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, args):
        """Quit console at EOF\n"""
        print("")
        return True

    def emptyline(self):
        """No action: input is empty line + ENTER\n"""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel
        saves it (to the JSON file) and prints the id\n"""
        arg = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if len(arg) > 1:
            raise TypeError("Incorrect number of arguments")
        if args in classes:
            instance = eval(str(args) + "()")
            instance.save()
            print(instance.id)
        else:
            print("** class doesn't exist **")
            return False

    def do_show(self, args):
        """Prints the string representation of an instance\n"""
        arg = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if len(arg) == 1:
            print("** instance id missing **")
            return False
        if len(arg) > 2:
            raise TypeError("Incorrect number of arguments")
            return False
        if arg[0] not in classes:
            print("** class doesn't exist **")
            return False
        else:
            key = arg[0] + "." + arg[1]
            storage = models.storage.all()
            if key in storage:
                print(storage[key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id\n"""
        arg = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if len(arg) == 1:
            print("** instance id missing **")
            return False
        if len(arg) > 2:
            raise TypeError("Incorrect number of arguments")
            return False
        if arg[0] not in classes:
            print("** class doesn't exist **")
            return False
        else:
            key = arg[0] + "." + arg[1]
            storage = models.storage.all()
            if key in storage:
                del(storage[key])
                models.storage.save
            else:
                print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances
        Based or not on the class name\n"""
        arg = args.split()
        objList = []
        if len(args) == 0:
            for key in models.storage.all():
                objList.append(str(models.storage.all()[key]))
            print(objList)
        if len(arg) == 1:
            if arg[0] in classes:
                storage = models.storage.all()
                for key in storage:
                    if arg[0] in key:
                        objList.append(str(storage[key]))
                print(objList)
            else:
                print("** class doesn't exist **")

    def do_update(self, args):
        """Updates an instance
        Based on class name and id
        By adding or updating attribute"""
        arg = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if len(arg) == 1:
            print("** instance id missing **")
            return False
        if len(arg) == 2:
            print("** attribute name missing **")
            return False
        if len(arg) == 3:
            print("** value missing **")
            return False
        if len(arg) > 4:
            raise TypeError("Incorrect number of arguments")
            return False
        if arg[0] not in classes:
            print("** class doesn't exist **")
            return False
        else:
            key = arg[0] + "." + arg[1]
            storage = models.storage.all()
            if key in storage:
                setattr(storage[key], arg[2], arg[3])
                models.storage.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    """our main"""
    HBNBCommand().cmdloop()
