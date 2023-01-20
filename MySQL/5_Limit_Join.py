# Limit:
# we can limit the number of records returned from the query.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 5")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# Start from another position:
# offset: used to specify from which row we want the data to retrieve.

mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)


# Join:
# Join two or more tables:
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

# INNER JOIN: We can join using this statement also.
# sql = "SELECT column_name(s)
# FROM table1
# INNER JOIN table2
# ON table1.column_name = table2.column_name"

mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# Left Join:
# If you want to show all users, even if they do not have a favorite product, use the LEFT JOIN statement:
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  LEFT JOIN products ON users.fav = products.id"

# Right join:
# If you want to return all products, and the users who have them as their favorite, even if no user have them as their favorite, use the RIGHT JOIN statement:
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  RIGHT JOIN products ON users.fav = products.id"