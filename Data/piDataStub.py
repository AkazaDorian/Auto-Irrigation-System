import tcp, udp, time, bash
from picamera import PiCamera
import database

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
    filepath = '/home/pi/proj/photo/' + currTime + '.jpg'
    camera.capture(filepath)
    camera.stop_preview()
    camera.close()
    return filepath

def main():
    bash.command('sudo systemctl start readSensor')
    while True:
        command, address = udp.receive(PI_DATA_UDP_PORT)
        if command == 'h':
            udp.send(PI_CONTROL_IP_DATA, PI_CONTROL_UDP_PORT_DATA, '15.2')
        elif command == 't':
            time, hum, tem = database.read_data_from_db()
            udp.send(PI_CONTROL_IP_DATA, PI_CONTROL_UDP_PORT_DATA, '22.4')
        elif command == 'i':
            tcp.send(PI_CONTROL_IP_DATA, PI_CONTROL_TCP_PORT_DATA, '~\proj\image.jpg')

if __name__=='__main__':
    main()
