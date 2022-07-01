# holbertonschool-AirBnB_clone
![65f4a1dd9c51265f49d0](https://user-images.githubusercontent.com/98162365/176899920-64b889dc-9e43-4413-b0a4-b1821b53dc2b.png)
## Welcome to the AirBnB clone project!
#### This is the First step: A command interpreter to manage our AirBnB objects.
A command interpreter is similar to the Shell but limited to a specific use-case.  
Our command interprer is able to manage the objects of our project:
* Create a new object (ex: a new User, State, City, etc)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object
### Programming languge
This project is written in Python 3.0, and use the pycodestyle(version 2.8.*)
### Description of each files:
| Folder Name | File Name | Description |
|-------------|-----------|-------------|
| | AUTHORS | lists all individuals having contributed content to the repository |
| | README.md | contains the information for the user about the project |
| | console.py | contains the entry point of the command interpreter, all the commands are implemented in this file |
| models | base_model.py | defines all common attributes/methods for other classes |
| models | user.py | inherits from BaseModel, defines class User |
| models | amenity.py | inherits from BaseModel, defines class Amenity |
| models | city.py | inherits from BaseModel, defines class Place |
| models | place.py | inherits from BaseModel, defines class User |
| models | state.py | inherits from BaseModel, defines class State |
| models | review.py | inherits from BaseModel, defines class Review |
| models/engine | file_storage | serializes instances to a JSON file and deserializes JSON file to instances |
| tests | test_console.py | unittest for methods in console.py
| tests/test_models | test_base_model.py | unittest for class BaseModel
| tests/test_models | test_user.py | unittest for class User
| tests/test_models | test_amenity.py | unittest for class Amenity
| tests/test_models | test_city.py | unittest for class City
| tests/test_models | test_place.py | unittest for class Place
| tests/test_models | test_state.py | unittest for class State
| tests/test_models | test_file_storage.py | unittest for storing objects in JSON file |
| tests/test_models/engine | test_console.py | unittest for functionalities of console.py |

### How to start the command interpreter
1. git clone https://github.com/yuan-fang-228/holbertonschool-AirBnB_clone.git
1. run ./console under the project folder to start this interpreter.
1. type in built-in commands
1. use "quit" or EOF to quit the interpreter
### Execution
This interpreter work in both interactive and non-interactive mode.
* Interactive Mode
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
* Non-interactive Mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
### Built-in commands
* EOF: quit the program.
* quit: quit the program.
* all: Prints all string representation of all instances based.
* all \<class name\>: print all the string representation of all instances of one class.
* help: list all the commands in this console.
* help \<command\>: provide the document of the command.
* \<class name\> count: retrieve the number of instances of a class.
* create \<class name\>: Creates a new instance of the class, saves it (to the JSON file) and prints the id.
* destroy \<class name\> \<id\>: Deletes an instance based on the class name and id (save the change into the JSON file).
* show \<class name\> \<id\>: Prints the string representation of an instance based on the class name and id.
* update \<class name\> \<id\> \<attribute name\> "\<attribute value\>": Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
### Examples
```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) help create
Creates a new instance of BaseModel
        saves it (to the JSON file) and prints the id

(hbnb) create User
e83b0b29-0f7d-40a1-9095-aa3dbe369d27
(hbnb) destroy User e83b0b29-0f7d-40a1-9095-aa3dbe369d27
(hbnb) show User e83b0b29-0f7d-40a1-9095-aa3dbe369d27
** no instance found **
(hbnb) quit
```
### Unittesting
All the test files can be executed by this command - 

```python3 -m unittest discover tests```

Or run tests file by file using this command -

```python3 -m unittest tests/test_models/test_base_model.py```

### Authors
* Cienna Nguyen
* Yuan Fang
* James Honey
