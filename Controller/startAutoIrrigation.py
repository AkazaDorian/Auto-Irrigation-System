import bash, udp, time

PI_DATA_IP = '10.0.0.38'
PI_DATA_UDP_PORT = 10001
PI_CONTROL_UDP_PORT_DATA = 10001

def main():
    while True:
        udp.send(PI_DATA_IP, PI_DATA_UDP_PORT, 'h')
        hum, addr = udp.receive(PI_CONTROL_UDP_PORT_DATA)
        hum = float(hum)
        udp.send(PI_DATA_IP, PI_DATA_UDP_PORT, 't')
        tem, addr = udp.receive(PI_CONTROL_UDP_PORT_DATA)
        tem = float(tem)
        delay = tem ** 2 - tem * 10 - hum * 2
        bash.command('sudo systemctl start motor')
        time.sleep(delay)
        bash.command('sudo systemctl stop motor')
        time.sleep(86400 - delay - 1)

if __name__=='__main__':
    main()
