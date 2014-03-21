#!/usr/bin/env python

'''
MAVRIC GUI
'''
##########################################
'''To be fixed: def move. Needs to take self as an argument!
'''
#######################

import sys
from PyQt4 import QtGui, QtCore

def move(Prog, Status):
    if Prog == 0:
        global move0
        move0 = Status
    elif Prog == 1:
        global move1
        move1 = Status
    elif Prog == 2:
        global move2
        move2 = Status
    elif Prog == 3:
        global move3
        move3 = Status
    elif Prog == 4:
        global move4
        move4 = Status
    elif Prog == 5:
        global move5
        move5 = Status
    elif Prog == 6:
        global move6
        move6 = Status
    elif Prog == 7:
        global move7
        move7 = Status

class Progress(QtGui.QWidget):

    def __init__(self):
        super(Progress, self).__init__()

        self.initUI()
    
    def initUI(self):
    #Left Joystick
        #X axis
        self.pbar = QtGui.QProgressBar(self)
        self.pbar.setGeometry(50, 40, 200, 25)
        self.lbl = QtGui.QLabel('X axis', self)
        self.lbl.move(10, 40)
        #self.pbar.setValue(move0)
        
        #Y axis
        self.pbar1 = QtGui.QProgressBar(self)
        self.pbar1.setGeometry(50, 80, 200, 25)
        self.lbl1 = QtGui.QLabel('Y axis', self)
        self.lbl1.move(10, 80)   
        #self.pbar1.setValue(move1)

        #Z axis
        self.pbar3 = QtGui.QProgressBar(self)
        self.pbar3.setGeometry(50, 120, 200, 25)
        self.lbl3 = QtGui.QLabel('Z axis', self)
        self.lbl3.move(10, 120)
        #self.pbar3.setValue(move3)

        #Throttle
        self.pbar2 = QtGui.QProgressBar(self)
        self.pbar2.setGeometry(50, 160, 200, 25)
        self.lbl2 = QtGui.QLabel('Throttle', self)
        self.lbl2.move(10, 160)
        #self.pbar2.setValue(move2)

    #Right Joystick
        #X axis
        self.pbar4 = QtGui.QProgressBar(self)
        self.pbar4.setGeometry(350, 40, 200, 25)
        self.lbl4 = QtGui.QLabel('X axis', self)
        self.lbl4.move(300, 40)
        #self.pbar4.setValue(move4)
        
        #Y axis
        self.pbar5 = QtGui.QProgressBar(self)
        self.pbar5.setGeometry(350, 80, 200, 25)
        self.lbl5 = QtGui.QLabel('Y axis', self)
        self.lbl5.move(300, 80)   
        #self.pbar5.setValue(move5)

        #Z axis
        self.pbar7 = QtGui.QProgressBar(self)
        self.pbar7.setGeometry(350, 120, 200, 25)
        self.lbl7 = QtGui.QLabel('Z axis', self)
        self.lbl7.move(300, 120)
        #self.pbar7.setValue(move7)

        #Throttle
        self.pbar6 = QtGui.QProgressBar(self)
        self.pbar6.setGeometry(350, 160, 200, 25)
        self.lbl6 = QtGui.QLabel('Throttle', self)
        self.lbl6.move(300, 160)
        #self.pbar6.setValue(move6)  
        
        self.timer = QtCore.QBasicTimer()
        self.step = 0
        
        self.setGeometry(300, 300, 600, 300)
        self.setWindowTitle('MAVRIC Axis Display')
        self.show()
        self.timer.start(100, self)
           
def main():

    app = QtGui.QApplication(sys.argv)
    ex = Progress()
    ex.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()

