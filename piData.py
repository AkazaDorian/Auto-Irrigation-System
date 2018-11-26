import socket, sys, os, time, subprocess, struct, serial
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

def receiveUDP(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('0.0.0.0', port)
    s.bind(server_address)

    print ("Waiting to receive on port %d : press Ctrl-C or Ctrl-Break to stop " % port)
    buf, address = s.recvfrom(port)
    buf = buf.decode('utf-8')
    print ("Received command from %s : %s" % (address, buf))
    s.close()
    return buf, address

def sendUDP(ip, port, txt):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (ip, port)
    s.sendto(txt.encode('utf-8'), server_address)

def sendTCP(ip, port, file):
    try: 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.connect((ip, port)) 
    except socket.error as msg: 
        print(msg) 
        print(sys.exit(1)) 
    fhead = struct.pack(b'128sl', bytes(os.path.basename(file), encoding='utf-8'), os.stat(file).st_size) 
    s.send(fhead) 
    print('client filepath: {0}'.format(file)) 
    
    fp = open(file, 'rb') 
    while 1: 
        data = fp.read(1024) 
        if not data: 
            print('{0} file sent over...'.format(file)) 
            break 
        s.send(data) 
    s.close() 

def bashCommand(command):
    process = subprocess.Popen(command.split(), stdout = subprocess.PIPE)
    output, error = process.communicate()
    return output, error

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
        command, address = receiveUDP(PI_DATA_UDP_PORT)
        if command == 'h':
            #TODO grab sensor log from database, save in hum
            hum, tem = readSensor()
            sendUDP(PI_CONTROL_IP_DATA, PI_CONTROL_UDP_PORT_DATA, hum)
        elif command == 't':
            #TODO grab sensor log from database, save in tem
            hum, tem = readSensor()
            sendUDP(PI_CONTROL_IP_DATA, PI_CONTROL_UDP_PORT_DATA, tem)
        elif command == 'i':
            path = takePhoto()
            sendTCP(PI_CONTROL_IP_DATA, PI_CONTROL_TCP_PORT_DATA, path)

if __name__=='__main__':
    main()
