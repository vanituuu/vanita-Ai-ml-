# Python Sets

Python set is an unordered collection of multiple items having different datatypes. In Python, sets are mutable, unindexed and do not contain duplicates. The order of elements in a set is not preserved and can change.

-Can store None values.
-Implemented using hash tables internally.
-Do not implement interfaces like Serializable or Cloneable.
-Python sets are not inherently thread-safe; synchronization is needed if used across threads.
-Creating a Set in Python
In Python, the most basic and efficient method for creating a set is using curly braces.
```py

set1 = {1, 2, 3, 4}
print(set1)
```
# Using the set() function
Python Sets can be created by using the built-in set() function with an iterable object or a sequence by placing the sequence inside curly braces, separated by a 'comma'.

Note: A Python set cannot contain mutable types such as lists or dictionaries, because they are unhashable.
```py
set1 = set()
print(set1)
​
set1 = set("GeeksForGeeks")
print(set1)
​
# Creating a Set with the use of a List
set1 = set(["Geeks", "For", "Geeks"])
print(set1)
​
# Creating a Set with the use of a tuple
tup = ("Geeks", "for", "Geeks")
print(set(tup))
​
# Creating a Set with the use of a dictionary
d = {"Geeks": 1, "for": 2, "Geeks": 3}
print(set(d))
```
# Checking Subset and Super Set
A set can be a subset or super set of other sets:

Subset: issubset()
Super set: issuperset
```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True
Example:

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers) # False, because it is a super set
whole_numbers.issuperset(even_numbers) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.issubset(dragon)     # False
```
