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
        if arg[0] not in classes:
            print("** class doesn't exist **")
            return False
        if len(arg) > 1:
            print("Incorrect number of arguments")
            return False
        instance = eval(str(args) + "()")
        instance.save()
        print(instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance\n"""
        arg = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if arg[0] not in classes:
            print("** class doesn't exist **")
            return False
        if len(arg) == 1:
            print("** instance id missing **")
            return False
        if len(arg) > 2:
            print("Incorrect number of arguments")
            return False
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
        if arg[0] not in classes:
            print("** class doesn't exist **")
            return False
        if len(arg) == 1:
            print("** instance id missing **")
            return False
        if len(arg) > 2:
            print("Incorrect number of arguments")
            return False
        key = arg[0] + "." + arg[1]
        storage = models.storage.all()
        if key in storage:
            del(storage[key])
            models.storage.save()
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
        if len(arg) > 1:
            print("Incorrect number of arguments")
            return False

    def do_update(self, args):
        """Updates an instance
        Based on class name and id
        By adding or updating attribute"""
        arg = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if arg[0] not in classes:
            print("** class doesn't exist **")
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
            print("Incorrect number of arguments")
            return False
        key = arg[0] + "." + arg[1]
        storage = models.storage.all()
        arg[3] = arg[3].strip('\"')
        argCheck = arg[3].replace(".", "")
        if arg[3].isdigit():
            arg[3] = int(arg[3])
        elif argCheck.isdigit():
            arg[3] = float(arg[3])
        if key in storage:
            setattr(storage[key], arg[2], arg[3])
            models.storage.save()
        else:
            print("** no instance found **")

    def do_count(self, args):
        """retrieve the number of instances of a class\n"""
        arg = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if len(arg) == 1:
            if arg[0] in classes:
                storage = models.storage.all()
                count = 0
                for key in storage:
                    if arg[0] in key:
                        count += 1
                print(count)
            else:
                print("** class doesn't exist **")
                return False
        if len(arg) > 1:
            print("Incorrect number of arguments")
            return False

    def default(self, args):
        """Handle cmd in format <class name>.cmd()\n"""
        arg = args.split(".")
        if len(arg) > 1:
            if arg[0] in classes:
                if arg[1] == "all()":
                    self.do_all(arg[0])
                    return
                if arg[1] == "count()":
                    self.do_count(arg[0])
                    return
                command = arg[1].split("(")
                command[1] = command[1].replace(")", "")
                if command[0] == "show" or command[0] == "destroy":
                    command[1] = command[1].strip('\"')
                    new_cmd = arg[0] + " " + command[1]
                    if command[0] == "show":
                        self.do_show(new_cmd)
                    else:
                        self.do_destroy(new_cmd)
                    return
                if command[0] == "update":
                    command[1] = command[1].replace("{", "")
                    command[1] = command[1].replace("}", "")
                    command[1] = command[1].replace(".", "")
                    command[1] = command[1].replace('"', '')
                    command[1] = command[1].replace("'", "")
                    detail = command[1].split(", ")
                    if ": " in command[1]:
                        objId = detail[0]
                        for i in range(len(detail)):
                            if ": " in detail[i]:
                                upDate = detail[i].split(": ")
                                attrName = upDate[0]
                                attrValue = upDate[1]
                                new_cmd = arg[0] + " " + detail[0]\
                                    + " " + attrName + " " + attrValue
                                self.do_update(new_cmd)
                            i += 1
                        return
                    else:
                        new_cmd = arg[0] + " " + detail[0]\
                            + " " + detail[1] + " " + detail[2]
                        self.do_update(new_cmd)
                        return
                return cmd.Cmd.default(self, args)
            else:
                print("** class doesn't exist **")
                return False
        else:
            return cmd.Cmd.default(self, args)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
