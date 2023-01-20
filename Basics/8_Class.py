# Class: it is a blueprint for creating object OR object constructor
# Object: it is a instance of the class.
# Almost everything in python is an object with its properties and methods.

class myClass:
    x = 5
# Creating one object
p1 = myClass()
print(p1.x)

# __init__(): When the class is being initiated it is always executed and create a new object
# Constructor: create the instance of class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
p1 = Person("Jay", 20)
print(p1)
print(p1.name)
print(p1.age)

# __str__(): returns the string representation of the object.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})" # This is a f string formatting

p1 = Person("John", 36)
print(p1)

# f string formatting:
name = "Eric"
age = 74
f"Hello, {name}. You are {age}."

import datetime
today = datetime.datetime.today()
print(f"{today:%B %d, %Y}")

# Object Methods:
# self: It is a reference to the current instance of the class and is used to access variables that belong to the class
### Note: It has the first parameter of any function in the class. Also we can write anything instead of self.

class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age
    def myfunc(abc):
        print("Hello my name is " + abc.name)
p1 = Person("John", 36)
p1.myfunc()

# Modify object
p1.age = 40

# Delete the object properties
del p1.age
del p1 # Delete the object

# If we won't to create a class but not write anything in then write the pass keyword it will executed code without the error
class hello:
    pass

