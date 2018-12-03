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
        if command == 'h' or command == 't': # humidity or temperature requested
            udp.send(PI_DATA_IP, PI_DATA_UDP_PORT, command)
            val, addr = udp.receive(PI_CONTROL_UDP_PORT_DATA)
            udp.send(address[0], ANDROID_UDP_PORT, val)
        elif command == 'i': # image requestedm, 
            udp.send(PI_DATA_IP, PI_DATA_UDP_PORT, command)
            tcp.forward(PI_CONTROL_TCP_PORT_DATA, address[0], ANDROID_TCP_PORT)
        elif command == 'r': # start motor requested
            bash.command('sudo systemctl start motor')
        elif command == 's': # stop motor requested
            bash.command('sudo systemctl stop motor')
        elif command == 'a': # turn auto irrigation mode on
            bash.command('sudo systemctl start autoIrrigation')
        elif command == 'u': # turn auto irrigation mode off
            bash.command('sudo systemctl stop autoIrrigation')

if __name__=='__main__':
    main()
