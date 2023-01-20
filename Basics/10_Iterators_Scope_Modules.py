# Iterators:
# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon
# There is two methods: __iter__() and __next__()

# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
# All these objects are iter() method which is used to get an iterator

mytuple = ("apple", "banana", "cherry")
myitr = iter(mytuple)
print(next(myitr))
print(next(myitr))
print(next(myitr))

mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# Create an iterator:
# To create an object of iterator you have to implement the method __iter__() and __next__() to your object.

# __iter__() must always return the iterator object itself.
# __next__() return the next item in the sequence.

class MyNumber:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumber()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# How we can stop the iteration: using StopIteration

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)

# Python Scope
# A variable is only available from inside the region it is created. this is called scope

# Local and global scope we are talking in the python scope
# What we have do if we created the global scope inside the method so we can use the global keyword for that purpose.
def myfunc():
    global x
    x = 300

myfunc()
print(x)

# Modules:
# Consider a module to be the sane as a code library.
# A file contains the set of functions you to include in your application.

# How to use it our module?
# Import our file and then we can use those file functionality.

# import 10_1_module

# a = 10_1_module.add(12, 10)
# print(a)

# Re-Naming a module:

# import 10_1_module as x

# a = x.add(12, 10)
# print(a) 

# Built-in modules;
import platform
x = platform.system()
print(x)

y = dir(platform)
print(x)

# Import from module
# from 10_1_module import sub

# print(sub(12, 10))
