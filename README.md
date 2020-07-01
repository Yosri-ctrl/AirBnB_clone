AirBnB Clone
What's a command interpreter:
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…
Each task is linked and will help you to:
    put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
    create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
    create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
    create the first abstracted storage engine of the project: File storage.
    create all unittests to validate all our classes and storage engine
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:
    Create a new object (ex: a new User or a new Place)
    Retrieve an object from a file, a database etc…
    Do operations on objects (count, compute stats, etc…)
    Update attributes of an object
    Destroy an object
To run the consol type 'python3 console.py' or './console.py' in the command line.
You can use the included classes BaseModel, User, City, State, Amenity, Review, and Place.
The console currently supports the following commands:
    create <class name>, create an object of the class typed
    show <class name> <id>, display the object information
    destroy <class name> <id>, delete the object
    all <class name>, show all objects of the class typed or show all classes if no class typed
    update <class name> <id> <attribute name> <attribute value>, update an instance attribute
    <class name>.all(), display all instances of the specified class
    <class name>.count(), display the number of instances of the specified class
    <class name>.show(<id>), display the instance with correct id typed
    <class name>.destroy(<id>), delete the instance with correct id typed
    <class name>.update(<id>, <attribute name>, <attribute value>), update an instance with the new attribute
