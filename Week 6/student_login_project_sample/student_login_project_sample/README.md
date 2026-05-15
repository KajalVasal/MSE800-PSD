
# Python Decorator Activity Logger
This project demonstrates how to use **Python decorators** to log user 
activities in a simple student management system.
The decorator records:
- Function name
- Current timestamp
- Activity start message
- Activity completion message

# Project Structure
project/
│
├── decorators.py
├── users.py
├── main.py
└── README.md

# Features
* Uses Python decorators
* Logs function execution details
* Demonstrates reusable logging functionality
* Simple and beginner-friendly project structure

# Files Description
## 1. decorators.py
Contains the `log_activity` decorator.

### Responsibilities:
* Prints activity header
* Displays function name
* Displays current date and time
* Executes wrapped function
* Prints completion message

## 2. users.py
Contains student-related functions:
* `student_login()`
* `submit_assignment()`
* `view_grades()`
All functions are decorated using `@log_activity`.

## 3. main.py
Main entry point of the application.
### Activities Performed:
1. Student login
2. Assignment submission
3. Viewing grades

# How It Works
The decorator wraps around each function and automatically logs activity details before and after execution.
Example:
python
@log_activity
def student_login(username):
    print(f"{username} logged into the system.")

When the function runs, the decorator prints logging information automatically.

# Installation & Run
## Requirements
* Python 3.13

## Run the Program
python main.py

# Concepts Used
* Python Functions
* Decorators
* Wrapper Functions
* `*args` and `**kwargs`
* Modules and Imports
* Datetime Module

# Author
Created as a Python learning project for practicing decorators and logging.

# Warning
In this project, for student login and submit assignment username is Mohammad but 
for view grades username is Alex.