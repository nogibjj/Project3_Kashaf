# import sqlite3
import sqlite3


# connect to database with a function
def create_db_table():
    # create and connect to database
    connect = sqlite3.connect("climate_db")
    cursor = connect.cursor()

    # Create table query
    # query to create a table for AQI in each country
    aqi_country = """CREATE TABLE IF NOT EXISTS aqi_country (
		Rank INTEGER,
        Country_Region varchar,
		aqi_2021 decimal,
		aqi_2020 decimal,
        aqi_2019 decimal,
        aqi_2018 decimal,
        Population decimal);"""
    # query to create a table about deaths due to different risk factos in each country
    deaths_country = """CREATE TABLE IF NOT EXISTS deaths_country (
		Entity varchar,
        Code varchar, 
        Year int, 
        Outdoor_air_pollution int,
        High_systolic_blood_pressure int,
        Diet_high_in_sodium int, 
        Diet_low_in_whole grains int,
        Alcohol_use int,
        Diet_low_in_fruits int,
        Unsafe_water_source int,
        Secondhand_smoke int, 
        Low_birth_weight int,
        Child_wasting int, 
        Unsafe_sex int, 
        Diet_low_in_nuts_and_seeds int, 
        Household_air_pollution_from_solid_fuels int, 
        Diet_low_in_vegetables int,
        Low_physical_activity int, 
        Smoking int, 
        High_fasting_plasma_glucose int, 
        Air_pollution int, 
        High_body_mass_index int, 
        Unsafe_sanitation int,
        No_access_to_handwashing_facility int, 
        Drug_use_Sex int,
        Low_bone_mineral_density int, 
        Vitamin_A_deficiency int, 
        Child_stunting int,
        Discontinued_breastfeeding int,
        Nonexclusive_breastfeeding int, 
        Iron_deficiency int);"""
        

    # execute query to create table
    cursor.execute(aqi_country) 
    cursor.execute(deaths_country)
    # close and save the change of db
    connect.commit()
    connect.close()


if __name__ == "__main__":
    create_db_table()