from PySide import QtCore, QtGui

class PortDialog(QtGui.QDialog):
    """A dialog to configure the serial port."""

    # List of baud rates
    _baud_rates = ['9600', '19200', '38400', '57600', '115200']

    def __init__(self, parent):
        """Create and initialize a PortDialog.

        Args:
            parent (QWidget): Parent Qt widget.
        """
        super(PortDialog, self).__init__(parent)
        self.setWindowTitle('Configure port')

        # Get an instance of the settings object
        self.settings = QtCore.QSettings()

        # Setup the UI
        self._initUI()

    def _initUI(self):
        """A private method to setup the UI."""
        # Main layout
        layout = QtGui.QVBoxLayout()
        self.setLayout(layout)

        # Foram layout for selection boxes
        form = QtGui.QFormLayout()
        layout.addLayout(form)

        # Port selection
        self.port_field = QtGui.QLineEdit(self)
        # Attempt to load saved port
        port_name = self.settings.value('comm/port')
        if port_name is not None:
            self.port_field.setText(port_name)
        form.addRow('Port:', self.port_field)

        # Baud rate selection
        self.baud_list = QtGui.QComboBox(self)
        self.baud_list.addItems(self._baud_rates)
        # Attempt to load saved baud rate
        temp_baud = self.settings.value('comm/baud')
        if temp_baud is not None:
            baud_index = self._baud_rates.index(str(temp_baud))
            self.baud_list.setCurrentIndex(baud_index)
        form.addRow('Baud Rate:', self.baud_list)

        # Ok/cancel buttons
        buttons = QtGui.QHBoxLayout()
        buttons.addStretch(1)
        layout.addLayout(buttons)
        no_button = QtGui.QPushButton('Cancel', self)
        no_button.clicked.connect(self.reject)
        buttons.addWidget(no_button)
        ok_button = QtGui.QPushButton("OK", self)
        ok_button.setDefault(True)
        ok_button.clicked.connect(self.ok_action)
        buttons.addWidget(ok_button)

    def ok_action(self):
        """Action handler for ok button."""
        # Save port name
        port_name = self.port_field.text()
        self.settings.setValue('comm/port', port_name)

        # Save baud rate
        baud_rate = int(self.baud_list.currentText())
        self.settings.setValue('comm/baud', baud_rate)

        # Notify the port controller
        QtGui.QApplication.instance().port_controller.configure()

        # Cleanup the dialog
        self.accept()
