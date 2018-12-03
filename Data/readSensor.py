import database, time, serial

READING_PERIOD = 3600

def readSensor():
    ser = serial.Serial('/dev/ttyACM0',9600)
    time.sleep(2)
    print('reading humidity')
    ser.write('h'.encode())
    hum = ser.readline().decode('utf-8')
    print('reading temperature')
    ser.write('t'.encode())
    tem = ser.readline().decode('utf-8')
    return hum, tem

def main():
    while True:
        hum, tem = readSensor()
        database.data_entry(hum, tem)
        time.sleep(READING_PERIOD - 2)
        
if __name__=='__main__':
    main()