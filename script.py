import sqlite3

#create a database connection
connection = sqlite3.connect('database.db')

#create a cursor
cursor = connection.cursor()

#create a table
command1 = ('''CREATE TABLE IF NOT EXISTS
                    products(product_id INTEGER PRIMARY KEY, category TEXT, price FLOAT, quantity FLOAT)''')

cursor.execute(command1)

command2 = ('''CREATE TABLE IF NOT EXISTS 
                    costs(purchase_id INTEGER PRIMARY KEY, product_id INTEGER, cost FLOAT,
                    FOREIGN KEY(product_id) REFERENCES products(product_id))''')

cursor.execute(command2)

#add to products table
cursor.execute('''INSERT INTO products VALUES(1, 'bread', 10.00, 100)''')
cursor.execute('''INSERT INTO products VALUES(2, 'milk', 20.00, 100)''')
cursor.execute('''INSERT INTO products VALUES(3, 'eggs', 30.00, 100)''')

#add to costs table
cursor.execute('''INSERT INTO costs VALUES(1, 1, 5.00)''')
cursor.execute('''INSERT INTO costs VALUES(2, 2, 10.00)''')
cursor.execute('''INSERT INTO costs VALUES(3, 3, 15.00)''')

#get results
cursor.execute('''SELECT * FROM products''')
results = cursor.fetchall()
print(results)
#this will return the products table.
