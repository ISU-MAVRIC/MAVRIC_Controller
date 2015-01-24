import sys

import pygame
from PySide import QtCore, QtGui

from Controllers.CommandController import *
from Controllers.InputController import *
from Controllers.PortController import *
from Views.ApplicationWindow import *

from Models.InputModel import *
from Models.CameraModel import *


def main():
    # Initialize frameworks
    app = QtGui.QApplication(sys.argv)
    pygame.init()

    # Application settings
    QtCore.QCoreApplication.setOrganizationName('MAVRIC')
    QtCore.QCoreApplication.setApplicationName('Base Station')
    settings = QtCore.QSettings()
    app.setStyle('plastique')

    input_model = InputModel()
    camera_model = CameraModel()

    # Setup application objects
    app.command_controller = CommandController(app)
    app.input_controller = InputController(app.command_controller, input_model, app)
    app.camera_controller = CameraController(input_model, camera_model, app)
    app.port_controller = PortController(app.command_controller, app)

    # Create main window
    app.window = ApplicationWindow()
    # Causes window to start windowed
    app.window.showNormal()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
