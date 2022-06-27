#!/usr/bin/python3

import cmd, sys

class HBNBCommand(cmd.Cmd):
    # our cmd loop
    intro = 'Welcome to the shell.   Type help or ? to list commands.\n'
    prompt = '(hbnb) '

    # ------- basic commands --------

    def do_quit(self, arg):
        # close the cmd loop
        'quit the loop'
       	return True

    def do_EOF(self, arg):
        # close the cmd loop at EOF
        'EOF reached - quit'
        print("")
        return True

    def emptyline(self):
        # do nothing if empty line is input
        pass

    def do_hello(self, arg):
        # test command
        'prints Well, hello'
        print("Well, hello")

if __name__ == '__main__':
    # our main
    HBNBCommand().cmdloop()
