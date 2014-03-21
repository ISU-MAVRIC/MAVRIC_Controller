#!/usr/bin/env python

'''
Provides a serial connection
'''
################################################

import serial
from PyQt4.QtCore import *
from PyQt4.QtGui import *

usbport = 'COM7'

# Set up serial baud rate
ser = serial.Serial(usbport, 9600, timeout=1)

def move(servo, angle):
   
    if (0 <= angle <= 255):
        ser.write(chr(255))
        ser.write(chr(servo))
        ser.write(chr(angle))
    else:
        print "Servo angle must be an integer between 0 and 255.\n"
'''
timer = QTimer()
timer.timeout.connect(move)
timer.start(20)
'''
timer = QTimer()
timer.connect(timer,SIGNAL("timeout()"), move)
timer.start(20)
