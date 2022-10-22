# Project3_Kashaf

Generate a script that queries a database using Sqlite.

Part 1: Use Sqlite in Python

Create and query tables within a database using SQLite in Python. In this demo, we’ll create a database to manage data about a grocery business. 

1. install pysqlite3
2. build the script.py file to create the table: 
    i. define a connection (connection is used to connect to a database - pass in the name of the dataset, if you are referencing a new one then a new database will be created)
    ii. create a cursor (a cursor interacts with the database through sql commands - this will allow us to create and modify tables in our database)
3. Create the tables (products & costs)
4. Query the table using sql joins


Part 2: Load Dataset using Kaggle API

1. install kaggle - add to requirements file
2. create a directory with mkdir /home/codespace/.kaggle
3. copied the dataset to /home/codespace/.kaggle using 
cp /workspaces/Project3_Kashaf/kaggle.json /home/codespace/.kaggle
4. change permissions using 
chmod 600 /home/codespace/.kaggle/kaggle.json
5. load dataset using Kaggle API (copy this from Kaggle): 
kaggle datasets download -d jagaryousef/the-world-bank-projects
6. unzip the dataset
