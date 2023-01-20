# To create a table in mysql use the "CREATE TABLE" statement.

# make sure you defined name of database when you create a connection

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mydatabase"
)

# It is object which allows you to iterate the records of a table.
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# Primary key:
# When creating a table you should also create a column with a unique key for each round.
# This can be done by defining a PRIMARY KEY.

mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))") # AUTO_INCREMENT: It will increament value by 1

# If the table already exists, use the ALTER TABLE keyword
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# Insert table

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

# It is required to make the changes otherwise it will not affected.
mydb.commit()
print(mycursor.rowcount, "Record inserted")

# To insert multiple rows into a table, use the executemany() method.
# second parameter of the executemany() method is a list of tuples, containing the data you want to insert

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
    ('Peter', 'Lowstreet 4'),
    ('Amy', 'Apple st 652'),
    ('Hannah', 'Mountain 21'),
    ('Michael', 'Valley 345'),
    ('Sandy', 'Ocean blvd 2'),
    ('Betty', 'Green Grass 1'),
    ('Richard', 'Sky st 331'),
    ('Susan', 'One way 98'),
    ('Vicky', 'Yellow Garden 2'),
    ('Ben', 'Park Lane 38'),
    ('William', 'Central st 954'),
    ('Chuck', 'Main Road 989'),
    ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")

# Get Inserted ID
# You can get the id of row you just inserted by asking the cursor object.

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)

mydb.commit()
# To get and print the ID of the last inserted row, lastrowid is used
print("1 record inserted, ID:", mycursor.lastrowid)

