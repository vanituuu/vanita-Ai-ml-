# Python Tuples

A tuple in Python is an immutable ordered collection of elements.

-Tuples are similar to lists, but unlike lists, they cannot be changed after their creation (i.e., they are immutable).
-Tuples can hold elements of different data types.
-The main characteristics of tuples are being ordered, heterogeneous and immutable.

# Creating a Tuple
A tuple is created by placing all the items inside parentheses (), separated by commas. A tuple can have any number of items and they can be of different data types.
**Example**
```py
tup = ()
print(tup)
​
# Using String
tup = ('Geeks', 'For')
print(tup)
​
# Using List
li = [1, 2, 4, 5, 6]
print(tuple(li))
​
# Using Built-in Function
tup = tuple('Geeks')
print(tup)

# Creating a Tuple with repetition
tup1 = ('Geeks',) * 3
print(tup1)
​
# Creating a Tuple with the use of loop
tup = ('Geeks')
n = 5
for i in range(int(n)):
    tup = (tup,)
    print(tup)
```



# licing tuples
We can slice out a sub-tuple by specifying a range of indexes where to start and where to end in the tuple, the return value will be a new tuple with the specified items.

Range of Positive Indexes
```py
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[0:4]         # all items
all_items = tpl[0:]         # all items
middle_two_items = tpl[1:3]  # does not include item at index 3
fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]    # all items
all_fruits= fruits[0:]      # all items
orange_mango = fruits[1:3]  # doesn't include item at index 3
orange_to_the_rest = fruits[1:]
```
# Range of Negative Indexes

# Syntax
```py
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[-4:]         # all items
middle_two_items = tpl[-3:-1]  # does not include item at index 3 (-1)
fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]    # all items
orange_mango = fruits[-3:-1]  # doesn't include item at index 3
orange_to_the_rest = fruits[-3:]
```
# Changing Tuples to Lists
We can change tuples to lists and lists to tuples. Tuple is immutable if we want to modify a tuple we should change it to a list.
```py
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')
```

# Checking an Item in a Tuple
We can check if an item exists or not in a tuple using in, it returns a boolean.
```py
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
'item2' in tpl # True
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment
```
# Joining Tuples
We can join two or more tuples using + operator
```py
# syntax
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
```
# Deleting Tuples
It is not possible to remove a single item in a tuple but it is possible to delete the tuple itself using del.
```py
# syntax
tpl1 = ('item1', 'item2', 'item3')
del tpl1
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits
```
# Tuple Unpacking with Asterisk (*)
In Python, the " * " operator can be used in tuple unpacking to grab multiple items into a list. This is useful when you want to extract just a few specific elements and collect the rest together.
```py

tup = (1, 2, 3, 4, 5)
​
a, *b, c = tup
​
print(a) 
print(b) 
print(c)
```
