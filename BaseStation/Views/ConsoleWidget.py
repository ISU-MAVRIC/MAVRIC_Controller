from PySide import QtCore, QtGui

class ConsoleWidget(QtGui.QDockWidget):
    """A dockable widget to display the command console."""

    def __init__(self, parent=None):
        """Create and initialize a ConsoleWidget.

        Args:
            parent (QWidget): Parent Qt widget.
        """
        super(ConsoleWidget, self).__init__("Console", parent)
        self.setAllowedAreas(QtCore.Qt.DockWidgetArea.BottomDockWidgetArea)

        self._initUI()

    def _initUI(self):
        """A private method to setup the UI."""
        # Create the content frame
        frame = QtGui.QFrame()
        self.setWidget(frame)

        # Create the main layout
        layout = QtGui.QVBoxLayout()
        frame.setLayout(layout)

        # Console display widget
        self.console = QtGui.QTextEdit(frame)
        self.console.setReadOnly(True)
        layout.addWidget(self.console)

        # Console send widgets
        send_layout = QtGui.QHBoxLayout()
        self.send_field = QtGui.QLineEdit(frame)
        send_layout.addWidget(self.send_field)
        send_button = QtGui.QPushButton("Send", frame)
        send_layout.addWidget(send_button)
        layout.addLayout(send_layout)
