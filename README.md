# holbertonschool-AirBnB_clone
https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220630%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220630T001625Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6b65f304378acd1db5752ae5e0cbea0cb3aa08eb660739a790d5413500023536
## Welcome to the AirBnB clone project!
#### This is the First step: A command interpreter to manage our AirBnB objects.
A command interpreter is similar to the Shell but limited to a specific use-case.  
Our command interprer is able to manage the objects of our project:
* Create a new object (ex: a new User, State, City, etc)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

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
