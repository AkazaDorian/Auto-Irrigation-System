import socket, sys

def receive(port):
    try: 
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(('0.0.0.0', port)) # use 0.0.0.0 instead of localhost
    except socket.error as msg: 
        print(msg) 
        sys.exit(1) 

    print ("Waiting to receive on port %d : press Ctrl-C or Ctrl-Break to stop " % port)
    buf, address = s.recvfrom(port)
    buf = buf.decode('utf-8') # transform bytes into string (for python3)
    print ("Received txt from %s : %s" % (address, buf))
    s.close() # close socket when finished
    return buf, address

def send(ip, port, txt):
    try: 
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_address = (ip, port)
        s.sendto(txt.encode('utf-8'), server_address)
    except socket.error as msg: 
        print(msg) 
        sys.exit(1) 
    s.close()