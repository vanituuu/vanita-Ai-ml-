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
**append()**:   Purpose	Adds a single element to the end of the list.extend()
**extend()**:	Adds multiple elements from an iterable to the end of the list.

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

# Add Any iterible
The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

**Example**
Add elements of a tuple to a list:
```py
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
```
# Slicing Items from a List

**Positive Indexing:** We can specify a range of positive indexes by specifying the start, end and step, the return value will be a new list. (default values for start = 0, end = len(lst) - 1 (last item), step = 1)
```py
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # it returns all the fruits
# this will also give the same result as the one above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the first index
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']
```
**Negative Indexing:** We can specify a range of negative indexes by specifying the start, end and step, the return value will be a new list.
```py
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # it returns all the fruits
orange_and_mango = fruits[-3:-1] # it does not include the last index,['orange', 'mango']
orange_mango_lemon = fruits[-3:] # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']
```

# Joining Lists
There are several ways to join, or concatenate, two or more lists in Python.

• Plus Operator (+)
# syntax
```py
list3 = list1 + list2
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables ) # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
```

Joining using extend() method The extend() method allows to append list in a list. See the example below.
# syntax
```py
list1 = ['item1', 'item2']
list2 = ['item3', 'item4', 'item5']
list1.extend(list2)
num1 = [0, 1, 2, 3]
num2= [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1) # Numbers: [0, 1, 2, 3, 4, 5, 6]
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers) # Integers: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits ) # Fruits and vegetables: ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']

```

# Sorting List Items
To sort lists we can use sort() method or sorted() built-in functions. The sort() method reorders the list items in ascending order and modifies the original list. If an argument of sort() method reverse is equal to true, it will arrange the list in descending order.

**sort():** this method modifies the original list

# syntax
```py
lst = ['item1', 'item2']
lst.sort()                # ascending
lst.sort(reverse=True)    # descending
```
**Example:**
```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)             # sorted in alphabetical order, ['banana', 'lemon', 'mango', 'orange']
fruits.sort(reverse=True)
print(fruits) # ['orange', 'mango', 'lemon', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages) #  [19, 22, 24, 24, 24, 25, 25, 26]

ages.sort(reverse=True)
print(ages) #  [26, 25, 25, 24, 24, 24, 22, 19]
sorted(): returns the ordered list without modifying the original list Example:

fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))   # ['banana', 'lemon', 'mango', 'orange']
# Reverse order
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = sorted(fruits,reverse=True)
print(fruits)     # ['orange', 'mango', 'lemon', 'banana']

```

# List Compherison
List comprehension is a concise and powerful way to create new lists by applying an expression to each item in an existing iterable (like a list, tuple or range). It helps you write clean, readable and efficient code compared to traditional loops.

Syntax
[expression for item in iterable if condition]

• Parameters:

– expression: operation or value to include in the new list.

– item: current element from the iterable.

– iterable: sequence like a list, tuple or range.

– if condition (optional): filter to include only items that satisfy the condition.

• Why Use List Comprehension?

– Cleaner code: Combines looping, filtering and transformation in one line.

– More readable: Avoids verbose loops and temporary variables.

– Faster execution: Often faster than equivalent for-loops.
```py
a = [1, 2, 3, 4, 5]
res = [val * 2 for val in a]
print(res)
```
**Explanation:** res = [val * 2 for val in a] use list comprehension to create a new list by doubling each number in a
```py
a = [1, 2, 3, 4, 5]
res = [val for val in a if val % 2 == 0]
print(res)
```

# Question
**You are given a list that contains integers. You need to print the elements of the list with a space between them.**
**Note: Do not add a new line at the end.**
```py
def printList(self,list):
    for i in range(len(list)):
        if i == len(list) - 1:
            print(list[i],end="")
        else:
            print(list[i],end="")
```
** Another way**
```py
def printList(self,list):
    print(*list,end="")

```






