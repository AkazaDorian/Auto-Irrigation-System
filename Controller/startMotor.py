import RPi.GPIO as GPIO
import time
import sys
from array import *

GPIO.setwarnings(False) # disable GPIO warnings
GPIO.setmode(GPIO.BOARD) # pin mode

ports = [31, 33, 35, 37]

for p in ports:
    GPIO.setup(p,GPIO.OUT) # initialize as output

'''
A stepper motor requires its 4 pins to be True in turn to rotate.
'''
while True:
    for j in range(0, 4):
        time.sleep(0.002)
        for i in range(0, 4):
            if i == j:
                GPIO.output(ports[i],True)
            else:
                GPIO.output(ports[i],False)
exit()