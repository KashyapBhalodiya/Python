# Inheritance:
"""
Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.

"""

# Creating the parent class:
class person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def printName(self):
        print(self.fname + " " + self.lname)

x = person("John", "Doe")
x.printName()

# Creating the child class:
# Create a class named Student, which will inherit the properties and methods from the Person class:
class Student(person):
    pass

y = Student("Mike", "Olsen")
y.printName()

class Student(person):
    # When we added __init__() function the child class will no longer inherited the parent's __init__() function
    # The child's __init__() function overrides the inheritance of the parent's __init__() function.
    def __init__(self, fname, lname):
        # To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function
        person.__init__(self, fname, lname)
        # Now we have successfully added the __init__() function, and kept the inheritance of the parent class, 
        # and we are ready to add functionality in the __init__() function.

# Super() function: It will make the child class inherite all the methods and properties from its parent
class Student(person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        # By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the 
        # methods and properties from its parent.

        # Add the properties
        self.graduationyear = 2019

x = Student("Mike", "Olsen")
print(x.graduationyear)
    
class Student(person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

x = Student("Mike", "Olsen", 2019)

# Add the methods:
class Student(person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.fname, self.lname, "to the class of", self.graduationyear)
    # If you add a method in the child class with the same name as a function in the parent class, 
    # the inheritance of the parent method will be overridden.

x = Student("Mike", "Olsen", 2019)
x.welcome()
