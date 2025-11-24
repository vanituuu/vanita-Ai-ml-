# Python Operators


In Python programming, Operators in general are used to perform operations on values and variables.

Operators: Special symbols like -, + , * , /, etc.

Operands: Value on which the operator is applied.

Types of Operators in Python

Operators-in-python

# 1.Arithmetic Operators

Python Arithmetic operators are used to perform basic mathematical operations like addition, subtraction, multiplication and division.

Example:

# Declaring the variable at the top first

a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function - try to avoid overriding built-in functions
print(total) # if you do not label your print with some string, you never know where the result is coming from
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponentiation)


Let us start start connecting the dots and start making use of what we already know to calculate (area, volume,density, weight, perimeter, distance, force).

Example:

# Calculating area of a circle
radius = 10                                 # radius of a circle
area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')                         # Adding unit to the weight

# Calculate the density of a liquid
mass = 75 # in Kg
volume = 0.075 # in cubic meter
density = mass / volume # 1000 Kg/m^3


# 2. Assignment Operators
Assignment operators are used to assign values to variables. For example,

# assign 5 to x 
x = 5
Here, = is an assignment operator that assigns 5 to x.

Here's a list of different assignment operators available in Python.

Operator	Name	Example

=	Assignment Operator	a = 7

+=	Addition Assignment	a += 1 # a = a + 1

-=	Subtraction Assignment	a -= 3 # a = a - 3

*=	Multiplication Assignment	a *= 4 # a = a * 4

/=	Division Assignment	a /= 3 # a = a / 3

%=	Remainder Assignment	a %= 10 # a = a % 10

**=	Exponent Assignment	a **= 10 # a = a ** 10

Example 2: Assignment Operators

# assign 10 to a
a = 10

# assign 5 to b
b = 5 

# assign the sum of a and b to a
a += b      # a = a + b

print(a)

# Output: 15


# 3. Comparison Operators
In Python, Comparison (or Relational) operators compares values. It either returns True or False according to the condition.


a = 13
b = 33
​
print(a > b)

print(a < b)

print(a == b)

print(a != b)

print(a >= b)

print(a <= b)

print(len('mango') == len('avocado'))  # False

print(len('mango') != len('avocado'))  # True

print(len('mango') < len('avocado'))   # True

print(len('milk') != len('meat'))      # False

print(len('milk') == len('meat'))      # True

print(len('tomato') == len('potato'))  # True

print(len('python') > len('dragon'))   # False

In addition to the above comparison operator Python uses:

is: Returns true if both variables are the same object(x is y)

is not: Returns true if both variables are not the same object(x is not y)

in: Returns True if the queried list contains a certain item(x in y)

not in: Returns True if the queried list doesn't have a certain item(x in y)

print('1 is 1', 1 is 1)                   # True - because the data values are the same

print('1 is not 2', 1 is not 2)           # True - because 1 is not 2

print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string

print('B in Asabeneh', 'B' in 'Asabeneh') # False - there is no uppercase B

print('coding' in 'coding for all') # True - because coding for all has the word coding

print('a in an:', 'a' in 'an')      # True

print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

In Python, both is and == are used for comparison, but they serve different purposes:

== (Equality Operator) → Compares values of two objects.

is (Identity Operator) → Compares memory location of two objects.


a = [1,2,3]

b = [1,2,3]
​
print(a == b)  

print(a is b)

# is' operator

The is operator checks if two variables refer to the same object in memory, rather than just having equal values. It returns True only if both variables point to the exact same object in memory.

Example:

points to the same memory location as x

print(x is y)

x = [10, 20, 30]

y = x    # y points to the same memory location as x
​
print(x is y)

# == operator
The == operator checks if two objects contain the same values, regardless of whether they are stored in the same memory location.

Example:


a = [1, 2, 3]

b = [1, 2, 3]

print(a == b) # same values

a = [1, 2, 3]

b = [1, 2, 3]
​
print(a == b)

# 4. Logical Operators

Python Logical operators perform Logical AND, Logical OR and Logical NOT operations. It is used to combine conditional statements.

The precedence of Logical Operators in Python is as follows:

Logical not

logical and

logical or



a = True

b = False

print(a and b)

print(a or b)

print(not a)

# Example: Logical Operators (AND, OR, NOT) with generic variables

a, b, c = True, False, True
​
# AND: Both conditions must be True

if a and c:

    print("Both a and c are True (AND condition).")
​
# OR: At least one condition must be True

if b or c:

    print("Either b or c is True (OR condition).")
​
# NOT: Reverses the condition

if not b:

    print("b is False (NOT condition).")

# 5.Bitwise Operators

Python Bitwise operators act on bits and perform bit-by-bit operations. These are used to operate on binary numbers.

Bitwise Operators in Python are as follows:

Bitwise NOT

Bitwise Shift

Bitwise AND

Bitwise XOR

Bitwise OR



a = 10

b = 4

print(a & b)

print(a | b)

print(~a)

print(a ^ b)

print(a >> 2)

print(a << 2)

# 6. Ternary Operator
In Python, Ternary operators also known as conditional expressions are operators that evaluate something based on a condition being true or false. 

It simply allows testing a condition in a single line replacing the multiline if-else, making the code compact.

Syntax :  [on_true] if [expression] else [on_false] 




a, b = 10, 20

min = a if a < b else b

print(min)


