import sys
from PySide import QtGui
from Views.ApplicationWindow import *

def main():
    app = QtGui.QApplication(sys.argv)
    window = ApplicationWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
