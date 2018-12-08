import udp, tcp, os

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
    # test humidity access 
    udp.send('localhost', PI_DATA_UDP_PORT, 'h')
    val = udp.receive(PI_CONTROL_UDP_PORT_DATA)
    assert int(val) >= 0 and int(val) <= 100, 'Invalid humidity value!' + val

    # test temperature access 
    udp.send('localhost', PI_DATA_UDP_PORT, 't')
    val = udp.receive(PI_CONTROL_UDP_PORT_DATA)
    assert int(val) >= -50 and int(val) <= 50, 'Invalid temperature value!' + val

    # test image access 
    udp.send('localhost', PI_DATA_UDP_PORT, 'i')
    val = tcp.receive(PI_CONTROL_UDP_PORT_DATA)
    assert val != None, 'Did not receive a picture!'
    assert os.path.isfile(val), 'File not exist!'

if __name__=='__main__':
    main()
