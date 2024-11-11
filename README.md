# Python Data Types and Structures Test

This repository contains a series of exercises designed to test your understanding and mastery of Python's data types and data structures. It includes tasks that cover basic data types, list operations, tuples, sets, dictionaries, and error handling. Each test is structured into smaller functions to make it easy for you to implement and for instructors to evaluate.
Structure Overview

## The project is organized as follows:

.
├── basic_test.py                 # Contains basic Python operations (integers, strings, booleans).
├── intermediate_test.py          # Tests involving lists, tuples, sets, and dictionaries.
├── advanced_test.py              # More complex tasks involving list comprehensions, nested structures, and dictionary manipulation.
├── error_handling_test.py        # Tests designed to help you handle common Python errors.
├── tests/                        # Folder containing all unit tests.
│   ├── test_basic.py             # Unit tests for the basic_test.py functions.
│   ├── test_intermediate.py      # Unit tests for the intermediate_test.py functions.
│   ├── test_advanced.py          # Unit tests for the advanced_test.py functions.
│   └── test_error_handling.py    # Unit tests for the error_handling_test.py functions.
├── requirements.txt             # File for any necessary dependencies.

## Files Overview:

    basic_test.py: Contains basic tasks such as integer operations, string manipulation, and boolean expressions.
    intermediate_test.py: Focuses on more complex data structures like lists, tuples, sets, and dictionaries.
    advanced_test.py: Includes advanced tasks such as list comprehensions, dictionary comprehensions, and nested data structures.
    error_handling_test.py: Includes exercises that focus on common Python errors such as IndexError and TypeError.
    tests/: Contains unit test files that test the functions in the corresponding *_test.py files.
    requirements.txt: Lists any necessary Python libraries for the project.

## Getting Started
1. Clone the Repository

To start working on the exercises, you can clone the repository to your local machine.

git clone git@github.com:MojahiMotaung/python_dataTypes_test.git
cd python_dataTypes_test

2. Set Up Your Environment

Ensure that you have Python 3 installed. If you don't have it yet, you can download and install Python 3 from the official site: python.org.

You can create a virtual environment to isolate dependencies for the project:

python3 -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows

3. Install Dependencies

If the project has any dependencies, they are listed in the requirements.txt file. Install them using pip:

pip install -r requirements.txt

4. Implement the Functions

Each file (basic_test.py, intermediate_test.py, advanced_test.py, and error_handling_test.py) contains a set of function stubs. Your job is to implement the logic for each function, following the instructions provided in the docstrings.
5. Run the Tests

Once you have implemented the functions, you can run the tests to verify your solutions.

To run the tests for any of the levels, you can use the unittest command. For example:

### Basic Level Test:

python -m unittest tests.test_basic

### Intermediate Level Test:

python -m unittest tests.test_intermediate

### Advanced Level Test:

python -m unittest tests.test_advanced

### Error Handling Test:

    python -m unittest tests.test_error_handling

### Alternatively, to run all the tests at once:

python -m unittest discover tests/

6. Review the Test Results

If the implementation is correct, you will see output similar to this:

...
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK

If any test fails, the error message will indicate which test failed and what the issue is, so you can review and correct the implementation.
## Function Descriptions
### Basic Test

    int_division(): Perform integer division (7 // 2).
    float_multiplication(): Multiply 3.0 by 2.
    combine_operations(): Combine integer division and float multiplication in one expression.
    extract_word(): Extract the word 'awesome' from the string "Python is awesome!".
    to_lowercase(): Convert the string "Python is awesome!" to lowercase.
    count_o(): Count how many times the letter 'o' appears in the string.
    evaluate_boolean(): Evaluate a boolean expression based on comparison operators.

### Intermediate Test

    List operations: Modify lists by adding, removing, inserting, and reversing elements.
    Tuple operations: Create new tuples from parts of existing ones and check for membership.
    Set operations: Find the intersection, union, and difference between two sets.
    Dictionary operations: Add, modify, delete, and retrieve values from a dictionary.

### Advanced Test

    List comprehension: Create a list of squares for all even numbers between 1 and 20.
    Dictionary comprehension: Convert a list of tuples into a dictionary.
    Nested data structures: Work with nested dictionaries and lists, performing tasks like accessing and modifying inner elements.

### Error Handling Test

    IndexError: Fix an index error when accessing a list.
    TypeError: Fix a type error involving string and integer concatenation.

## Contribution

If you want to contribute improvements, fixes, or additional exercises, feel free to fork this repository and submit a pull request. Any contributions are welcome!