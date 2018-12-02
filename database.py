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

# write data humidity, temperayure to the table use 'cursor.execute()' with timestamps
# commit to save the file
def data_entry(humid, temp):
        create_table()
        unix = time.time()
        date = str(time.strftime("%z-%Y-%m-%d-%H-%M-%S"))
        humidity = humid
        temerature = temp
        cur.execute("INSERT INTO irrigationRecord (datestamp, humidity, temperature) VALUES (?, ?, ?)",
                  (date, humidity, temp))
        conn.commit()

# used in method read_data_from_db() to get coloumn in a row 
def get_data_column(data):
        col_time = data[0]
        col_humidity = data[1]
        col_temperature = data[2]
        return col_time, col_humidity, col_temperature

# read needed data from database using cursor.execute() function
# use 'select from table_name WHERE conditions' inside the execute() function
# 'fetchall()' to get all the data in selection
# print or return the data
def read_data_from_db():
        cur.execute('SELECT * FROM irrigationRecord WHERE datestamp IN (select max(datestamp) from irrigationRecord)')
        data = c.fetchone()
        time, humidity, temperature = get_data_column(data)
        return time, humidity, temperature

# read the whole database for irrigation data
def readAllData():
        cur.execute('SELECT * FROM irrigationRecord')
        data = c.fetchall()
        return data

# close cursor
if cur:
        cur.close()

# cole connection to database
if conn:
        conn.close()
