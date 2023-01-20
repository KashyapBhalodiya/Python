# Insert into Collection

# To insert a document into a collection, we use the insert_one() method.
# The first parameter of the insert_one() method is a dictionary containing the name(s) 
# and value(s) of each field in the document you want to insert.

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydict = {"name": "John", "address" : "Highway 200"}
x = mycol.insert_one(mydict)

# print(mydb.list_collection_names())

# Return the _id field:
# insert_one() method returns a InsertOneResult object, which has a property, inserted_id, 
# that holds the id of the inserted document.

# f you do not specify an _id field, then MongoDB will add one for you and assign a unique id for each document.
x = mycol.insert_one(mydict)
print(x.inserted_id)

# Insert multiple documents
# To insert the multiple documents we will used insert_many() method.
mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)

# inserted_ids holds the ids of the inserted documents
print(x.inserted_ids)

# Insert mulitple documents with specified IDs
mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)
print(x.inserted_ids)


# Find

# find() and find_one() methods to find data in a collection.

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

x = mycol.find_one()

print(x)

# find() method returns all occurrences in the selection
for x in mycol.find():
    print(x)


# Return only some fields
# The second parameter of the find() method is an object describing which fields to include in the result

for x in mycol.find({}, {"_id": 0, "name": 1, "address": 1}):
    print(x)

# You are not allowed to specify both 0 and 1 values in the same object 
# If you specify a field with the value 0, all other fields get the value 1, and vice versa

for x in mycol.find({},{ "address": 0 }):
    print(x)

