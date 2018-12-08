import tcp, udp, bash, time

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

def main():
    while True:
        command, address = udp.receive(PI_CONTROL_UDP_PORT_AND)
        if command == 'h': # humidity or temperature requested
            udp.send(address[0], ANDROID_UDP_PORT, '15.1')
        elif command == 't': # humidity or temperature requested
            udp.send(address[0], ANDROID_UDP_PORT, '22.3')
        elif command == 'i': # image requestedm, 
            tcp.send(address[0], ANDROID_TCP_PORT, '~\proj\image.jpg')
        elif command == 'r': # start motor requested
            print('sudo systemctl start motor')
        elif command == 's': # stop motor requested
            print('sudo systemctl stop motor')
        elif command == 'a': # turn auto irrigation mode on
            print('sudo systemctl start autoIrrigation')
        elif command == 'u': # turn auto irrigation mode off
            print('sudo systemctl stop autoIrrigation')

if __name__=='__main__':
    main()
