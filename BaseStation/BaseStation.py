import sys

import pygame
from PySide import QtCore, QtGui

from Controllers.InputController import *
from Views.ApplicationWindow import *

def main():
    # Initialize frameworks
    app = QtGui.QApplication(sys.argv)
    pygame.init()

    # Application settings
    QtCore.QCoreApplication.setOrganizationName('MAVRIC')
    QtCore.QCoreApplication.setApplicationName('Base Station')
    settings = QtCore.QSettings()
    app.setStyle('plastique')

    # Setup application objects
    app.input_controller = InputController(app)

    # Create main window
    window = ApplicationWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
