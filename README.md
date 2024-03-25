This is a readme file that gives the description of the project, description of the command interpreter:
1. how to start it
2. how to use it
3. examples

Project Description:

The project is a command-line interpreter (CLI) for managing objects within a hypothetical housing rental application. The application allows users to create, view, update, and delete various types of objects such as states, cities, places, amenities, and reviews.

Command Interpreter Description:

The command interpreter is designed to provide a user-friendly interface for interacting with the application. It enables users to perform CRUD (Create, Read, Update, Delete) operations on the objects managed by the application.

How to Start:

To start the command interpreter, follow these steps:

Ensure that Python is installed on your system.
Clone the project repository from the provided URL.
Navigate to the project directory in your terminal or command prompt.
How to Use:

Once the command interpreter is started, you can use the following commands:

quit or EOF: Exit the program.
create <class_name>: Create a new instance of the specified class.
show <class_name> <object_id>: Display the details of the specified object.
destroy <class_name> <object_id>: Delete the specified object.
all <class_name>: Display all instances of the specified class.
update <class_name> <object_id> <attribute_name> <attribute_value>: Update the specified attribute of the object.

Examples:

To create a new state:
(hbnb) create State

To show details of a specific place:
(hbnb) show Place 1234-5678

To update the name of a city:
(hbnb) update City 9876-5432 name "New City Name"

To delete an amenity:
(hbnb) destroy Amenity 2468-1357

To display all reviews:
(hbnb) all Review

