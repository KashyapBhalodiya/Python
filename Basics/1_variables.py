# Using Hash we can comment in Python

# For Multiline comments we used """ Multiline Comment """

# How to declare the variable in python?
# variablename = value

x = 5
print(x)

# Casting in python:
x = str(3)
y = int(3)
z = float(5)

print(type(x))
print(type(y))
print(type(z))

# In python we can assign the multiple values
a, b, c = 1, 2, 3
print(b)

# One value to multiple variables
a = b = c = "Orange"
print(a)

# Unpack the collection
variables = ['a', 2, 12.21]
p, q, r = variables
print(p)
print(q)
print(r)

# Global keyword
# To create a global variable inside a function you can use the global keyword

def myfun():
    global x
    x = "This is a global object"

myfun()
print(x)

# Built-In Data types:
"""
str, int, float, complex (1j), list, tuple, range (range(6)), dict, set, frozenset, bool, bytes, bytearray, memoryview, None
"""

# How to generate the random numbers in python
# Python doesn't have built-in function to create a random number but it has built-in module.

import random

# There is more method in random module
print(random.randrange(1, 10)) # Returns the random number specified range
print(random.shuffle(["apple","banana","orange"])) # Returns the sequence in a random order

# How to create mulitiline of string
str = """
This is a
multiline of
string
"""
print(str)
print(len(str)) # String length
print("of" in str) # Check string
print("of" not in str) # Check if not present string

# Slicing in string: You can return a range of characters by usingthe slice syntax

# The first character is starting in index 0.

s = "Hello World"
print(s[2:5])
print(s[:5])
print(s[:])
print(s[-5:-2])

# There is more methods for string
"""
capitalize, count, find, format, index, isalnum, isalpha, isascii, isdecimal, isdigit, isidentifier, isnumeric, join, isupper, islower, replace, 
"""
print(s.upper()) # Upper case
print(s.lower()) # Lower case
print(s.strip()) # Remove the white spaces
print(s.replace("H", "J")) # Replace string
print(s.split(",")) # Split the string

# String format
age = 30
txt = "My name is John and my age is {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# Python Escape Characters
"""
\' 
\\
\n
\r = It will start the next string in new line
\t
\b
\f
\ooo = Octal value (\123\123\523\232)
\xhh = hexadecimal value (\x45\x51\x12\x45)
"""

# Python Operators
"""
Arithmetic: +,-,*,/,%,**,//
Assignment: =, +=, -=, *=, /=, %=, //=, **=, &=, ?=, >>=, <==, ^=
Comparison: ==, !=, >, <, >=, <=
Logical: and, or, not
Identity: is, is not
Membership: in, not in
Bitwise: &, |, ^, ~, <<, >>
"""


