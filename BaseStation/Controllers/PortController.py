from PySide import QtCore
from serial import Serial


class PortController(QtCore.QObject):
    """A class to interface with the hardware serial port."""

    def __init__(self, controller, parent=None):
        """Construct and initialize a PortController.

        Args:
            controller (CommandController): CommandController instance for
            encoding and decoding commands.
            parent (QObject): Parent Qt object.
        """
        super(PortController, self).__init__(parent)
        self.controller = controller

        # Create internal objects
        self.settings = QtCore.QSettings()
        self.port = Serial()

        # Create timer
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self._update)

        # Load initial settings
        self.configure()

    def connect(self):
        """Connect to the internal serial port.

        Connect to the serial port specified through the application settings.

        Returns:
            True if the port connects, False otherwise.
        """
        self.port.open()
        if self.port.isOpen() == True:
            self.timer.start(500)
            return True

        return False

    def disconnect(self):
        """Disconnect the internal serial port."""
        self.timer.stop()
        self.port.close()

    def configure(self):
        """Load the configuration from the application settings object."""
        port_name = self.settings.value("comm/port")
        port_baud = self.settings.value("comm/baud")

        self.port.port = port_name
        self.port.baudrate = port_baud

    def write(self, data):
        """Write data to the serial port.

        Args:
            data (bytes): Data to be written.

        Returns:
            True if the port is ready, False otherwise.
        """
        if self.port.isOpen() == False:
            return False

        self.port.write(data)
        return True

    def _update(self):
        """Timer callback function."""
        while self.port.inWaiting() > 0:
            byte = self.port.read()
            self.controller.parse(byte)
