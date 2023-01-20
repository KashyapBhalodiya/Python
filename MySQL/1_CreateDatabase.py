"""
Python can be used in database applications.
One of the most popular databases is MySQL.
"""

# Download and install "MySQL Connector": python -m pip install mysql-connector-python

# test mysql connector:
import mysql.connector # If the page is successfully is run then it is installed.

# Create a connection

mydb = mysql.connector.connect(
    host="localhost",
    user="",
    password=""
)
print(mydb)

# How to create the database
mydb2 = mysql.connector.connect(
    host="localhost",
    user="",
    password=""
)

mycursor = mydb2.cursor()
mycursor.execute("CREATE DATABASE mydatabase")

# Check if database is exist:
mycursor.execute("SHOW DATABASES")

# check if tables is exist:
mycursor.execute("SHOW TABLES")

# Return a list of your system's databases:
for x in mycursor:
    print(x)

# Try to access the database when making the connection
# If the database does not exist, you will get an error
mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="mydatabase"
)

