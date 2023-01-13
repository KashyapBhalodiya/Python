# Dictionary

"""
used to store data values in key:value pairs.
collection which is ordered, changeable and do not allow duplicates.

"""

# How to create a dictionary
import this


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
print(len(thisdict))
print(type(thisdict))

thisdict = dict(name = "John", age = 36, country = "Norway") # Constructor
print(thisdict)

# Accessig the dictionary values
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]
print(x)
x = thisdict.get("model")
print(x)
x = thisdict.keys()
print(x)
x = thisdict.values()
print(x)
x = thisdict.items()
print(x)

# Check if the key is exist or not
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

# Update the dictionary
thisdict.update({"year": 2002})

# adding the items
thisdict["color"] = "red"
print(thisdict)

# Removing the items
thisdict.pop("model")
print(thisdict)

thisdict.popitem() # Remove the last item
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["model"]
# del thisdict # It will delete the entire dictionary
print(thisdict)


thisdict.clear()
print(thisdict)

# Loop through dictionary
for x in thisdict:
    print(x)

for x in thisdict:
    print(thisdict[x])

for x in thisdict.values():
    print(x)

for x in thisdict.keys():
    print(x)

for x, y in thisdict.items():
    print(x, y)

# Copy dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict.copy()
print(mydict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = dict(thisdict)
print(mydict)

# We create also nested dictionary

# Methods: clear, copy, fromkeys, get, items, keys, pop, popitem, setdefault, update, values