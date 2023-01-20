# Delete: You can delete records from an existing table by using the "DELETE FROM" statement

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="mydatabase"
)

mycursor = mydb.cursor()
sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
mycursor.execute(sql)
# Required otherwise any changes are not updated
mydb.commit() # To end our current transaction and make permanent all changes performed in the transaction.

# rowcount: Returns the number of rows are updated.
print(mycursor.rowcount, "record(s) deleted")


# Prevent SQL Injection:
# It is considered a good practice to escape the values of any query, also in delete statements.
# uses the placeholder %s to escape values in the delete statement

sql = "DELETE FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )
mycursor.execute(sql, adr)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")

# Drop Table:
sql = "DROP TABLE customers"
mycursor.execute(sql)

# Drop only if exist
sql = "DROP TABLE IF EXISTS customers"
mycursor.execute(sql)

# Update table
sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

# Prevent SQL Injection
sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 345", "Canyon 123")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

