import sys

import pygame
from PySide import QtCore, QtGui

from Views.ApplicationWindow import *

def main():
    app = QtGui.QApplication(sys.argv)

    QtCore.QCoreApplication.setOrganizationName('MAVRIC')
    QtCore.QCoreApplication.setApplicationName('Base Station')
    settings = QtCore.QSettings()
    app.setStyle('plastique')

    pygame.init()

    window = ApplicationWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
