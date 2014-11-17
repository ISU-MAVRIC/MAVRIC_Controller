from PySide import QtCore
from serial import Serial

class PortController(QtCore.QObject):

    def __init__(self, controller, parent=None):
        super(PortController, self).__init__(parent)
        self.controller = controller

        self.settings = QtCore.QSettings()
        self.port = Serial()

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update)

        self.configure()

    def connect(self):
        self.port.open()
        if self.port.isOpen() == True:
            self.timer.start(50)
            return True

        return False

    def disconnect(self):
        self.timer.stop()
        self.port.close()

    def configure(self):
        port_name = self.settings.value("comm/port")
        port_baud = self.settings.value("comm/baud")

        self.port.port = port_name
        self.port.baudrate = port_baud

    def update(self):
        while self.port.inWaiting() > 0:
            byte = self.port.read()
            self.controller.parse(byte)
