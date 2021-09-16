# MEDomicsUdeS Python Coding Standard

This document presents the Python coding standard of the MEDomicsUdeS lab. It also contains cool tips, tricks and links to code efficiently in Python.

## Table of Contents
- [MEDomicsUdeS Python Coding Standard](#medomicsudes-python-coding-standard)
  * [Table of Contents](#table-of-contents)
  * [Changelog](#changelog)
  * [Contributors](#contributors)
  * [To-Do](#to-do)
  * [Standard](#standard)
    + [R000 - Recommended Software](#r000---recommended-software)
    + [R001 - Style - PEP 8](#r001---style---pep-8)
    + [R002 - Project Repository Structure](#r002---project-repository-structure)
    + [R003 - Naming Variables - Functions - Classes](#r003---naming-variables---functions---classes)
    + [R004 - f-strings](#r004---f-strings)
    + [R005 - Type Hinting - PEP 484](#r005---type-hinting---pep-484)
    + [R006 - Docstring - PEP 257 - Google Style](#r006---docstring---pep-257---google-style)
    + [R007 - Comments](#r007---comments)
    + [R008 - String Quotes](#r008---string-quotes)
    + [R009 - Pythonic - The Zen of Python - PEP 20](#r009---pythonic---the-zen-of-python---pep-20)
    + [R010 - Multiprocessing and Compilation](#r010---multiprocessing-and-compilation)
    + [R011 - Main](#r011---main)
    + [R012 - Paths - Working Directory](#r012---paths---working-directory)
    + [R013 - Enumerations - PEP 435](#r013---enumerations---pep-435)
    + [R014 - Abstract Classes - PEP 3119](#r014---abstract-classes---pep-3119)
    + [R015 - Universite de Sherbrooke Computer Science Department Programming Standard](#r015---universite-de-sherbrooke-computer-science-department-programming-standard)
    + [R016 - Encapsulation - Private vs Protected vs Public](#r016---encapsulation---private-vs-protected-vs-public)
    + [R017 - Decorators](#r017---decorators)

NOTES: 

- To update the Table of Contents, use: https://ecotrust-canada.github.io/markdown-toc/
- Section headers cannot contain special characters other than -, otherwise the TOC hyperlinks will not work

## Changelog

Revision | Date       | Description |
---------| -----------| ----------- |
B        | 2021-09-13 | Updated based on team's comments    |
A        | 2021-08-08 | Creation    |

## Contributors

- [Simon Giard-Leroux](https://github.com/sgiardl)

## To-Do

- [x] Table of contents
- [x] Paths
- [x] More details on variable names (ie. equation variable), max chars of variable name
- [x] Enums
- [x] ABC
- [x] What is pythonic? List comprehension, etc.
- [x] Constants (all caps) vs Environment Variables
- [x] Multiprocessing
- [x] Check existing udes code standard & integrate contents
- [x] if __name__ == '__main__'
- [x] Encapsulation : protected vs private
- [ ] Class inheritance vs aggregation
- [x] decorators : staticmethod classmethod abstractmethod
- [ ] Reorder rules in a logic way

## Standard

### R000 - Recommended Software

Operating System:
- Ubuntu: https://ubuntu.com/
- Pop!OS: https://pop.system76.com/
- EndeavourOS: https://endeavouros.com/
- Arch Linux: https://archlinux.org/ (if you like to live dangerously)

Package Suite & Environment Manager:
- Anaconda: https://www.anaconda.com/products/individual

IDE:
- PyCharm Professional (free for students): https://www.jetbrains.com/shop/eform/students
- Visual Studio Code: https://code.visualstudio.com

Deep Learning Framework:
- PyTorch: https://pytorch.org/get-started/locally/

### R001 - Style - PEP 8

Follow all rules of the PEP 8 when coding in Python. The following list presents the most important aspects of PEP 8 to keep in mind when coding in Python. The detailed PEP can be found here: https://www.python.org/dev/peps/pep-0008/

- Indentation
  - Use 4 spaces per indentation level
- Maximum Line Length
  - 120 characters (not 79 characters as specified in PEP8)
- Blank Lines
  - Surround top-level function and class definitions with two blank lines
  - Method definitions inside a class are surrounded by a single blank line
  - Add a blank line at the end of each file
- Imports: 
  - Imports should be in alphabetical order.
  - Imports should usually be on separate lines.
  - Imports are always put at the top of the file, just after any module comments and docstrings, and before module globals and constants.
  - Imports should be grouped in the following order:
    - Standard library imports.
    - Related third party imports.
    - Local application/library specific imports.
    - You should put a blank line between each group of imports.

To help follow the PEP 8, you can use an IDE with a built-in PEP 8 syntax checker, such as PyCharm or Visual Studio Code.

### R002 - Project Repository Structure

Use cookiecutter-datascience when creating a new repository. This utility creates an initial folder and file structure that is well suited for data science / machine learning projects.

To use cookiecutter-datascience, follow the guide on this page: https://github.com/drivendata/cookiecutter-data-science

### R003 - Naming Variables - Functions - Classes 

- Adopt "snake case" OR "camel case" (but not both) when naming variables, functions, methods and attributes.
- Use descriptive names for variables.
- For functions and methods, start the name with an imperative action verb, (except boolean return value: can be a question).
- For class names, start each word with a capital letter (Pascal case).
- Class names should represent an object or an actor that can execute concrete actions.
- Use all-caps for constants names. Place all constants in a separate file called 'constants.py'.
- When dealing with an equation, use variable names that match the variables of the equation itself, for example use 'alpha' or 'beta'.
- Keep the names of variables, functions and classes within a reasonable length (25-30 characters max.)

Examples:

```python
# Variable Names Snake Case
fruits_list = ['apple', 'banana', 'pineapple']
area_under_curve = 34.6

# Variable Names Camel Case
fruitsList = ['apple', 'banana', 'pineapple']
areaUnderCurve = 34.6

# Functions & Methods Snake Case
def calculate_area_under_curve(*args):

# Functions & Methods Camel Case
def calculateAreaUnderCurve(*args):

# Classes Pascal Case
class AreaCalculator:

# Constants
NUM_WORKERS = 24
IMAGE_EXT = 'jpg'

# Equations
def calculate_y(m: float, x: float, b: float) -> float:
    return m * x + b
```

### R004 - f-strings

The most useful way to manage strings in Python is the f-string, which was introduced in Python 3.6. Use f-strings whenever possible to enhance code readability. More details can be found at the following link: https://docs.python.org/3/reference/lexical_analysis.html#f-strings.

Example:

```python
builder_name = "Bob"

print(f'Hi there, my name is {builder_name}')

hourly_wage = 99.91 # Hourly wage in dollars

print(f'I work long hours! The total price for a day is {24 * hourly_wage:.2f}')
```

### R005 - Type Hinting - PEP 484

While Python is a dynamically typed language, PEP 484 was introduced to allow coders to specify argument and return value types for functions and methods. If a type is specified for a function argument, Python will not raise an exception: type hints are merely used to inform. Follow PEP 484 for all functions and methods, more details can be found at the following link: https://www.python.org/dev/peps/pep-0484/.

Example:

```python
def greeting(name: str) -> str:
    return 'Hello ' + name
```

Even for class constructors, specify return type as None. For example:

```python
class BobTheBuilder:
    def __init__(self, has_hammer: bool = True) -> None:
        self.has_hammer = has_hammer
```
### R006 - Docstring - PEP 257 - Google Style

Write a docstring at the beginning of each Python .py file containing the following information:
- File name
- Authors
- Description
- Date of last modification

Write a docstring at the beginning of each class describing the general purpose of the class.

Write a docstring at the beginning of each function or method to describe the function/method purpose, arguments type and expected values and return type and expected values. Place this docstring right after the defintion of the function/method.

Follow PEP 257: https://www.python.org/dev/peps/pep-0257/

Follow the Google docstring style: https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

### R007 - Comments

Add a textual comment in English before each line or block of lines to help reviewers understand your train of thought or intention.

### R008 - String Quotes

Use either ' OR " for strings delimiters, but not both.

### R009 - Pythonic - The Zen of Python - PEP 20

The Zen of Python (from PEP 20: https://www.python.org/dev/peps/pep-0020/):
```
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

Implement "Pythonic" code as much as possible, which means, for example:
- Avoid using loops as much as possible, take advantage of the vectorized nature of the language. For example, to calculate the sum of numerical values inside a list:
```python
my_list = [50, 100, 150, 200]

# Bad Non-Pythonic Unvectorized Way

sum = 0

for i in range(len(my_list)):
    sum = sum + my_list[i]
    
# Good Pythonic Vectorized Way
my_sum = sum(my_list)
```
- Use List Comprehension as much as possible. For example, to filter out a list:
```python
my_list = ['Apple', 'Orange', 'Cabbage', 'Orange']

# Without List Comprehension

filtered_list = []

for item in my_list:
    if item != 'Orange':
        filtered_list.append(item)

# With List Comprehension

filtered_list = [item for item in my_list if item != 'Orange']
```
### R010 - Multiprocessing and Compilation

By default, Python uses a single CPU thread to perform calculations. In order to use the full potential of modern multithread CPU's, various multiprocessing libraries have been created. For example:
- Built-in 'multiprocessing' library: https://docs.python.org/3/library/multiprocessing.html
- Ray: https://ray.io/

Python is an interpreted language, which makes the language multi-platform but this is a trade-off in terms of performance. Various libraries have been created to speed up computation by implementing Just-in-time (JIT) compilation for Python, for example:
- Numba: http://numba.pydata.org/

It is also possible to use the GPU to perform some calculations to improve performance, for example : 
- CUDA + Numba: https://developer.nvidia.com/how-to-cuda-python

### R011 - Main

In the main Python file that you execute, you should include the following construct between the imports and your code:

```python
# Imports

if __name__ == '__main__':
    # Code
```
This will make sure that if you import this main file to use some of its functions elsewhere, the main code block will not be executed during the importation.

It is the equivalent of the following C++ main construct:
```cpp
// Imports

int main() {
    // Code
    return 0;
}
```
### R012 - Paths - Working Directory

Normally, you should place the main Python file to be executed in the root of the repository, which is the working directory, and imports should refer to files that are present in a 'src' folder. For example, if you want to import MyClass from the 'src/data/utils.py' file, your import statement should be written as such:

```python
from src.data.utils import MyClass
```

You can use different methods of the 'os' library to get or change the working directory path, for example:

```python
# To get the current working directory
path = os.getcwd()

# To change the working directory (ie. move back 1 folder)
os.chdir('..')
```

### R013 - Enumerations - PEP 435

Enumerations allow a simple interface between human-readable string values and numerical values. For example, if you want your class to have a method with a color as an argument, you can specify all possible colors using an enumeration, each being associated to an integer value. This can improve the interactibility and optimize your classes.

Read the standard library documentation on enumerations: https://docs.python.org/3/library/enum.html

```
An enumeration is a set of symbolic names (members) bound to unique, constant values. Within an enumeration, the members can be compared by identity, and the enumeration itself can be iterated over.

Because Enums are used to represent constants we recommend using UPPER_CASE names for enum members, and will be using that style in our examples.
```

```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
```

Guide on when to use Enums: https://stackoverflow.com/questions/37601644/python-whats-the-enum-type-good-for

```
When should I use enum.Enum?

Use it anywhere you have a canonical source of enumerated data in your code where you want explicitly specified to use the canonical name, instead of arbitrary data.

For example, if in your code you want users to state that it's not "Green", "green", 2, or "Greene", but Color.green - use the enum.Enum object. It's both explicit and specific.

```

Read PEP 435: https://www.python.org/dev/peps/pep-0435/

### R014 - Abstract Classes - PEP 3119

To implement an abstract class in Python, which is a signature class that cannot be instanced itself but only its child classes can be, you can use the 'abc' library (ABC : Abstract Base Class):

```python
from abc import ABC

class AbstractClass(ABC):
    pass
```

Read the standard library documentation: https://docs.python.org/3/library/abc.html

Read PEP 3119: https://www.python.org/dev/peps/pep-3119/

### R015 - Universite de Sherbrooke Computer Science Department Programming Standard

The Université de Sherbrooke Computer Science Department created a programming standard in 2004 for the C++ and Java languages. It contains general good practices and guidelines for writing clear and concise code.

Refer to the following document: 
https://www.usherbrooke.ca/informatique/fileadmin/sites/informatique/documents/Intranet/Documentation_informatique/Normes_de_programmation/normes-de-programmation-1.pdf

### R016 - Encapsulation - Private vs Protected vs Public

In Python, encapsulation can be implemented in classes so that some attributes or methods can be public, protected or private:
- Public: can be accessed from inside the class, outside the class and child classes (no underscore before name)
- Protected: can be accessed from inside the class and child classes (1 underscore before name)
- Private: can be accessed from inside the class only (2 underscores before name)

Example:

```python
class MyClass:
    def __init__(self) -> None:
        self.x = 4   # Public Attribute
        self._y = 6  # Protected Attribute
        self.__z = 8 # Private Attribute

    # Public Method
    def get_product_x_y(self):
        return self.x * self._y
        
    # Protected Method
    def _get_product_x_z(self):
        return self.x * self.__z
        
    # Private Method
    def __get_product_y_z(self):
        return self._y * self.__z
        
my_object = MyClass()

my_object.x   # Can be read
my_object._y  # Cannot be read
my_object.__z # Cannot be read

prod = my_object.get_product_x_y()   # Can be used
prod = my_object._get_product_x_z()  # Cannot be used
prod = my_object.__get_product_y_z() # Cannot be used
```

To implement an attribute as read-only, which means it can be read from outside the class but not changed from outside the class, you can make it private and use a @property decorator, for example:

```python
class MyClass:
    def __init__(self) -> None:
        self.__x = 4   # Private Attribute

    @property
    def x(self):
        return self.__x
        
my_object = MyClass()

my_object.x # self.__x can be accessed as read only
```

### R017 - Decorators

In Python, decorators are wrappers that are specified above a function definition with an @. The following is a list of common decorators used in Python:

- @abstractmethod: To force a certain abstract method to be defined in child classes inheriting from an abstract parent class.
```python
from abc import ABC

class MyAbstractClass(ABC):
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def calculate_area(x: int, y, int) -> int:

```

- @staticmethod

- @classmethod

- @property

- @torch.no_grad()

