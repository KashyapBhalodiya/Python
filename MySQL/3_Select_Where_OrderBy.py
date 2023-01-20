# Select statement

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="mydatabase"
)

mycursor = mydb.cursor()
# Select the all the customers table
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall() # fetch all rows from last executed statement
for x in myresult:
    print(x)

# Selecting columns
mycursor.execute("SELECT name, address FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# using the fetchone() method
# If we are only inserted in one row then we will use
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchone()

# Where
# It is used to filter records.

sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"
mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# Wildcard characters
# Provide two wild characters: % (matches any string of zero or more characters) and _ (matches any single character)
sql = "SELECT * FROM customers WHERE address LIKE '%way%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# Prevent SQL Injection:
# When query values are provided by the user you should escape the values.

sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )
mycursor.execute(sql, adr)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# Order by
# Use the ORDER BY statement to sort the result in ascending or descending order.
# The ORDER BY keyword sorts the result ascending by default. To sort the result in descending order, use the DESC keyword.

sql = "SELECT * FROM customers ORDER BY name"
# sql = "SELECT * FROM customers ORDER BY name DESC"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

