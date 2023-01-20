"""
python cab be used in database application. one of the most popular database is MongoDB.

MongoDB stores data in JSON-like documents, which makes the database very flexible and scalable.

"""

import pymongo

# Create database

# To create a database in MongoDB, start by creating a MongoClient object, then specify a connection 
# URL with the correct ip address and the name of the database you want to create.

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

# Check if database exist or not
dblist = myclient.list_database_names()
if 'database' in dblist:
    print("The database exist")

# See the all the databases
print(myclient.list_database_names())

# Create a collection
# To create a collection in MongoDB, use database object and specify the name of 
# the collection you want to create.

# In mongodb a collection is not created until it gets content.
mycol = mydb["customers"]

# Check if the collection is exist
collist = mydb.list_collection_names()
if "customers" in collist:
    print("The collection exists.")

# List out all the collections
print(mydb.list_collection_names())

