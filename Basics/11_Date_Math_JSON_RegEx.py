# Dates: We can import a module named datetime to work with dates as date objects.

import datetime

# Contains year, month, day, hour, minute, second and microsecond
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A")) # Print the day

# Creating date objects
# datetime() class requires three parameters to create a date: yaer, month, day
# Other default values are 0 (None for timezone)
x = datetime.datetime(2022, 5, 17)
print(x)

# strftime() method:
# Formatting date objects into readable strings
x = datetime.datetime(2018, 7, 1)
print(x.strftime("%B"))

# In strftime method we have many reference of format codes
# Like: %a, %A, %m, %H, %S, %Z

# Python Math: allpws mathematical tasks on numbers
import math

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)
print(abs(-4.12))
print(pow(2, 3))

print(math.sqrt(64))
print(math.ceil(1.4)) # rounds a number upwards to its nearest integer
print(math.floor(1.4)) # rounds a number downwards to its nearest integer
print(math.pi)

# In math module there is many modules like cost, dist, gcd, isqrtradians
print(math.gcd(3, 6)) # Greatest common factor number that divides them

# Python JSON
# It is a syntax for storing and exchanging data
# JSON is text written with JS object notation

import json
# Convert from JSON to python
x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y['age'])

# Convert from python to JSON
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

y = json.dumps(x)
print(y)

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

# Format the result
json.dumps(x, indent=4)

json.dumps(x, indent=4, separators=(". ", " = "))

# Order the result
json.dumps(x, indent=4, sort_keys=True)

# RegEx Python
# It is a sequence of characters that forms a search pattern.
# It is used to check if a string contains the specific search patter.

import re # Module
txt = "The rain in spain"
x = re.search("^The.*Spain$", txt)
print(x)

# Functions: 
"""
findall: x = re.findall("ai", txt) => Returns a list containing all matches

search: x = re.search("Portugal", txt) => Returns a Match object if there is a match anywhere in the string
    # The Match object has properties and methods used to retrieve information about the search, and the result:
      .span() returns a tuple containing the start-, and end positions of the match.
      .string returns the string passed into the function
      .group() returns the part of the string where there was a match

split: x = re.split("\s", txt) => Returns a list where the string has been split at each match

sub: x = re.sub("\s", "9", txt) => Replaces one or many matches with a string
"""

# Metacharacters
"""
[]	A set of characters "[a-m]"
\	  Signals a special sequence (can also be used to escape special characters)	"\d"
.	  Any character (except newline character)	"he..o"
^	  Starts with	"^hello"
$	  Ends with	"planet$"
*	  Zero or more occurrences	"he.*o"
+	  One or more occurrences	"he.+o"	
?	  Zero or one occurrences	"he.?o"	
{}	Exactly the specified number of occurrences	"he.{2}o"	
|	  Either or	"falls|stays"	
()	Capture and group
"""

# Sets
"""
[arn]	      Returns a match where one of the specified characters (a, r, or n) is present	
[a-n]	      Returns a match for any lower case character, alphabetically between a and n	
[^arn]	    Returns a match for any character EXCEPT a, r, and n	
[0123]	    Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	      Returns a match for any digit between 0 and 9	
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	  Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	        In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string	

"""