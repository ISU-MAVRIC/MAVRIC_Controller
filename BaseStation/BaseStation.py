import sys

import pygame
from PySide import QtCore, QtGui

from Controllers.CommandController import *
from Controllers.InputController import *
from Controllers.PortController import *
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
    app.command_controller = CommandController(app)
    app.input_controller = InputController(app)
    app.port_controller = PortController(app.command_controller, app)

    # Create main window
    window = ApplicationWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
