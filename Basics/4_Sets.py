# Set
"""
Used to store the multiple values into the single variable
collection which in unordered, unchangeable and unindexed. Also they do not allow the duplicate values.
Set can't have two items with the same values.

Once a set is created we can't change the items of the set but we can add the new items.

Methods: add, clear, copy, difference, difference_update, discard, intersection, intersection_update, isdisjoint, issubset, isupersest, 
        pop, remove, symmetric_difference, symmetric_difference_update, union, update

"""

# How to create a set inside the python
thisset = {"apple", "banana", "cherry"}
print(thisset)
print(len(thisset))
print(type(thisset))

thisset = set((1, 2, 3)) # Set constructor
print(thisset)

# Access items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

# Add the items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# Remove : If the items doesn't exist so they generate the error
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

# Loop
thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)

# Join the two sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

# Keep only duplicates items
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y) # return a new set, that only contains the items that are present in both sets
print(z)

# Keep All, But NOT the Duplicates
# keep only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y) # return a new set, that contains only the elements that are NOT present in both sets.
print(z)

