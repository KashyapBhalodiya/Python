# If - else: 
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# Short hand operation in python
print("A") if a > b else print("B")
print("A") if a > b else print("=") if a == b else print("B")

# pass statement:
# if statements cannot be empty, but if you for some reason have an if statement with no content, 
# put in the pass statement to avoid getting an error.

if b > a:
    pass


for x in range(2, 6):
    print(x)

for x in range(2, 30, 3):
    print(x)

# Function:
"""
It is a block of code which only runs when it is called.
You can pass data, known as parameters into a function.
A function can return data as a result.

Arguments:
Information can be passed into functions as arguments.
Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

"""

def my_function():
    print("Hello from a function")
my_function()

def my_function(fname):
    print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Arbitary arguments 
# If you don;t know how many arguments passed into your function add a * before the parameter name in the function definition.

def my_function(*kids):
    print("Yougest once is: " + kids[3])
my_function("A", "B", "C", "D", "E")

# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, 
# add two asterisk: ** before the parameter name in the function definition.

def my_function(**kid):
    print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

# Keyword argument
# You can also send arguments with the key=value pairs
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Lambda in python
# It is a small anonymous function. (function without the name)
# A lambda function can take any number of arguments, but can only have one expression.
# syntax: lambda argument : expression

x = lambda a : a + 10
print(x(5))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

def myFunction(n):
    return lambda a : a * n
mydoubler = myFunction(2)
print(mydoubler(11))

