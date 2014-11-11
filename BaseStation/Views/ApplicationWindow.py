from PySide import QtCore, QtGui

from ConsoleWidget import *
from VitalsWidget import *

class ApplicationWindow(QtGui.QMainWindow):

    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('MAVRIC Base Station')
        self.statusBar()

        self.tab_widget = QtGui.QTabWidget(self)

        self.setCentralWidget(self.tab_widget)

        self.console_widget = ConsoleWidget(self)
        self.addDockWidget(QtCore.Qt.DockWidgetArea.BottomDockWidgetArea,
                self.console_widget)

        self.vitals_widget = VitalsWidget(self)
        self.addDockWidget(QtCore.Qt.DockWidgetArea.LeftDockWidgetArea,
                self.vitals_widget)

        self.showMaximized()
