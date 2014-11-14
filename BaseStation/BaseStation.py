import sys
import pygame
from PySide import QtGui
from Views.ApplicationWindow import *

def main():
    app = QtGui.QApplication(sys.argv)
    app.setStyle('plastique')

    pygame.init()

    window = ApplicationWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
