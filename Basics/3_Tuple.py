# Tuple
"""
Tuples are used to store multiple items in a single variable

Tuple items are ordered, unchangeable, and allow duplicate values.
First item is start at index 0th


"""

# How to create a tuple
import this


thistuple = ("apple", "banaba", "cherry")
print(thistuple)
print(len(thistuple))
print(type(thistuple))

# Tuple Constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

print(thistuple[1])
print(thistuple[-1])
print(thistuple[2:5])
print(thistuple[-4:-1])

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

# add the items
# Convert into the list
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# Adding the tuple to a tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

# Remove items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# del keyword is used to remove the all the tuple
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)

# Unpacking the tuple
fruits = ("apple", "banana", "cherry", "strawberry")
(green, yellow, *red) = fruits
# (green, *yellow, red) = fruits
print(green)
print(yellow)
print(red)

# Loop through a tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

# Loop throuhg a tuple index numbers
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

# Methods of tuple: count() and index()
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)