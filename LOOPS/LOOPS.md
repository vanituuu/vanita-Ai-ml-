# Loops in Python - For, While and Nested Loops

Loops in Python are used to repeat actions efficiently. The main types are For loops (counting through items) and While loops (based on conditions).Python programming language also provides the following types of two loops:

1.while loop
2.for loop


# While Loop
We use the reserved word while to make a while loop. It is used to execute a block of statements repeatedly until a given condition is satisfied. When the condition becomes false, the lines of code after the loop will be continued to be executed.

  # syntax
while condition:
    code goes here


```python
cnt = 0
while (cnt < 3):
    cnt = cnt + 1
    print("Hello Geek")
```
**Infinite While Loop**
If we want a block of code to execute infinite number of times then we can use the while loop in Python to do so.

Code given below uses a 'while' loop with the condition "True", which means that the loop will run infinitely until we break out of it using "break" keyword or some other logic.

```python
while (True):
    print("Hello Geek")
```
Note: It is suggested not to use this type of loop as it is a never-ending infinite loop where the condition is always true and we have to forcefully terminate the compiler.

# Break ,Continue and else statment
Break: We use break when we like to get out of or stop the loop.
# syntax
while condition:
    code goes here
    if another_condition:
        break

**Example**
Exit the loop when i is 3:

```python
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
```

Continue: With the continue statement we can skip the current iteration, and continue with the next:
**Example**
Continue to the next iteration if i is 3:

```py
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
```
# The else Statement
With the else statement we can run a block of code once when the condition no longer is true:

**Example**

Print a message once the condition is false:
```py
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
```

# For Loop

For loops is used to iterate over a sequence such as a list, tuple, string or range. It allow to execute a block of code

repeatedly, once for each item in the sequence.

# syntax
for iterator in lst:
    code goes here

**Example**
```py
n = 4
for i in range(0, n):
    print(i)
```
**Example:**
Iterating Over List, Tuple, String and Dictionary Using for Loops in Python.
```py

li = ["Hello ", "Good","Morning"]
for x in li:
    print(x)
    
tup = ("Morning", "Afternoon", "Evening")
for x in tup:
    print(x)
    
s = "abc"
for x in s:
    print(x)
    
d = dict({'x':123, 'y':354})
for x in d:
    print("%s  %d" % (x, d[x]))
    
set1 = {10, 30, 20}
for x in set1:
    print(x)

language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])
```



