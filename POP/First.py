print("""
This is a python course for 
beginners
\n\n
""")

course = 'Python For Beginners'
print(course)
print(course[2])
print(course[-2])

print(course[0:3])
print(course[3:8])
print(course[0:])
print(course[2:])
print(course[:5])

another = course[:]
print(another)
print(another[1:-1])
print(another[5:-2])

print('\n\n')

## Formated String
first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder' # String concatination
msg = f'{first} [{last}] is a coder' # Formated String
print(message)
print(msg + '\n\n')

## Stirng methods
mukund = 'Computer Engineer'
print(len(mukund))
print(mukund.upper())
print(mukund.lower())
print(mukund.find('m'))
print(mukund.find('a'))
print(mukund.replace('Computer', 'IT'))
print('IT' in mukund)
print(mukund.title())
print('\n\n')

## Arithmetic Operations
# Search our python 3 math module
import math
from pydoc import tempfilepager
from tkinter import N
from tkinter.tix import Tree
from traceback import print_tb
from unicodedata import digit

from numpy import number, outer
print(round(12.12))
print(abs(-21))
print(math.ceil(2.3))
print(math.floor(2.3))
print('\n\n')

## If statements

is_hot = False
is_cold = False
if is_hot:
    print("It's a hot day")
elif is_cold:
    print("It's a cold day")
else:
    print("It's a lovely day")
print("\n\n")

## Logical operators

has_high_income = True
has_good_credit = True
if has_high_income and has_good_credit:
    print('Good')
else:
    print('Try to try will be success')

has_high_income = False
has_good_credit = False
if has_high_income or has_good_credit:
    print('Good')
else:
    print('Try to try will be success')

has_high_income = True
has_good_credit = False
if has_high_income and not has_good_credit:
    print('Good')
else:
    print('Try to try will be success')
print("\n\n")

## Comparison operators
temperature = 35
if temperature > 35:
    print("Hot day")
elif temperature == 35:
    print("Cool day")
else:
    print("Cold day")
print("\n\n")

## While loop
i = 1
while (i <= 5):
    print(i)
    i = i + 1
print("\n\n")

## For loop
for item in [1, 2, 3, 4]:
    print(item)
print("\n")
for item in range(10):
    print(item)
print("\n")
for item in range(5, 10):
    print(item)
print("\n")
for item in range(1, 10, 2):
    print(item)
print("\n")

prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f"Total: {total}\n\n")

## nested loops
for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")

numbers = [5, 3, 1, 3, 5]
for i in numbers:
    output = ''
    for count in range(i):
        output += 'x'
    print(output)
print("\n\n")

## list
names = ["Kashyap", "Yash", "Niraj", "Mukund", "Roy"]
print(names)
print(names[0])
print(names[-2])
print(names[2:4])

# Largest number in the list
numbers = [3, 6, 2, 1, 5, 9]
max = numbers[0]
for i in numbers:
    if i > max:
        max = i
print(max)
print("\n\n")

## Matrix representation

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][0])
matrix[0][0] = 10
print(matrix[0][0])
print("\n")
for row in matrix:
    for item in row:
        print(item)
print("\n\n")

## List methods
numbers = [5, 4, 1, 7, 2]
numbers.append(20)
print(numbers)
numbers.insert(0, 10)
print(numbers)
print(numbers.index(4)) # If number is not exist then value error occured
print(50 in numbers)
print(numbers.count(5))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
num = numbers.copy()
print(num)
numbers.clear()
print(numbers)
print('\n')
arr = [2, 2, 5, 5, 4, 3, 1, 2, 10]
unique = []
for i in arr:
    if i not in unique:
        unique.append(i)
print(unique)
print("\n\n")

## Tuples
numbers = (1, 2, 3, 4, 5)
print(numbers[0])

## Dictionary
customer = {
    "name" : "John Smith",
    "age" : 12, 
    "is_verified" : True
}
print(customer.get("birthdate", "Jan 1 1999"))
print(customer)
print(customer["name"])

message = input(">")
words = message.split(' ')
emojis = {
    ":)" : "smile",
    ":(" : "sad"
}
output = ''
for word in words:
    output += emojis.get(word, word)
print(output)
print("\n\n")
## Function
def greet_user():
    print("Good Morning")
greet_user()

def greet(name):
    print(f"Hi {name}")
greet("Raju")

def square(number):
    return number * number
square(3)
print("\n\n")
## Exceptions
try:
    age = int(input('Age: '))
    print(age)
except ValueError:
    print("Invalid value")

try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
except ZeroDivisionError:
    print('Not divisible by zero')
except ValueError:
    print("Invalid value")
print("\n\n")

## Classes
class Point:
    def move(self): # self is used to represent as object of the given class
        print("Move")
    def drop(self):
        print("draw")
# Create object
point1 = Point()
point1.move()
point1.drop()
point1.x = 12
print(point1.x)

## Constructors
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self): 
        print("Move")
    def drop(self):
        print("draw")
point2 = MyClass(10, 20)
print(point2.x)
print("\n\n")

# Excercise
class Person:
    def __init__(self, name):
        self.name = name
    def talk(self, name):
        print(f"Hello {self.name}")
p1 = Person("Niraj")
print(p1.name)
print("\n\n")

## Inheritance
class Mammal:
    def walk(self):
        print("Walk")

class Dog(Mammal):
    def bark(self):
        print("Bark")

class Cat(Mammal):
    pass

dog1 = Dog()
dog1.bark()
cat1 = Cat()
cat1.walk()
print('\n\n')

## How to create packages in python
# Go to Ecommerce_Package

## Generating Random values
import random

for i in range(3):
    print(random.random())

members = ['John', 'Mary', 'Bob', 'Mosh']
leader = random.choice(members)
print(leader)
print("\n\n")

## Files and Directories
# pip install openpyxl (read for excel files)
from pathlib import Path

path = Path("Ecommerce_Package")
print(path.exists())
for file in path.glob('*.py'):
    print(file)

import openpyxl as xl
wb = xl.load_workbook('transactions.xlsx')
sheet = wb['Sheet1']
cell = sheet.cell(1, 1)
print(cell.value)


























































