import sqlite3
import csv
from sqlite3 import Error

#create a database connection
connection = sqlite3.connect('database.db')

#create a cursor
def create_connection(db_file):
    conn = None
    try: 
        conn = sqlite3.connect(db_file)
        print("Database Created")
    except Error as e:
        print(e)
    return conn

def create_table(c, create_table_sql):
    try:
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def add_data(cur, filename, db_name, num_cols):
    #add data from csv to the database 
    file = open(filename, encoding = 'utf-8')
    reader = csv.reader(file)
    #delete the first row of the csv file
    next(reader)
    questionmarks = ', '.join(['?'] * num_cols)
    #query to insert data into the database
    query = 'INSERT INTO ' + db_name + ' VALUES (' + questionmarks + ')'
    cur.executemany(query, reader)
    print("Data added to the database")

