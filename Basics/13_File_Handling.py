# File Handling: It is an important part of any web application.
# Python has several functions for creating, reading, updating, and deleting files.

"""
The key function for working with files in Python is the open() function.
The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists

"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
"""
# Make sure the file is exist or else we will get error
f = open("13_DemoFile.txt", "r")

# The open() function returns a file object, which has a read() method for reading the content of the file
print(f.read())
print(f.read(5)) # Specifies how many characters are print

# You can return one line by using the readline() method
print(f.readline())

# By looping through the lines of the file, you can read the whole file, line by line
for x in f:
    print(x)

# Good practice to always close the file when you are done with it.
f.close()

# To write to an existing file, you must add a parameter to the open() function:
    # "a" - Append - will append to the end of the file
    # "w" - Write - will overwrite any existing content

f = open("13_DemoFile.txt", "a")
f.write("Now the file has more content!")
f.close()
#open and read the file after the appending:
f = open("13_DemoFile.txt", "r")
print(f.read())


f = open("13_DemoFile.txt", "w")
f.write("Now the file has more content!")
f.close()
f = open("13_DemoFile.txt", "r")
print(f.read())

# Create a New File
# To create a new file in Python, use the open() method, with one of the following parameters:
    # "x" - Create - will create a file, returns an error if the file exist
    # "a" - Append - will create a file if the specified file does not exist
    # "w" - Write - will create a file if the specified file does not exist

# f = open("myfile.txt", "x") new empty file is created
# f = open("myfile.txt", "w") create a new file if it does not exist

# Delete a File
# To delete a file, you must import the OS module, and run its os.remove() function:
import os
# os.remove("myfile.txt")

# Check if File exist:
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")

# Delete the folder

# os.rmdir("myfolder") # You can only remove empty folders.
