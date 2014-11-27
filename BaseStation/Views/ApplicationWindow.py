from PySide import QtCore, QtGui

from ConsoleWidget import *
from InputDialog import *
from OverviewTab import *
from PortDialog import *
from VitalsWidget import *

class ApplicationWindow(QtGui.QMainWindow):
    """The main application window."""

    def __init__(self):
        """Create and initialize an ApplicationWindow.

        Args:
            parent (QObject): Parent Qt object.
        """
        super(ApplicationWindow, self).__init__()

        self._initUI()

    def _initUI(self):
        # Set window title
        self.setWindowTitle('MAVRIC Base Station')

        # Create the menu bar
        menubar = self.menuBar()

        # File menu
        file_menu = menubar.addMenu('&File')

        # File/Log
        log_action = QtGui.QAction('Set &Log File', self)
        log_action.setShortcut('Ctrl+L')
        log_action.setStatusTip('Choose log output file')
        log_action.triggered.connect(self.configure_log)
        file_menu.addAction(log_action)

        # File/Exit
        file_menu.addSeparator()
        exit_action = QtGui.QAction('&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Options menu
        option_menu = menubar.addMenu('&Options')

        # Options/Serial
        serial_action = QtGui.QAction('Setup &Port', self)
        serial_action.setStatusTip('Configure the communications port')
        serial_action.triggered.connect(self.configure_port)
        option_menu.addAction(serial_action)
        self.connect_action = QtGui.QAction('&Connect Port', self)
        self.connect_action.setCheckable(True)
        self.connect_action.setStatusTip('Connect to the communications port')
        self.connect_action.toggled.connect(self.connect_port)
        option_menu.addAction(self.connect_action)

        # Options/Input
        option_menu.addSeparator()
        input_action = QtGui.QAction('Setup &Input', self)
        input_action.setStatusTip('Configure the input devices')
        input_action.triggered.connect(self.configure_input)
        option_menu.addAction(input_action)

        # Main tab frame
        self.tab_widget = QtGui.QTabWidget(self)
        self.setCentralWidget(self.tab_widget)

        # Overview tab
        self.overview_tab = OverviewTab()
        self.tab_widget.addTab(self.overview_tab, 'Overview')

        # Console dockable
        self.console_widget = ConsoleWidget(self)
        self.addDockWidget(QtCore.Qt.DockWidgetArea.BottomDockWidgetArea,
                self.console_widget)

        # Vitals dockable
        self.vitals_widget = VitalsWidget(self)
        self.addDockWidget(QtCore.Qt.DockWidgetArea.LeftDockWidgetArea,
                self.vitals_widget)

        # Create the status bar
        self.statusBar()

        # Maximize the window
        self.showMaximized()

    def configure_log(self):
        """Action handler for File/Log."""
        # Open a save file dialog
        fname, _ = QtGui.QFileDialog.getSaveFileName(
            self, 'Save log file',
            filter='Log files (*.txt)'
        )

    def configure_port(self):
        """Action handler for Options/Setup Port."""
        # Create and run port config dialog
        dialog = PortDialog(self)
        dialog.exec_()

    def connect_port(self, state):
        """Action handler for Options/Connect Port."""
        # Test if we should connect
        if state == True:
            # Try to connect
            if QtGui.QApplication.instance().port_controller.connect() == False:
                # Connection failed, uncheck menu item
                self.connect_action.setChecked(False)
        else:
            # Disconnect
            QtGui.QApplication.instance().port_controller.disconnect()

    def configure_input(self):
        """Action handler for Options/Setup Input."""
        # Create and run input config dialog
        dialog = InputDialog(self)
        dialog.exec_()
