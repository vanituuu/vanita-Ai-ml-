# Python Lists

In Python, a list is a built-in data structure that can hold an ordered collection of items. Unlike arrays in some languages, Python lists are very flexible:

• Can contain duplicate items

• Mutable: items can be modified, replaced, or removed

• Ordered: maintains the order in which items are added

• Index-based: items are accessed using their position (starting from 0)

•Can store mixed data types (integers, strings, booleans, even other lists)

# Creating a List

Lists can be created in several ways, such as using square brackets, the list() constructor or by repeating elements. Let's look at each method one by one with example:

# 1. Using Square Brackets
We use square brackets [] to create a list directly.
```py
a = [1, 2, 3, 4, 5] # List of integers
b = ['apple', 'banana', 'cherry'] # List of strings
c = [1, 'hello', 3.14, True] # Mixed data types
​
print(a)
print(b)
print(c)
```
# 2. Using list() Constructor
We can also create a list by passing an iterable (like a tuple, string or another list) to the list() function.
```py
a = list((1, 2, 3, 'apple', 4.5))  
print(a)

b = list("GFG")
print(b)
a = list((1, 2, 3, 'apple', 4.5))  
print(a)
​
b = list("GFG")
print(b)
```
# 3. Creating List with Repeated Elements
We can use the multiplication operator * to create a list with repeated items.

```py
a = [2] * 5
b = [0] * 7
​
print(a)
print(b)
```
# Accessing List Elements
Elements in a list are accessed using indexing. Python indexes start at 0, so a[0] gives the first element. Negative indexes allow access from the end (e.g., -1 gives the last element).

```py
a = [10, 20, 30, 40, 50]
print(a[0])    
print(a[-1])
print(a[1:4])   # elements from index 1 to 3
```

# Adding Elements into List
We can add elements to a list using the following methods:

append(): Adds an element at the end of the list.

extend(): Adds multiple elements to the end of the list.

insert(): Adds an element at a specific position.

clear(): removes all items.

```py
a = []
​
a.append(10)  
print("After append(10):", a)  
​
a.insert(0, 5)
print("After insert(0, 5):", a) 
​
a.extend([15, 20, 25])  
print("After extend([15, 20, 25]):", a) 
​
a.clear()
print("After clear():", a)
```

# Updating Elements into List
Since lists are mutable, we can update elements by accessing them via their index.
```py
a = [10, 20, 30, 40, 50]
a[1] = 25 
print(a)
```
# Removing Elements from List
We can remove elements from a list using:

remove(): Removes the first occurrence of an element.

pop(): Removes the element at a specific index or the last element if no index is specified.

del statement: Deletes an element at a specified index.

```py
a = [10, 20, 30, 40, 50]
​
a.remove(30)  
print("After remove(30):", a)
​
popped_val = a.pop(1)  
print("Popped element:", popped_val)
print("After pop(1):", a) 
​
del a[0]  
print("After del a[0]:", a)
```

# Iterating Over Lists
We can iterate over lists using loops, which is useful for performing actions on each item.

```py
a = ['apple', 'banana', 'cherry']
for item in a:
    print(item)
```
