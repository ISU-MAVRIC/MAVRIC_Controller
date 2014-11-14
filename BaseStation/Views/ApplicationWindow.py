from PySide import QtCore, QtGui

from ConsoleWidget import *
from InputDialog import *
from OverviewTab import *
from VitalsWidget import *

class ApplicationWindow(QtGui.QMainWindow):

    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('MAVRIC Base Station')

        menubar = self.menuBar()
        file_menu = menubar.addMenu('&File')
        log_action = QtGui.QAction('Set &Log File', self)
        log_action.setShortcut('Ctrl+L')
        log_action.setStatusTip('Choose log output file')
        log_action.triggered.connect(self.configure_log)
        file_menu.addAction(log_action)
        file_menu.addSeparator()
        exit_action = QtGui.QAction('&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        option_menu = menubar.addMenu('&Options')
        serial_action = QtGui.QAction('Setup &Port', self)
        serial_action.setStatusTip('Configure the communications port')
        serial_action.triggered.connect(self.configure_port)
        option_menu.addAction(serial_action)
        connect_action = QtGui.QAction('&Connect Port', self)
        connect_action.setCheckable(True)
        connect_action.setStatusTip('Connect to the communications port')
        connect_action.triggered.connect(self.connect_port)
        option_menu.addAction(connect_action)
        option_menu.addSeparator()
        input_action = QtGui.QAction('Setup &Input', self)
        input_action.setStatusTip('Configure the input devices')
        input_action.triggered.connect(self.configure_input)
        option_menu.addAction(input_action)

        self.tab_widget = QtGui.QTabWidget(self)
        self.overview_tab = OverviewTab()
        self.tab_widget.addTab(self.overview_tab, 'Overview')
        self.setCentralWidget(self.tab_widget)

        self.console_widget = ConsoleWidget(self)
        self.addDockWidget(QtCore.Qt.DockWidgetArea.BottomDockWidgetArea,
                self.console_widget)

        self.vitals_widget = VitalsWidget(self)
        self.addDockWidget(QtCore.Qt.DockWidgetArea.LeftDockWidgetArea,
                self.vitals_widget)

        self.statusBar()

        self.showMaximized()

    def configure_log(self):
        fname, _ = QtGui.QFileDialog.getSaveFileName(
            self, 'Save log file',
            filter='Log files (*.txt)'
        )

    def configure_port(self):
        pass

    def connect_port(self):
        pass

    def configure_input(self):
        dialog = InputDialog(self)
        if dialog.exec_() == QtGui.QDialog.DialogCode.Accepted:
            pass # notify input manager
