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
#### Programming languge
This project is written in Python 3.0, and use the pycodestyle(version 2.8.*)
### Description of each files:
| Folder Name | File Name | Description |
|-------------|-----------|-------------|
| | AUTHORS | lists all individuals having contributed content to the repository |
| | README.md | contains the information for the user about the project |
| | console.py | contains the entry point of the command interpreter |
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
### Built-in commands
### Examples
### Unittesting

### Authors
* Cienna Nguyen
* Yuan Fang
* James Honey
