# Conditional Statements in Python

Conditional statements in Python are used to execute certain blocks of code based on specific conditions. These statements help control the flow of a program, making it behave differently in different situations.

**If Conditional Statement**

If statement is the simplest form of a conditional statement. It executes a block of code if the given condition is true.

 #syntax
 
if condition:
    this part of code runs for truthy conditions

**Example**
```python
age = 20
if age >= 18:
    print("Eligible to vote.")
```

**Short Hand**
#syntax

• code if condition 
```python
age=20
if age>=18 : print("Eligible to vote.")
```
# If else Conditional Statement

If Else allows us to specify a block of code that will execute if the condition(s) associated with an if or elif statement evaluates to False. Else block provides a way to handle all other cases that don't meet the specified conditions.

#syntax

if condition:
    this part of code runs for truthy conditions
else:
     this part of code runs for false conditions
     
**Example**
```Python
age = 10
if age <= 12:
    print("Travel for free.")
else:
    print("Pay for ticket.")
```
**Short Hand**

#syntax

code if condition else code

age = 20
result = "Eligible for vote" if age>=18 else "Not eligible for vote"
print("result is",result)


# elif Statement

elif statement in Python stands for "else if." It allows us to check multiple conditions, providing a way to execute different blocks of code based on which condition is true. The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

**Example**
```python
age = 25

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")
```

# Nested if..else Conditional Statement
Nested if..else means an if-else statement inside another if statement. We can use nested if statements to check conditions within conditions. You can have if statements inside if statements. 

**Example**
```python
age = 70
is_member = False

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")
```

We can avoid writing nested condition by using logical operator and.

If Condition and Logical Operators

#syntax

if condition and condition:
    code
    
**Example:**

a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')
    
**If and Or Logical Operators**

#syntax

if condition or condition:
    code
Example:

user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')


