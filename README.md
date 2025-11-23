# Python Full Course

Welcome to my **Python Full Course**.  
This repository contains complete Python notes and code examples for beginners.

---

## 📘 Topics Covered

### 1️⃣ Introduction to Python  
- What is Python    
- Running first program  

### 2️⃣ Variables  
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
In Python there are several types of data types. Let us get started with the most common ones. Different data types will be covered in detail in other sections. For the time being, let us just go through the different data types and get familiar with them. You do not have to have a clear understanding now.

Number
Integer: Integer(negative, zero and positive) numbers Example: ... -3, -2, -1, 0, 1, 2, 3 ...
Float: Decimal number Example ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...
Complex Example 1 + j, 2 + 4j
String
A collection of one or more characters under a single or double quote. If a string is more than one sentence then we use a triple quote.

Example:

'Asabeneh'
'Finland'
'Python'
'I love teaching'
'I hope you are enjoying the first day of 30DaysOfPython Challenge'
Booleans
A boolean data type is either a True or False value. T and F should be always uppercase.

Example:

    True  #  Is the light on? If it is on, then the value is True
    False # Is the light on? If it is off, then the value is False
List
Python list is an ordered collection which allows to store different data type items. A list is similar to an array in JavaScript.

Example:

[0, 1, 2, 3, 4, 5]  # all are the same data types - a list of numbers
['Banana', 'Orange', 'Mango', 'Avocado'] # all the same data types - a list of strings (fruits)
['Finland','Estonia', 'Sweden','Norway'] # all the same data types - a list of strings (countries)
['Banana', 10, False, 9.81] # different data types in the list - string, integer, boolean and float
Dictionary
A Python dictionary object is an unordered collection of data in a key value pair format.

Example:

{
'first_name':'Asabeneh',
'last_name':'Yetayeh',
'country':'Finland', 
'age':250, 
'is_married':True,
'skills':['JS', 'React', 'Node', 'Python']
}
Tuple
A tuple is an ordered collection of different data types like list but tuples can not be modified once they are created. They are immutable.

Example:

('Asabeneh', 'Pawel', 'Brook', 'Abraham', 'Lidiya') # Names
('Earth', 'Jupiter', 'Neptune', 'Mars', 'Venus', 'Saturn', 'Uranus', 'Mercury') # planets
Set
A set is a collection of data types similar to list and tuple. Unlike list and tuple, set is not an ordered collection of items. Like in Mathematics, set in Python stores only unique items.

In later sections, we will go in detail about each and every Python data type.

Example:

{2, 4, 3, 5}
{3.14, 9.81, 2.7} # order is not important in set

