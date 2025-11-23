# Python Full Course

Welcome to my **Python Full Course**.  
This repository contains complete Python notes and code examples for beginners.

---

## 📘 Topics Covered

### 1️⃣ Introduction
- [Introduction](introduction/Intro.md)
- What is Python    
- Running first program  

### 2️⃣ Variables 
- [Variables](Variable/Variable.md)
- Rules for variables  
- Assigning values  
- Multiple assignment  

### 3️⃣ Data Types  
- int, float, string  
- list, tuple, dict  
- type() function  

### 4️⃣ Conditions  
- if  
- if-else  
- elif  
- nested conditions  

### 5️⃣ Loops  
- for loop  
- while loop  
- break  
- continue  

### 6️⃣ Functions  
- Defining functions  
- Arguments  
- Return values  
- Default parameters  

### 7️⃣ Lists  
- Adding items  
- Removing items  
- Looping lists  

### 8️⃣ Tuples  
- Immutable sequences  

### 9️⃣ Dictionaries  
- Key-value pairs  
- Adding, updating, deleting  

---
Introduction:

Python is one of the most popular programming languages. It’s simple to use, packed with features and supported by a wide range of libraries and frameworks. Its clean syntax makes it beginner-friendly. It is easy to learn and use

A high-level language, used in web development, data science, automation, AI and more.
Known for its readability, which means code is easier to write, understand and maintain.
Backed by library support, so we don’t have to build everything from scratch


Comments:
Comments play a crucial role in enhancing code readability and allowing developers to leave notes within their code. In Python, any text preceded by a hash (#) symbol is considered a comment and is not executed when the code runs.

Example: Single Line Comment

    # This is the first comment
    # This is the second comment
    # Python is eating the world
Example: Multiline Comment

Triple quote can be used for multiline comment if it is not assigned to a variable

"""This is multiline comment
multiline comment takes multiple lines.
python is eating the world
"""

Indentation in Python:

In Python, Indentation is used to define blocks of code. It tells the Python interpreter that a group of statements belongs to a specific block. All statements with the same level of indentation are considered part of the same block. Indentation is achieved using whitespace (spaces or tabs) at the beginning of each line. The most common convention is to use 4 spaces or a tab, per level of indentation.

Data types

Data types in Python are a way to classify data items. They represent the kind of value, which determines what operations can be performed on that data. Since everything is an object in Python programming, Python data types are classes and variables are instances (objects) of these classes.

The following are standard or built-in data types in Python:

Numeric: int, float, complex
Sequence Type: string, list, tuple
Mapping Type: dict
Boolean: bool
Set Type: set, frozenset
Binary Types: bytes, bytearray, memoryview
Complex Example 1 + j, 2 + 4j


String

Strings in Python can be created using single quotes, double quotes or even triple quotes. We can access individual characters of a String using index.
Example:

'Python'

s = 'Welcome to the Python'
print(s)

Booleans


A boolean data type is either a True or False value. T and F should be always uppercase.

Example:

    True  #  Is the light on? If it is on, then the value is True
    False # Is the light on? If it is off, then the value is False
List
Python list is an ordered collection which allows to store different data type items.Lists in Python can be created by just placing sequence inside the square brackets[].

Example:

# Empty list
a = []

# list with int values
a = [1, 2, 3]
print(a)

# list with mixed values int and String
b = ["Welcome", "Everybody", 4, 5]
print(b)


Tuple

Tuple is an ordered collection of Python objects. The only difference between a tuple and a list is that tuples are immutable. Tuples cannot be modified after it is created.
Example:
# initiate empty tuple
tup1 = ()

tup2 = ('Morning', 'For')
print("\nTuple with the use of String: ", tup2)


Set

In Python Data Types, Set is an unordered collection of data types that is iterable, mutable, and has no duplicate elements. The order of elements in a set is undefined though it may consist of various elements.

Example:
set1 = set(["Morning", "and", "Morning"]) #Duplicates are removed automatically
print(set1) 

# loop through set
for i in set1:
   print(i, end=" ") #prints elements one by one
  
# check if item exist in set   
print("Morning" in set1)

Dictionary


A dictionary in Python is a collection of data values.A Dictionary holds a key: value pair. Key-value is provided in dictionary to make it more optimized. Each key-value pair in a Dictionary is separated by a colon : , whereas each key is separated by a ‘comma’.

Example:

# initialize empty dictionary
d = {}

d = {1: 'Good Morning', 2: 'All', 3: 'of you'}
print(d)

# creating dictionary using dict() constructor
d1 = dict({1: 'Good Morning', 2: 'All', 3: ''})
print(d1)
