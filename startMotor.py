import RPi.GPIO as GPIO
import time
import sys
from array import *

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

ports = [31, 33, 35, 37]

for p in ports:
    GPIO.setup(p,GPIO.OUT)

while(True):
    for j in range(0, 4):
        time.sleep(0.002)
        for i in range(0, 4):
            if i == j:
                GPIO.output(ports[i],True)
            else:
                GPIO.output(ports[i],False)
exit()