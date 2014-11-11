from PySide import QtCore, QtGui

class VitalsWidget(QtGui.QDockWidget):

    def __init__(self, parent=None):
        super(VitalsWidget, self).__init__("Vitals", parent)
        self.setAllowedAreas(
            QtCore.Qt.DockWidgetArea.LeftDockWidgetArea |
            QtCore.Qt.DockWidgetArea.RightDockWidgetArea)
        self.initUI()

    def initUI(self):
        frame = QtGui.QFrame()
        layout = QtGui.QVBoxLayout()

        layout.addWidget(QtGui.QLabel("Voltage:", frame))
        self.voltage_bar = QtGui.QProgressBar(frame)
        self.voltage_bar.setTextVisible(True)
        layout.addWidget(self.voltage_bar)

        layout.addWidget(QtGui.QLabel("Current:", frame))
        self.current_bar = QtGui.QProgressBar(frame)
        self.current_bar.setTextVisible(True)
        layout.addWidget(self.current_bar)

        layout.addWidget(QtGui.QLabel("Packet Rate:", frame))
        self.packet_bar = QtGui.QProgressBar(frame)
        self.packet_bar.setTextVisible(True)
        layout.addWidget(self.packet_bar)

        layout.addStretch(1)

        frame.setLayout(layout)
        self.setWidget(frame)
