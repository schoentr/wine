import psycopg2
import pandas as pd
import numpy as np

import numpy.polynomial.polynomial as poly
# df = pd.read_csv("data/cereal.csv", skiprows = 1)
wine_frame = pd.read_csv('wine-reviews/wine_data_2.csv',skiprows =1)
wine_frame =wine_frame.drop_duplicates(subset=None, keep='first', inplace=False)
values= wine_frame.values
try:
    conn = psycopg2.connect("host=localhost dbname=wines user=schoentr password=whitney" )
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE wine(
    id SERIAL PRIMARY KEY,
    unnamed NUMERIC(8,0),
    country VARCHAR(255),
    description TEXT,
    designation VARCHAR(255),
    points NUMERIC (3, 0),
    price NUMERIC(5,2),
    province VARCHAR(255),
    region_1 VARCHAR(255),
    region_2 VARCHAR(255),
    taster_name  VARCHAR(255),
    taster_twitter_handle VARCHAR(255),
    title  VARCHAR(255),
    variety VARCHAR(255),
    winery VARCHAR(255));
    """)
except(Exception, psycopg2.DatabaseError) as error:
        print(error)
cur.close()
conn.close()
# for x  in range (5):
#     try:
#         print(x,values[x][13])
#         print(type(values[x][0]))
#         print(type(values[x][1]))
#         print(type(values[x][2]))
#         print(type(values[x][3]))
#         print(type(values[x][4]))
#         print(type(values[x][5]))
#         print(type(values[x][6]))
#         print(type(values[x][7]))
#         print(type(values[x][8]))
#         print(type(values[x][9]))
#         print(type(values[x][10]))
#         print(type(values[x][11]))
#         print(type(values[x][12]))
#         print(type(values[x][13]))
        

#         conn = psycopg2.connect(host="localhost", dbname="wines", user="schoentr")
#         cur = conn.cursor()
#         insert_query=""""INSERT INTO wine(unnamed,country,description,designation,points,price,province,region_1,region_2,taster_name,taster_twitter_handle,title,variety,winery) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
#         vars= (str(values[x][0]), str(values[x][0]),values[x][13],values[x][13],values[x][13],values[x][13], values[x][13], values[x][13], values[x][13],values[x][13],values[x][13],values[x][13], values[x][13], values[x][13], values[x][13])
        
#         cur.execute(insert_query,vars)
#         conn.commit()
#     except(Exception, psycopg2.DatabaseError) as error:
#         print(error)