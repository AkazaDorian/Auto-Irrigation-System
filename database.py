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
        unix = time.time()
        date = str(time.strftime("%z-%Y-%m-%d-%H-%M-%S"))
        humidity = humid
        temerature = temp
        cur.execute("INSERT INTO irrigationRecord (datestamp, humidity, temperature) VALUES (?, ?, ?)",
                  (date, humidity, temp))
        conn.commit()


def image_entry(im):
        create_table()
        unix = time.time()
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
        data = c.fetchone()
        time, humidity, temperature = get_data_column(data)
        return time, humidity, temperature


def get_image_column(data):
        col_time = data[0]
        col_image = data[1]
        return col_time, col_image


def read_image_from_db():
        cur.execute('SELECT * FROM photoRecord WHERE datestamp IN (select max(datestamp) from photoRecord)')
        data = c.fetchone()
        time, humidity, temperature = get_image_column(data)
        return time, humidity, temperature


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


## function Test ##
#readAll()
#print('                   ')
#ti,hu,tem = read_data_from_db()
#print(ti)
#print(hu)
#print(tem)


#data_entry(25.36, 59.63)
#data_entry(26.35, 25.02)
#data_entry(15.68, -96.36)
#data_entry(29.68, -48.02)
#data_entry(39.48, 69.48)
#data_entry(36.78, -69.15)
#data_entry(78.96, 19.68)
#data_entry(98.15, 36.14)
#data_entry(48.06, 02.36)
#data_entry(19.00, -8.69)
#data_entry(13.69, 02.95)
#data_entry(48.96, 18.96)





































    
