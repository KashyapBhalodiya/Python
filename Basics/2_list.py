
# Lists are used to store multiple items in a single variable.
# It is used store the collection of data.
# List is a collection which is prdered and changeable. Allows duplicate members.

# Methods: append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort

# How to create a list
import this


mylist = ['apple', 'banana', 'cherry']
print(mylist)

# List items are ordered, changeable and allow duplicate values.
# First item has index 0.

print(len(mylist)) # Find out the length of the list
print(type(mylist)) # Find out the type 
thislist = list(("apple", "banana", "cherry")) # list constructor

# Accessing items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
print(thislist[-1])
print(thislist[-1])

# Check if the list is exist or not
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

# Change a range of item values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Insert items
thislist.insert(2, "watermelon")
print(thislist)

# Append items
thislist.append("orange")
print(thislist)

# extend items
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# add any iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# Remove specified item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Remove specified index
thislist.pop(2)
print(thislist)

del thislist[0]
print(thislist)

del thislist # Delete the list completely

thislist.clear() # Clear the entire list
print(thislist)

# Loop

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

for i in range(len(thislist)):
    print(thislist[i])

i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

# Looping Using List Comprehension
[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

# newlist = [expression for item in iterable if condition == True]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)

newlist = [x for x in range(10)]
newlist = [x for x in range(10)]
newlist = [x.upper() for x in fruits]
newlist = ['hello' for x in fruits]
newlist = [x if x != "banana" else "orange" for x in fruits]

# Sorting list
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Sort descending order
thislist.sort(reverse = True)
print(thislist)

# Custoize sort function
thislist.sort(key = str.lower)
print(thislist)

# Reverse order
thislist.reverse()
print(thislist)

# Copy of the list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# How to join the list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

for x in list2:
    list1.append(x)
print(list1)

list1.extend(list2)
print(list1)

