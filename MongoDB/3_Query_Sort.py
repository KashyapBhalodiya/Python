# Query

# Filter the result
# When finding documents in a collection, you can filter the result by using a query object.
# The first argument of the find() method is a query object, and is used to limit the search.

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["mydatabase"]
mycol = mydb["mycustomers"]

myquery = {"address": "Park Lane 38"}
mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

# Addvanced query: we can use modifiers as values in query object
# E.g. to find the documents where the "address" field starts with the letter "S" or higher (alphabetically), 
# use the greater than modifier: {"$gt": "S"}:

myquery = { "address": { "$gt": "S" } }

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

# Filter with regular expressions: use regular expressions as a modifier.
# It is only be used to query strings.

# To find only the documents where the "address" field starts with the letter "S", use the regular expression {"$regex": "^S"}:
myquery = { "address": { "$regex": "^S" } }

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

# Sort:
mydoc = mycol.find().sort("name")

for x in mydoc:
    print(x)

mydoc = mycol.find().sort("name", -1)

for x in mydoc:
    print(x)