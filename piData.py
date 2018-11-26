import tcp, udp, time, serial
from picamera import PiCamera

ANDROID_UDP_PORT = 10000
ANDROID_TCP_PORT = 10002
PI_DATA_IP = '10.0.0.38'
PI_DATA_UDP_PORT = 10001
PI_DATA_TCP_PORT = 10003
PI_CONTROL_IP_DATA = '10.0.0.31'
PI_CONTROL_UDP_PORT_AND = 10000
PI_CONTROL_UDP_PORT_DATA = 10001
PI_CONTROL_TCP_PORT_AND = 10002
PI_CONTROL_TCP_PORT_DATA = 10003

def takePhoto():
    camera = PiCamera()
    camera.start_preview()
    time.sleep(5)
    currTime = time.strftime('%z-%Y-%m-%d-%H-%M-%S', \
        time.localtime(time.time()))
    filepath = '/home/pi/photo/' + currTime + '.jpg'
    camera.capture(filepath)
    camera.stop_preview()
    return filepath

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
    while(True):
        command, address = udp.receive(PI_DATA_UDP_PORT)
        if command == 'h':
            #TODO grab sensor log from database, save in hum
            hum, tem = readSensor()
            udp.send(PI_CONTROL_IP_DATA, PI_CONTROL_UDP_PORT_DATA, hum)
        elif command == 't':
            #TODO grab sensor log from database, save in tem
            hum, tem = readSensor()
            udp.send(PI_CONTROL_IP_DATA, PI_CONTROL_UDP_PORT_DATA, tem)
        elif command == 'i':
            path = takePhoto()
            tcp.send(PI_CONTROL_IP_DATA, PI_CONTROL_TCP_PORT_DATA, path)

if __name__=='__main__':
    main()
