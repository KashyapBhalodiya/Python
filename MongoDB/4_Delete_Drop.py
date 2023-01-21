# delete one document we used delete_one() method.

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = {"address": "Mountain 21"}

mycol.delete_one(myquery)

# Delete many documents we used delete_many() method
myquery = { "address": {"$regex": "^S"} }

x = mycol.delete_many(myquery)

print(x.deleted_count, " documents deleted.")

# Delete all the documents in a collection
x = mycol.delete_many({})

print(x.deleted_count, "documents deleted")

# Drop collections

# Delete collection: using drop() method

mycol.drop()

# The drop() method returns true if the collection was dropped successfully, and false if the collection does not exist.
