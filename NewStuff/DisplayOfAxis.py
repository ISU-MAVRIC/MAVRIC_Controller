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

class Progress(QtGui.QWidget):

    def __init__(self):
        super(Progress, self).__init__()

        self.initUI()

    def initUI(self):

        #X axis
        self.pbar = QtGui.QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)
        self.lbl = QtGui.QLabel('X axis', self)
        self.lbl.move(200, 40)
        #self.pbar.setValue(60)
        
        #Y axis
        self.pbar1 = QtGui.QProgressBar(self)
        self.pbar1.setGeometry(30, 80, 200, 25)
        self.lbl1 = QtGui.QLabel('Y axis', self)
        self.lbl1.move(200, 80)
        
        #self.pbar1.setValue(80)

        #Z axis
        self.pbar3 = QtGui.QProgressBar(self)
        self.pbar3.setGeometry(30, 120, 200, 25)
        self.lbl3 = QtGui.QLabel('Z axis', self)
        self.lbl3.move(200, 120)
        #self.pbar3.setValue(step3)

        #Throttle
        self.pbar2 = QtGui.QProgressBar(self)
        self.pbar2.setGeometry(30, 160, 200, 25)
        self.lbl2 = QtGui.QLabel('Throttle', self)
        self.lbl2.move(200, 160)
        #self.pbar2.setValue(step2)

        self.timer = QtCore.QBasicTimer()
        self.step = 0
        
        self.setGeometry(300, 300, 280, 280)
        self.setWindowTitle('MAVRIC Axis Display')
        self.show()
        self.timer.start(100, self)

def move(Prog, Status):
    if Prog == 0:
        self.pbar.setValue(Status)
    elif Prog == 1:
        self.pbar1.setValue(Status)
    elif Prog == 2:
        self.pbar2.setValue(Status)
    elif Prog == 3:
        self.pbar3.setValue(Status)
            
def main():

    app = QtGui.QApplication(sys.argv)
    ex = Progress()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()

