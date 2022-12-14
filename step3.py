import sqlite3
import pandas as pd


def connect_db():
    connect = sqlite3.connect("climate_db")
    cursor = connect.cursor()
    return cursor


def create_df(results, cursor):
    column_names = [x[0] for x in cursor.description]
    df = pd.DataFrame(results, columns=column_names)
    return df


def qi(cursor=connect_db()):
    i = "SELECT Country_Region, aqi_2021 FROM aqi_country order by 2 DESC limit 10;"
    q1i = create_df(cursor.execute(i).fetchall(), cursor)
    print(q1i)


def qii(cursor=connect_db()):
    # How many people died from air pollution in the top most polluted country in 2019?
    ii = "SELECT aqi.Country_Region, max(aqi.aqi_2019), (d.Outdoor_air_pollution + d.Air_pollution) air_pollution_deaths FROM aqi_country aqi join deaths_country d on aqi.Country_Region = d.Entity WHERE d.Year = 2019 and aqi.aqi_2019 != '-' order by aqi.aqi_2019 DESC;"
    # qii = "SELECT Entity, Year, Outdoor_air_pollution FROM deaths_country Where Year = 1990;"
    q1ii = create_df(cursor.execute(ii).fetchall(), cursor)
    print(q1ii)


def qiii(cursor=connect_db()):
    iii = "SELECT aqi.Country_Region, aqi.aqi_2019, Round((d.Outdoor_air_pollution + d.Air_pollution)*100/CAST(REPLACE(aqi.Population, ',', '') AS FLOAT),2) air_pollution_percentage_deaths_pk FROM aqi_country aqi join deaths_country d on aqi.Country_Region = d.Entity WHERE d.Year = 2019 and aqi.Country_Region = 'Pakistan' order by aqi.aqi_2019 DESC;"
    q1iii = create_df(cursor.execute(iii).fetchall(), cursor)
    print(q1iii)


def q_test(cursor=connect_db()):
    test = "SELECT count(Country_Region) FROM aqi_country where aqi_2019 != '-';"
    qtest1 = create_df(cursor.execute(test).fetchall(), cursor)
    print(qtest1)


if __name__ == "__main__":
    q_test()
