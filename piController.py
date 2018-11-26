import socket, sys, os, time, subprocess, struct

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

def receiveTCP(port):
    try: 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        s.bind(('', port)) 
        s.listen(10) 
    except socket.error as msg: 
        print(msg) 
        sys.exit(1) 
        
    print("Receiving") 
    sock, addr = s.accept() 
    fileinfo_size = struct.calcsize('128sl') 
    buf = sock.recv(fileinfo_size) 
    if buf: 
        filename, filesize = struct.unpack('128sl', buf) 
        fn = filename.decode().strip('\x00') 
        new_filename = os.path.join('./', fn) 
        
        recvd_size = 0 
        fp = open(new_filename, 'wb') 

        while not recvd_size == filesize: 
            if filesize - recvd_size > 1024: 
                data = sock.recv(1024) 
                recvd_size += len(data) 
            else: 
                data = sock.recv(1024) 
                recvd_size = filesize 
            fp.write(data) 
        fp.close() 
    sock.close() 
    s.close() 

def bashCommand(command):
    process = subprocess.Popen(command.split(), stdout = subprocess.PIPE)
    output, error = process.communicate()
    return output, error

def main():
    while(True):
        command, address = receiveUDP(PI_CONTROL_UDP_PORT_AND)
        if command == 'h' or command == 't':
            sendUDP(PI_DATA_IP, PI_DATA_UDP_PORT, command)
            val, addr = receiveUDP(PI_CONTROL_UDP_PORT_DATA)
            sendUDP(address[0], ANDROID_UDP_PORT, val)
        elif command == 'i':
            sendUDP(PI_DATA_IP, PI_DATA_UDP_PORT, command)
            receiveTCP(PI_CONTROL_TCP_PORT_DATA)
            #TODO forward the data stream to address
        elif command == 'r':
            bashCommand('sudo systemctl start motor')
        elif command == 's':
            bashCommand('sudo systemctl stop motor')
        elif command == 'i':
            bashCommand('sudo systemctl start autoIrrigation')
        elif command == 'u':
            bashCommand('sudo systemctl stop autoIrrigation')

if __name__=='__main__':
    main()