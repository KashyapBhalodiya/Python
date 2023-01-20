# PIP: It is a package manager of python packages.
# Package: It contains all the files you need a module.
# Module: Modules are Python code libraries you can include in your project.

# pip --version
# pip install versionName
# pip uninstall versionName
# pip list (List out all the packages)

# Python Try Except:
"""
The try block lets you test a block of code for errors.
The except block lets you handle the error.
The else block lets you execute code when there is no error.
The finally block lets you execute code, regardless of the result of the try- and except blocks.
"""

# Exception handling: When an error occures as we call it python will normally stop and generate an error message.

try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
  print("Something went wrong when opening the file")


x = -1
# raise keyword is used to raise an exception
# if x < 0:
#     raise Exception("Sorry, no numbers below zero")

# x = "hello"
# if not type(x) is int:
#   raise TypeError("Only integers are allowed")


# String formatting:
price = 49
txt = "The price is {} dollars"
print(txt.format(price))

"""
:<		Left aligns the result (within the available space)
:>		Right aligns the result (within the available space)
:^		Center aligns the result (within the available space)
:=		Places the sign to the left most position
:+		Use a plus sign to indicate if the result is positive or negative
:-		Use a minus sign for negative values only
: 		Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
:,		Use a comma as a thousand separator
:_		Use a underscore as a thousand separator
:b		Binary format
:c		Converts the value into the corresponding unicode character
:d		Decimal format
:e		Scientific format, with a lower case e
:E		Scientific format, with an upper case E
:f		Fix point number format
:F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)
:g		General format
:G		General format (using a upper case E for scientific notations)
:o		Octal format
:x		Hex format, lower case
:X		Hex format, upper case
:n		Number format
:%		Percentage format

string.format(value1, value2, ...)
"""

txt = "The price is {:.2f} dollars"

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
