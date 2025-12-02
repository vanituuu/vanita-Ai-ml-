# Variables

Variables store data in a computer memory. Mnemonic variables are recommended to use in many programming languages. A mnemonic variable is a variable name that can be easily remembered and associated. A variable refers to a memory address in which data is stored. Number at the beginning, special character, hyphen are not allowed when naming a variable. A variable can have a short name (like x, y, z), but a more descriptive name (firstname, lastname, age, country) is highly recommended.

**Python Variable Name Rules**

A variable name must start with a letter or the underscore character

A variable name cannot start with a number

A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )

Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME) are different variables)

Here are some example of valid variable names:


firstname

lastname

age

country

city

first_name

last_name

capital_city

_if # if we want to use reserved word as a variable

year_2021

year2021

current_year_2021

birth_year

num1

num2

Invalid variables names

first-name

first@name

first$name

num-1


# Assigning the Same Value

Python allows assigning the same value to multiple variables in a single line, which can be useful for initializing variables with the same value.

```py
a = b = c = 100
print(a, b, c) 
```
Type Casting a Variable

Type casting refers to the process of converting the value of one data type into another. Python provides several built-in functions to facilitate casting, including int(), float() and str() among others.

Basic Casting Functions

int(): Converts compatible values to an integer.

float(): Transforms values into floating-point numbers.

str(): Converts any data type into a string.
```py
s = "10"  
n = int(s) 
cnt = 5
f = float(cnt)  
age = 25
s2 = str(age)  

print(n)  

```

Getting the Type of Variable

In Python, we can determine the type of a variable using the type() function. This built-in function returns the type of the object passed to it.

```py
n = 42

f = 3.14

s = "Hello, World!"

li = [1, 2, 3]

d = {'key': 'value'}

bool = True

print(type(n))   

print(type(f)) 

print(type(s)) 

print(type(li)) 

print(type(d))   

print(type(bool))

print(f)

print(s2)  

```

# 1.Swapping Two Variables
 
Using multiple assignments, we can swap the values of two variables without needing a temporary variable.

``py
a, b = 5, 10

a, b = b, a

print(a, b)  
```

# 2. Counting Characters in a String

Assign the results of multiple operations on a string to variables in one line.

```py
word = "Python"

length = len(word)

print("Length of the word:", length) 

```

**Delete a Variable Using del Keyword**

We can remove a variable from the namespace using the del keyword. This deletes the variable and frees up the memory it was using.

```py
x = 10
print(x) 
del( x)
```
# Trying to print x after deletion will raise an error
# print(x)  # Uncommenting this line will raise NameError: name 'x' is not defined
del x removes the variable x from memory.
After deletion, trying to access the variable x results in a NameError indicating that the variable no longer exists.


[Introduction](introduction/intro.md)
