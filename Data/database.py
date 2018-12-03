import sqlite3
import time
import datetime

# build Connection to a database
conn = sqlite3.connect('DataBase.db')
# define cursor
cur = conn.cursor()


# create a table named irrigationRecord with columns datestamp(TEXT), humidity(DOUBLE), and temperature(DOUBLE)
# if the table does not exists
def create_table():
    cur.execute('CREATE TABLE IF NOT EXISTS irrigationRecord(datestamp TEXT, humidity DOUBLE, temperature DOUBLE)')
    cur.execute('CREATE TABLE IF NOT EXISTS photoRecord(datestamp TEXT, image BLOB)')


# write data humidity, temperayure to the table use 'cursor.execute()' with timestamps
# commit to save the file
def data_entry(humid, temp):
    create_table()
    date = str(time.strftime("%z-%Y-%m-%d-%H-%M-%S"))
    cur.execute("INSERT INTO irrigationRecord (datestamp, humidity, temperature) VALUES (?, ?, ?)",\
        (date, humid, temp))
    conn.commit()


def image_entry(im):
    create_table()
    date = str(time.strftime("%z-%Y-%m-%d-%H-%M-%S"))
    image = im
    cur.execute("INSERT INTO photoRecord (datestamp, image) VALUES (?, ?)", (date, image))
    conn.commit()


# read needed data from database using cursor.execute() function
# use 'select from table_name WHERE conditions' inside the execute() function
# 'fetchall()' to get all the data in selection
# print or return the data
def get_data_column(data):
    col_time = data[0]
    col_humidity = data[1]
    col_temperature = data[2]
    return col_time, col_humidity, col_temperature


def read_data_from_db():
    cur.execute('SELECT * FROM irrigationRecord WHERE datestamp IN (select max(datestamp) from irrigationRecord)')
    data = cur.fetchone()
    time, humidity, temperature = get_data_column(data)
    return time, humidity, temperature


def get_image_column(data):
    col_time = data[0]
    col_image = data[1]
    return col_time, col_image


def read_image_from_db():
    cur.execute('SELECT * FROM photoRecord WHERE datestamp IN (select max(datestamp) from photoRecord)')
    data = cur.fetchone()
    return get_image_column(data)


def readAllData():
    cur.execute('SELECT * FROM irrigationRecord')
    data = cur.fetchall()
    return data
