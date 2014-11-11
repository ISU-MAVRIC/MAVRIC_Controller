from PySide import QtCore, QtGui

class ConsoleWidget(QtGui.QDockWidget):

    def __init__(self, parent=None):
        super(ConsoleWidget, self).__init__("Console", parent)
        self.setAllowedAreas(QtCore.Qt.DockWidgetArea.BottomDockWidgetArea)
        self.initUI()

    def initUI(self):
        frame = QtGui.QFrame()
        layout = QtGui.QVBoxLayout()

        self.console = QtGui.QTextEdit(frame)
        self.console.setReadOnly(True)
        layout.addWidget(self.console)

        send_layout = QtGui.QHBoxLayout()
        self.send_field = QtGui.QLineEdit(frame)
        send_layout.addWidget(self.send_field)
        send_button = QtGui.QPushButton("Send", frame)
        send_layout.addWidget(send_button)
        layout.addLayout(send_layout)

        frame.setLayout(layout)
        self.setWidget(frame)
