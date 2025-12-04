# String

In Python, a string is a sequence of characters enclosed in quotes. It can include letters, numbers, symbols or spaces. Since Python has no separate character type, even a single character is treated as a string with length one. Strings are widely used for text handling and manipulation.

**Example**

```py
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

letter = 'V'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be made using a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "Hello everyone.I am vanita"
print(sentence)
```

# Multiline Strings

You can assign a multiline string to a variable by using three quotes:

**Example**

You can use three double quotes:
```py
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
```
# Escape Sequences in Strings
In Python and other programming languages \ followed by a character is an escape sequence. Let us see the most common escape characters:

\n: new line
\t: Tab means(8 spaces)
\\: Back slash
\': Single quote (')
\": Double quote (")
Now, let us see the use of the above escape sequences with examples.
```py
print('I hope everyone is enjoying the Python notes.\nAre you ?') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces 
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote

# output
I hope every one is enjoying the Python Challenge.
Are you ?
Days	Topics	Exercises
Day 1	5	    5
Day 2	6	    20
Day 3	5	    23
Day 4	1	    35
This is a backslash  symbol (\)
In every programming language it starts with "Hello, World!"
```

# String Slicing

Slicing is a way to extract a portion of a string by specifying the start and end indexes. The syntax for slicing is string[start:end], where start starting index and end is stopping index (excluded).

**Example:** In this example we are slicing through range and reversing a string.
```py
s = "GeeksforGeeks"
print(s[1:4])    # characters from index 1 to 3
print(s[:3])     # from start to index 2
print(s[3:])     # from index 3 to end
print(s[::-1])   # reverse string
```
# String Iteration
Strings are iterable; you can loop through characters one by one.

**Example:** Here, it print each character on its own line.
```py
s = "Python"
for char in s:
    print(char)
```

# String Immutability

Strings are immutable, which means that they cannot be changed after they are created. If we need to manipulate strings then we can use methods like concatenation, slicing or formatting to create new strings based on original.

**Example:**
In this example we are changing first character by building a new string.
```py
s = "geeksforGeeks"
s = "G" + s[1:]   # create new string
print(s)
s = "geeksforGeeks"
s = "G" + s[1:]   # create new string
print(s)
```
# Updating a String

As strings are immutable, “updates” create new strings using slicing or methods such as replace().

**Example:** This code fix the first letter and replace a word.
```py
s = "hello geeks"
s1 = "H" + s[1:]                   # update first character
s2 = s.replace("geeks", "GeeksforGeeks")  # replace word
print(s1)
print(s2)
```

# Formatting Strings
Python provides several ways to include variables inside strings.

# 1. Using f-strings

The simplest and most preferred way to format strings is by using f-strings.

**Example:** Embed variables directly using {} placeholders.
```py
name = "Alice"
age = 22
print(f"Name: {name}, Age: {age}"
```

# 2. Using format()

Another way to format strings is by using format() method.

**Example:** Use placeholders {} and pass values positionally.
```py
s = "My name is {} and I am {} years old.".format("Alice", 22)
print(s)
```

# String Membership Testing

in keyword checks if a particular substring is present in a string.

**Example:** Here, we are testing for the presence of substrings.
```py
s = "GeeksforGeeks"
print("Geeks" in s)
print("GfG" in s)
s = "GeeksforGeeks"
print("Geeks" in s)
print("GfG" in s)
```
# Reversing a String
We can easily reverse strings in python.

```py
greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH
```

# Skipping Characters While Slicing

It is possible to skip characters while slicing by passing step argument to slice method.

```py
language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto
```
# String Methods
There are many string methods which allow us to format strings. See some of the string methods in the following example:

• capitalize(): Converts the first character of the string to capital letter
```py
challenge = 'hello good morning'
print(challenge.capitalize())
```
• count(): returns occurrences of substring in string, count(substring, start=.., end=..). The start is a starting indexing for counting and end is the last index to count.
```py
challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1, 
print(challenge.count('th')) # 2`
```

• endswith(): Checks if a string ends with a specified ending
```py
challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False
```
• expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument
```py
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'
```
• find(): Returns the index of the first occurrence of a substring, if not found returns -1
```py
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0
```
• rfind(): Returns the index of the last occurrence of a substring, if not found returns -1
```py
challenge = 'thirty days of python'
print(challenge.rfind('y'))  # 16
print(challenge.rfind('th')) # 17
```
• format(): formats string into a nicer output
```py
first_name = 'Vanita'
last_name = 'Kumari'
age = 124
job = 'student'
country = 'India'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, age, job, country)
print(sentence) 

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result) # The area of a circle with radius 10 is 314
```
• islower(): Checks if all alphabet characters in the string are lowercase
```py
challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False
```
• isupper(): Checks if all alphabet characters in the string are uppercase
```py
challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True
```
• join(): Returns a concatenated string
```py
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'
```
• strip(): Removes all given characters starting from the beginning and end of the string
```py
challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth')) # 'irty days of py'
```
• replace(): Replaces substring with a given string
```py
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'
```
• split(): Splits the string, using given string or space as a separator
```py
challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']
```
• title(): Returns a title cased string
```py
challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python
```
• swapcase(): Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
```py
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON
```
