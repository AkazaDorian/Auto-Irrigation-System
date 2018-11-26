import socket, struct, sys, os

def receive(port):
    try: 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        # allow resuse of address
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        s.bind(('', port)) 
        s.listen(10) # listen to socket, backlog when 10 failed connections
    except socket.error as msg: 
        print(msg) 
        sys.exit(1) 
        
    print("Receiving") 
    sock, addr = s.accept() 
    fileinfo = struct.calcsize('128sl') # get filename and size
    buf = sock.recv(fileinfo) 
    if buf: 
        filename, filesize = struct.unpack('128sl', buf) 
        fp = open(filename.decode().strip('\x00') , 'wb') # create new file

        while True: 
            data = sock.recv(1024)
            fp.write(data) 
            if len(data) < 1024: # last packet received
                break
        fp.close() 
    sock.close() 
    s.close() 

def send(ip, port, file):
    try: 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.connect((ip, port)) 
    except socket.error as msg: 
        print(msg) 
        print(sys.exit(1)) 

    # pack the filename and size into a struct of bytes in a package of 128 bytes of int or log
    fhead = struct.pack(b'128sl', bytes(os.path.basename(file), encoding='utf-8'), os.stat(file).st_size) 
    s.send(fhead) 
    print('client filepath: {0}'.format(file)) 
    
    fp = open(file, 'rb') # open file
    while 1: 
        data = fp.read(1024) 
        if not data: 
            print('{0} file sent over...'.format(file)) 
            break # data sent
        s.send(data) # send data in blocks of 1024 bytes
    s.close() # close socket when finished

def forwardTCP(portIn, ipOut, portOut):
    #TODO
    print('TODO')