<h1>#0x00. AirBnB clone - The console</h1>


<h2>Welcome to the AirBnB clone project!</h2>

First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help us to:

  *put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
  *create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
  *create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
  *create the first abstracted storage engine of the project: File storage.
  *create all unittests to validate all our classes and storage engine


Execution

The shell should work like this in interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
But also in non-interactive mode: (like the Shell project in C)

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

<h2>More Info</h2>
 *The code passes a Pycodestyle checks
 *All files, classes and functions tested with unit tests
    #####Example####
	  guillaume@ubuntu:~/AirBnB$ python3 -m unittest discover tests
      ..............................................................................
      ........................................................................
      .......................
      ---------------------------------------------------------------------
      Ran 189 tests in 13.135s

      OK
      guillaume@ubuntu:~/AirBnB$
	  
	Note that this is just an example, the number of tests creaed can be different from the above example
	<hr>
	<hr>
	
## 0x00.Table of contents

- [0x01 Introduction](#0x01-Introduction)
- [0x02 Environment](#0x02-Environment)
- [0x03 Installation](#0x03-Installation)
- [0x04 Testing](#0x04-Testing)
- [0x05 Usage](#0x05-Usage)


## 0x01 Introduction

Team project to build a clone of [AirBnB](https://www.airbnb.com/).

The console is a command interpreter to manage objects abstraction between objects and how they are stored.

To see the fundamental background of the project visit the [Wiki](https://github.com/ralexrivero/AirBnB_clone/wiki).

The console will perform the following tasks:

- create a new object
- retrive an object from a file
- do operations on objects
- destroy an object

<h2> Storage</h2>

All the classes are handled by the `Storage` engine in the `FileStorage` Class.

<h2> 0x02 Environment</h2>

The project is developed in Python and follows the PEP 8 style guide. Ensure you have Python 3.x installed in your environment.

<h2> 0x03 Installation</h2>

Clone the repository to your local machine:


Change into the project directory:

cd AirBnB_clone

<h2>0x04 Testing</h2>
To run the unit tests, execute the following command:
python3 -m unittest discover tests

All files, classes, and functions are tested to ensure the correctness of the implementation.

<h2>0x05 Usage</h2>
Interactive Mode
To run the console in interactive mode, use the following command:

./console.py

<h2>Non-Interactive Mode</h2>
You can also use the console in non-interactive mode by piping commands into it. For example:
echo "help" | ./console.py

<h2>Available Commands</h2>
The console supports the following commands:

help: Display information about available commands.
quit or EOF: Exit the console.
Additional commands are implemented for creating, retrieving, updating, and deleting AirBnB objects. Refer to the interactive mode examples in the Introduction section for more details.

<h2>More Info</h2>
The code passes Pycodestyle checks.
Comprehensive unit tests are provided to validate the functionality of all classes and the storage engine.
Feel free to explore and contribute to the project! Visit the Wiki for more detailed information about the architecture and design decisions.
