# insert data
import sqlite3
import csv


def initial_build():
    # connect to database
    connect = sqlite3.connect("climate_db")
    cursor = connect.cursor()

    # query to insert csv data into existing tables
    insert_aqi = """INSERT INTO aqi_country VALUES(?, ?, ?, ?, ?, ?, ?)"""
    insert_deaths = """INSERT INTO deaths_country VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

    # Readl files
    aqi_filepath = "data/aqi.csv"
    deaths_filepath = "data/deaths.csv"

    file_aqi = open(aqi_filepath, encoding="utf8")
    data_aqi = csv.reader(file_aqi)
    next(data_aqi)  # pass header row

    file_deaths = open(deaths_filepath,encoding="utf8")
    data_deaths = csv.reader(file_deaths)
    next(data_deaths)  # pass header row

    # execute inesert query
    cursor.executemany(insert_aqi, data_aqi)
    cursor.executemany(insert_deaths, data_deaths)
    # close and save the change of db
    connect.commit()


# connect.close()


def insert_db(path, table):
    # execute query
    # connect to database
    connect = sqlite3.connect("co2db")
    cursor = connect.cursor()
    file = open(path, encoding="utf8")
    data = csv.reader(file)
    next(data)  # pass header row

    if table == "co2":
        insert = """INSERT INTO aqi_country VALUES(?, ?, ?, ?, ?, ?, ?)"""
    else:
        insert = """INSERT INTO deaths_country VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

    cursor.executemany(insert, data)
    connect.commit()


# connect.close()

if __name__ == "__main__":

    initial_build()
    # connect.commit()
# connect.close()