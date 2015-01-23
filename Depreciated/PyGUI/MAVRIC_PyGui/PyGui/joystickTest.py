import sys

import pygame
from PySide import QtGui, QtCore


pygame.init()
gamepad = pygame.joystick.Joystick(0)
print gamepad.get_name()
gamepad.init()
print "Axes: {}".format(gamepad.get_numaxes())
print "Buttons: {}".format(gamepad.get_numbuttons())
print "------------------"
axes = gamepad.get_numaxes()


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        # qbtn = QtGui.QPushButton('Quit', self)
        # qbtn.setToolTip('Quits the application')
        # qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        # qbtn.resize(qbtn.sizeHint())
        # qbtn.move(50, 50)
        #
        # label1 = QtGui.QLabel('MarkRusciano', self)
        # label1.move(15, 10)
        #
        # label2 = QtGui.QLabel('tutorial', self)
        # label2.move(35, 40)
        #
        # label3 = QtGui.QLabel('for MAVRIC', self)
        # label3.move(55, 70)
        #
        # self.setGeometry(300,300,250,150)
        # self.show()

        okButton = QtGui.QPushButton("Ok")
        cancelButton = QtGui.QPushButton('Cancel')

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)



        self.setWindowTitle("TxtExampleWindow")

        self.show()

    def center(self):

        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):

        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure you want to quit?", QtGui.QMessageBox.Yes |
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

    #
    # while True:
    # for i in range(axes):
    #         axis = gamepad.get_axis( i )
    #         print axis
    #         time.sleep(.2)
    #     print "---------------"