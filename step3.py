import sqlite3
import numpy as np
import pandas as pd


def connect_db():
    connect = sqlite3.connect("climate_db")
    cursor = connect.cursor()
    return cursor


def create_df(results, cursor):
    column_names = [x[0] for x in cursor.description]
    df = pd.DataFrame(results, columns=column_names)
    return df

def q(cursor=connect_db()):
    q1 = "SELECT * FROM aqi_country where Country_Region == 'Pakistan'"
    q1i = create_df(cursor.execute(q1).fetchall(), cursor)
    print(q1i)


