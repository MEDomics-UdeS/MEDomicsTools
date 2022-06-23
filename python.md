# MEDomicsTools Python Coding Standard

This document presents the Python coding standard of the MEDomicsLab team. It also contains cool tips, tricks and links to code efficiently in Python.

## Table of Contents
- [MEDomicsTools Python Coding Standard](#medomicstools-python-coding-standard)
  - [Table of Contents](#table-of-contents)
  - [Contributors](#contributors)
  - [Changelog](#changelog)
  - [To-Do](#to-do)
  - [Standard](#standard)
    - [R000 - Recommended Software](#r000---recommended-software)
    - [R001 - Universite de Sherbrooke Computer Science Department Programming Standard](#r001---universite-de-sherbrooke-computer-science-department-programming-standard)
    - [R002 - Project Repository Structure](#r002---project-repository-structure)
    - [R003 - Pythonic - The Zen of Python - PEP 20](#r003---pythonic---the-zen-of-python---pep-20)
    - [R004 - Main](#r004---main)
    - [R005 - Paths - Working Directory](#r005---paths---working-directory)
    - [R006 - Style - PEP 8](#r006---style---pep-8)
    - [R007 - Naming Variables - Functions - Classes](#r007---naming-variables---functions---classes)
    - [R008 - Type Hinting - PEP 484](#r008---type-hinting---pep-484)
    - [R009 - Docstring - PEP 257 - Google Style](#r009---docstring---pep-257---google-style)
    - [R010 - Comments](#r010---comments)
    - [R011 - String Quotes](#r011---string-quotes)
    - [R012 - f-strings and r-strings](#r012---f-strings-and-r-strings)
        - [f-strings](#f-strings)
        - [r-strings](#r-strings)
    - [R013 - Multiprocessing and Compilation](#r013---multiprocessing-and-compilation)
    - [R014 - Enumerations - PEP 435](#r014---enumerations---pep-435)
    - [R015 - Abstract Classes - PEP 3119](#r015---abstract-classes---pep-3119)
    - [R016 - Encapsulation - Private vs Protected vs Public](#r016---encapsulation---private-vs-protected-vs-public)
    - [R017 - Decorators](#r017---decorators)
    - [R018 - Project Requirements](#r018---project-requirements)
    - [R019 - Distributing Python Modules](#r019---distributing-python-modules)
    - [R020 - Class inheritance vs Aggregation](#r020---class-inheritance-vs-aggregation)
    - [R021 - Debugging and Logging](#r021---debugging-and-logging)
    - [R022 - File and Folder Names](#r022---file-and-folder-names)
    - [R023 - Positional and Keyword Argument](#r023---positional-and-keyword-argument)
    - [R024 - Regular Expressions](#r024---regular-expressions)

NOTES: 

- To update the Table of Contents, use: https://ecotrust-canada.github.io/markdown-toc/
- Section headers cannot contain special characters other than -, otherwise the TOC hyperlinks will not work

## Contributors

- [Achille Lanctôt-Saumure](https://github.com/Troy-Boy)
- [Alexandre Ayotte](https://github.com/AleAyotte)
- [Mahdi Ait Lhaj Loutfi](https://github.com/MahdiAll99)
- [Martin Vallières](https://github.com/mvallieres)
- [Maxence Larose](https://github.com/MaxenceLarose)
- [Nicolas Raymond](https://github.com/Rayn2402)
- [Olivier Lefebvre](https://github.com/Olivier998)
- [Simon Giard-Leroux](https://github.com/sgiardl)

## Changelog

Revision | Date       | Description |
---------| -----------| ----------- |
F        | 2022-06-01 | Added multiple new sections    |
E        | 2022-02-10 | Added 'pipreqs' details    |
D        | 2021-12-01 | Updated based on team's comments    |
C        | 2021-10-04 | Added new items in to-do list    |
B        | 2021-09-13 | Updated based on team's comments    |
A        | 2021-08-08 | Creation    |

## To-Do

- [x] Class inheritance vs aggregation (Mahdi)
- [x] decorators : staticmethod classmethod abstractmethod (Nicolas)
- [x] Function/method calls : specify 1 or multiple arguments per line? (Nicolas)
- [x] Use 'pipreqs' package to generate project 'requirements.txt' file (Simon)
- [x] Start file and folder names in repository with lower case letters (Alex)
- [x] Bare * in arguments list to force use of keyword arguments and prevent positional arguments (Alex)
- [x] Regex (Hakima)
- [x] Creating PyPI packages (Maxence)
- [ ] Section on 'is' (identity), '==' (equality), 'Falsy/Truthy' vs 'True/False' (https://www.freecodecamp.org/news/truthy-and-falsy-values-in-python/) (Alex)
- [x] Lines wrapping/continuation (Mahdi)
- [x] r-strings (Mahdi)
- [x] Add new decorators in 'Decorators' section (https://github.com/lord63/awesome-python-decorator) (Mahdi)
- [x] Add details in the 'Comments' section, ie. when to use # or """ or ''' (Mahdi)
- [x] Add section on debugging (ie. use an IDE's debugger and not print statements everywhere) and the use of the 'logging' package (https://docs.python.org/2.7/library/logging.html) (Mahdi)

## Standard

### R000 - Recommended Software

Operating System:
- Ubuntu: https://ubuntu.com/
- Pop!OS: https://pop.system76.com/
- EndeavourOS: https://endeavouros.com/
- Arch Linux: https://archlinux.org/ (if you like to live dangerously)

Package Suite & Environment Manager:
- Anaconda: https://github.com/sgiardl/MEDomicsTools/blob/main/linux.md#using-anaconda

IDE:
- PyCharm Professional (free for students): https://www.jetbrains.com/shop/eform/students
- Visual Studio Code: https://code.visualstudio.com
 - Use 'pylint' for automatic PEP 8 syntax checking: https://code.visualstudio.com/docs/python/linting

Deep Learning Framework:
- PyTorch: https://pytorch.org/get-started/locally/

### R001 - Universite de Sherbrooke Computer Science Department Programming Standard

The Université de Sherbrooke Computer Science Department created a programming standard in 2004 for the C++ and Java languages. It contains general good practices and guidelines for writing clear and concise code.

Refer to the following document: 
https://www.usherbrooke.ca/informatique/fileadmin/sites/informatique/documents/Intranet/Documentation_informatique/Normes_de_programmation/normes-de-programmation-1.pdf

### R002 - Project Repository Structure

Use cookiecutter-datascience when creating a new repository. This utility creates an initial folder and file structure that is well suited for data science / machine learning projects.

To use cookiecutter-datascience, follow the guide on this page: https://github.com/drivendata/cookiecutter-data-science

### R003 - Pythonic - The Zen of Python - PEP 20

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

### R004 - Main

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

### R005 - Paths - Working Directory

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

### R006 - Style - PEP 8

Follow all rules of the PEP 8 when coding in Python. The following list presents the most important aspects of PEP 8 to keep in mind when coding in Python. The detailed PEP can be found here: https://www.python.org/dev/peps/pep-0008/

- For PyCharm, the settings can be changed in the 'Settings > Editor > Code Style' menu
- For Visual Studio Code, the settings can be changed in the 'settings.json' file (see https://code.visualstudio.com/docs/python/linting)

- Indentation
  - Use 4 spaces per indentation level (don't use tabs, use spaces, see https://www.python.org/dev/peps/pep-0008/#tabs-or-spaces)
- Maximum Line Length
  - 120 characters (not 79 characters as specified in PEP8)
- Blank Lines
  - Surround top-level function and class definitions with two blank lines
  - Method definitions inside a class are surrounded by a single blank line
  - Add a blank line at the end of each file
- lines wrapping and continuation
  - The preferred way of wrapping long lines is by using Python's implied line continuation inside parentheses(<span style="color:blue">(</span>), brackets(<span style="color:blue">[</span>) and braces(<span style="color:blue">{</span>). Example of parenthesized line break: :
    ```python
    list(
        "Welcome to MEDomics."
        )
    ```
  - Sometimes using a backslash looks better. Make sure to indent the continued line appropriately. The preferred place to break around a binary operator is after the operator, not before it. Example of back-slashed line break:
    ```python
    print 'This is a very long line, \
        but we can write it on multiple lines.'
    ```
  - Continuation lines should align wrapped elements either vertically using Python's implied line continuation inside parentheses (see example above), or using a hanging indent (see example down below). When using a hanging indent, there should be no arguments on the first line and further indentation should be used to clearly distinguish itself as a continuation line. The following example shows the correct way to do this :
    ```python
    # Hanging indents :
    foo = some_random_func(
        arg1, arg2,
        arg3, arg4)
    ```
    see [PEP8-indentation](https://www.python.org/dev/peps/pep-0008/#indentation).
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

### R007 - Naming Variables - Functions - Classes 

- Adopt "snake_case" OR "camelCase" (but not both) when naming variables, functions, methods and attributes.
- Use descriptive names for variables.
- For functions and methods, start the name with an imperative action verb, (except boolean return value: can be a question).
- For functions and methods, enumerate the arguments (following 'self' if it's a method) by adding a new line between each of them.
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
def calculate_y(m: float,
                x: float,
                b: float) -> float:
  
    return m * x + b
```

### R008 - Type Hinting - PEP 484

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

### R009 - Docstring - PEP 257 - Google Style

Write a docstring at the beginning of each Python .py file containing the following information:
- File name
- Authors
- Description
- Date of last modification

Write a docstring at the beginning of each class describing the general purpose of the class, the public methods and public attributes available.

Write a docstring at the beginning of each function or method to describe the function/method purpose, arguments type and expected values and return type and expected values. Place this docstring right after the definition of the function/method.

Follow PEP 257: https://www.python.org/dev/peps/pep-0257/

For new projects, the Google docstring style is recommended: https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

This rule is not made to be coercitive and to force you to rewrite all your code with a specific docstring standard, the most important point is to maintain consistency throughout your project. If starting a new project, the Google docstring style is recommended but not mandatory, other docstring styles can be used (ie. numpy).

### R010 - Comments

Add a textual comment in English before each line or block of lines to help reviewers understand your train of thought or intention. There are three types of comments that are used depending on the context:
- #### Inline comments
    An inline comment is a comment on the same line as the code. Inline comments should be separated by at least two spaces from the code. They should start with a # and a single space. For example :
    ```python
     name = "MEDomics"    # We assign a new value to the variable name
    ```
- #### Block comments
    Block of comments is a multi-inline comments, each line starts with a # and a single space. It is generally applied to the code the follows them and have the same indentation as that code. For example :
    ```python
    # We use * for multiplication of numbers
    # Finally we use print() function to print the value function
    print(3 * 7)
    ```
- #### Documentation strings
    Usually called 'docstrings'. Used most of the times to describe what the method does and should appear under the <em>def</em> line. For good docstings conventions refer to [R009](#r009---docstring---pep-257---google-style).


### R011 - String Quotes

Use either ' OR " for strings delimiters, but not both.

### R012 - f-strings and r-strings

- #### f-strings

    The most useful way to manage strings in Python is the f-string, which was introduced in Python 3.6. Use f-strings whenever possible to enhance code readability. More details can be found at the following link: https://docs.python.org/3/reference/lexical_analysis.html#f-strings.

    Example:

    ```python
    builder_name = "Bob"

    print(f'Hi there, my name is {builder_name}')

    hourly_wage = 99.91 # Hourly wage in dollars

    print(f'I work long hours! The total price for a day is {24 * hourly_wage:.2f}')
    ```

- #### r-strings

    r-strings or Python raw string is a string with the prefix 'r' or 'R'. r-string treats backslach(\\) as literal character and not as an escape character.

    Example:

    ```python
    s = "Hel\lo"
    raw_s = r"Hello"

    print(f's : {s}')

    print(f'raw_s : {raw_s}')
    ```

    Output:

    ```python
    Hel\lo
    Hello
    ```
To discover more about different types of string prefix refer to : https://docs.python.org/3/reference/lexical_analysis.html#literals

### R013 - Multiprocessing and Compilation

By default, Python uses a single CPU thread to perform calculations. In order to use the full potential of modern multithread CPU's, various multiprocessing libraries have been created. For example:
- Built-in 'multiprocessing' library: https://docs.python.org/3/library/multiprocessing.html
- Ray: https://ray.io/

Python is an interpreted language, which makes the language multi-platform but this is a trade-off in terms of performance. Various libraries have been created to speed up computation by implementing Just-in-time (JIT) compilation for Python, for example:
- Numba: http://numba.pydata.org/

It is also possible to use the GPU to perform some calculations to improve performance, for example : 
- CUDA + Numba: https://developer.nvidia.com/how-to-cuda-python

### R014 - Enumerations - PEP 435

Enumerations allow a simple interface between human-readable string values and numerical values. For example, if you want your class to have a method with a color as an argument, you can specify all possible colors using an enumeration, each being associated to an integer value. This can improve the intractability and optimize your classes.

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

### R015 - Abstract Classes - PEP 3119

To implement an abstract class in Python, which is a signature class that cannot be instanced itself but only its child classes can be, you can use the 'abc' library (ABC : Abstract Base Class):

```python
from abc import ABC

class AbstractClass(ABC):
    pass
```

Read the standard library documentation: https://docs.python.org/3/library/abc.html

Read PEP 3119: https://www.python.org/dev/peps/pep-3119/

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

- @abstractmethod: To force a certain abstract method to be defined in all child classes that inherit from an abstract parent class.
```python
from abc import ABC

class MyAbstractClass(ABC):
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def calculate_area(self, x: int, y, int) -> int:
        pass
```

- @staticmethod: When the access to the instance of a class itself is unneeded in a method, adding this decorator will remove the need to add 'self' as the first argument.
```python
class MyClass:
    def __init__(self) -> None:
        self.x = 40
    
    def calculate_area(self, y: float) -> float:
        return self.x * y
    
    @staticmethod
    def calculate_new_area(x: float, y: float) -> float:
        return x * y
```
- @classmethod: When the access to the instance of a class is unneeded but the access to the class itself is needed, adding this decorator will force the need of 'cls' as the first argument.
An example of usage could be to provide a class with a different constructor.
```python
class Square:
    def __init__(self, side_length_in_cm: float) -> None:
        self.length = side_length_in_cm
    
    @classmethod
    def from_decimeter(cls, side_length_in_dm: float):
        return cls(side_length_in_cm=side_length_in_dm*10)
```
- @property: A built-in decorator for the property() function in python. It makes the functions act as getters, setters or deleters. This is explained best with an example:
```python
class Person:

	def __init__(self, name):
		self._name = name

	@property
	def price(self):
		return self._name
	
	@price.setter
	def name(self, new_name):
        if isinstance(new_name, str):
		    self._name = new_name
        else:
            print("Please enter a valid name")

	@price.deleter
	def name(self):
		del self._name
```
-@deprecated : A python decorator to deprecate old python classes, functions or methods. Example of usage:
```python
from deprecated import deprecated

class Person(object):
    @deprecated
    def some_old_method(self):
        print(self._name)
```
You can use it with a "reason" message to help choose another alternative:
```python
from deprecated import deprecated

class Person(object):
    @deprecated(reason="This is an old method, use show_name() instead")
    def some_old_method(self):
        print(self._name)
```
- @torch.no_grad(): deactivate autograd in PyTorch, for example when calculating validation losses without performing a backward pass on the model weights, equivalent of <em>with torch.no_grad():</em>

Python has more awesome decorators for you, find out more about it here : [Python awesome decorators](https://github.com/lord63/awesome-python-decorator).

### R018 - Project Requirements

In the root folder of your repository, add a 'requirements.txt' file containing a list of all Python packages and versions used in your project. 

The following terminal command is **NOT** recommended, since it will generate a list of ALL packages in your actual environment, not only the ones that are used in the project:
```
# DO NOT USE THIS
pip freeze > requirements.txt
```

The 'pipreqs' package is recommended instead. It will only list the packages and versions that are imported in the project files. First, install the 'pipreqs' package:

```
# USE THIS
pip install pipreqs
```

Then, simply run the following command in the root folder of your project:
```
# USE THIS
pipreqs --force
```

### R019 - Distributing Python Modules

This [repository](https://github.com/MaxenceLarose/ProgFest-PackageDistributionIntroduction) presents a minimal example of a properly structured python package. It also contains a [pdf presentation](https://github.com/MaxenceLarose/ProgFest-PackageDistributionIntroduction/blob/main/DistributingPythonModules.pdf) (french only) that explains the main aspects of distributing a python module, namely

- What's a package?
- PyPI
- Project structure
- Automatic documentation
- Continuous integration using GitHub Actions

### R020 - Class inheritance vs Aggregation

In Python, class inheritance allows the definition of class that inherits all methods and properties from another class. The class that inherits is called **child class** or **derived class** and the class inherited from is called **parent class** or **base class**. In the following example we create a parent class called ***Teacher*** with the property ***name*** and a child class called ***Student*** that will have the same property as its parent class :

```python
class Teacher:
    def __init__(self, name):
        self.name = name
    
class Student(Teacher):
    def __init__(self, name):
        super().__init__(name)
``` 

On the other hand, aggregation is when an object can access another object, which means both objects can exist independently. In other words, the parent only contains a reference to the child. In the following example, we see that each object ***person*** is associated with a ***country***, but the ***country*** can exist without the ***person***:

```python
class Country:
    def __init__(self, name, capital):
        self.name = name
        self.capital = capital
        
class Person:
    def __init__(self, name, country):
        self.name = name
        self.country = country
```
The question now is: When to use aggregation or inheritance?
- If the new class needs most of the functionality of the original class, use inheritance.    
- If the new class has a different behavior than the original class and needs to change, use aggregation.

In a nutshell, we use aggregation, if part of the original class needs to be changed and we use inheritance, if we need almost all of the functionality of the original class without major changes.

### R021 - Debugging and Logging

Debugging is to go through your code step by step, to find where you exactly made a mistake. Once you have determined the bug, you find a fix, you apply it and finally test it. Most IDEs provide debugging tools like [Visual Studio](https://docs.microsoft.com/en-us/visualstudio/python/tutorial-working-with-python-in-visual-studio-step-04-debugging?view=vs-2022) or [PyCharm](https://www.jetbrains.com/help/pycharm/debugging-your-first-python-application.html) that will help you monitor the code while it's running and examine it carefully. You can set breakpoints that indicated where to pause the code so you can take a look at the values of variables, or the behavior of memory, or the sequence in which code runs.

Another useful tool for programmers is **Logging**. It helps programmers develop a better understanding of the flow of the program and the scenarios that might happen while running it. The [logging module](https://docs.python.org/3/library/logging.html) helps you integrate your log messages so that it can be used to log events. By default, there are 5 standard levels indicating the severity of events. Each has a corresponding method that can be used to log events at that level of severity. The defined levels, in order of increasing severity, are the following:
- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

And it can be called as shown in this example : 
```python
import logging 

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
```

To go even further, we can add our specific configuration to the logging, for example, we can specify a logging file rather than using the console:

```python
import logging

logging.basicConfig(filename='myapp.log')
logging.warning('This warning message will get logged to myapp.log')
```

Then we can also use it to log our exceptions information:

```python
logging.info('Started running')
a = 5
b = 0
try:
  c = a / b
except Exception as e:
  logging.exception(f"Exception occurred: {e}")
```

We encourage you to refer to the [logging module website](https://docs.python.org/3/library/logging.html) to learn more about the other useful features that it has to offer.

### R022 - File and Folder Names
For some aesthetic reasons, the name of every file and folder in your project repository should begin with a lower case letter.

### R023 - Positional and Keyword Argument
In python, there are two ways to pass an argument to a function/method as input. The first way is by position, its mean that arguments are passed in the function/method in the same order has they have been defined in the function definition. The second way is by keyword and it means that you will use a keyword to indicate which parameter should take the argument value. One could use both positional and keyword arguments in a function/method call but only if the positional arguments precede all keyword arguments. Also, you cannot skip a parameter between two positional arguments. 

```python
def get_mean_accuracy(recalls: Sequence[float], 
                      geometric_mean: bool = True) -> float:
    """
    Compute the mean accuracy according to the recalls of each class.

    :param recalls: A list of float that represent the recall of each class.
    :param geometric_mean: If true, the geometric mean is used. Else the euclidian mean will be used.
    :return: The mean accuracy.
    """
    if geometric_mean:
        return np.prod(recalls) ** (1 / len(recalls))
    else:
        return float(np.mean(recalls))
	

recall_list = [0.7, 0.6]

# Positonal arguments
geo_mean_recall = get_mean_accuracy(recall_list, True)

# Keyword arguments
geo_mean_recall = get_mean_accuracy(recalls=recall_list, geometric_mean=True)

# Positional and keyword arguments
geo_mean_recall = get_mean_accuracy(recall_list, geometric_mean=True)
```

#### Force keyword argument with *
Consider the method below. If you love risk and/or if you're an idiot, you could be tempted to only use positional argument when calling this function and since there are a lot of parameters that have the same type, you could easily make an error. A way to force the user to use keyword arguments is by using the * in the function definition. All parameters that come after the * would be keyword only parameters.
```
def fit(self,
	model: Union[NeuralNet, ResNet2D],
        trainset: Union[BrainDataset, RenalDataset],
        validset: Union[BrainDataset, RenalDataset],
	*,
        batch_size: int = 32,
        device: str = "cuda:0",
        eps: float = 1e-4,
        eta_min: float = 1e-4,
        gamma: float = 2.,
        grad_clip: float = 0,
        learning_rate: float = 1e-3,
        l2: float = 1e-4,
        mode: str = "standard",
        mom: float = 0.9,
        num_cumulated_batch: int = 1,
        num_epoch: int = 200,
        optim: str = "Adam") -> None:
```

### R024 - Regular Expressions

A Regular Expression is a sequence of characters that forms a search pattern to operate on strings, it defines a set of rules for the strings we want to match. RegEx are available in python through the [re](https://docs.python.org/3/library/re.html#module-re) module.

The [re](https://docs.python.org/3/library/re.html#module-re) module provides some functions to check if a string matches with a RE. 

| Function  | Description |
| ------------- | ------------- |
| *match()* | Check if the beginning of the string matches the RE. |
| *search()*  | Look for a match from any location of the string. |
| *sub()*  | Replace one or many matches with a specific string. |

Metacharacters are characters which have a special meaning in a RE:
| Metacharacter  | Description | RE | String |
| ------------- | ------------- | ------------- | ------------- |
| [ ] | A set of characters. | [a-z] | S**cience** |
| ^ | The beginning of the string. | ^M | **MEDomics Lab** |
| $ | The end of the string. | $b | **MEDomics Lab** |
| \| | Either or. | ^(u\|w) | **universe** |

A special sequence in a RE is a **\\** followed by a specific character and has a specific meaning:
| Special sequence  | Description | RE | String |
| ------------- | ------------- | ------------- | ------------- |
| \\A | Matches if the spcified characters are at the beginning of the string. | \\AHello | **Hello World** |
| \\d | Matches where the string contains digits. | \\d | It is **2022**! |
| \\S | Matches where the string does not contain white spaces. | \\S | **It matches with each character exepct the white space!** |
| \\Z | Matches if the spcified characters are at the end of the string. | \\Z(ing) | **It's matching** |

For a complete listing, refer to [the official documentation](https://docs.python.org/3/library/re.html#re.search).

Example:

```python
import re

txt = "It's raining on april 28th"

# Search for digits in the string 
x = re.search("\d", txt) # True

 # Replace each digit with 9
x = re.sub("\d", "9", txt) # x = "It's raining on april 99th"

```
