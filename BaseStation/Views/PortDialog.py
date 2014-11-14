from PySide import QtCore, QtGui

class PortDialog(QtGui.QDialog):

    _baud_rates = ['9600', '19200', '38400', '57600', '115200']

    def __init__(self, parent):
        super(PortDialog, self).__init__(parent)
        self.setWindowTitle('Configure port')

        self.settings = QtCore.QSettings()

        self.initUI()

    def initUI(self):
        layout = QtGui.QVBoxLayout()
        self.setLayout(layout)

        form = QtGui.QFormLayout()
        layout.addLayout(form)
        self.port_field = QtGui.QLineEdit(self)
        port_name = self.settings.value('comm/port')
        if port_name is not None:
            self.port_field.setText(port_name)
        form.addRow('Port:', self.port_field)

        self.baud_list = QtGui.QComboBox(self)
        self.baud_list.addItems(self._baud_rates)
        temp_baud = self.settings.value('comm/baud')
        if temp_baud is not None:
            baud_index = self._baud_rates.index(str(temp_baud))
            self.baud_list.setCurrentIndex(baud_index)
        form.addRow('Baud Rate:', self.baud_list)

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
        port_name = self.port_field.text()
        self.settings.setValue('comm/port', port_name)
        
        baud_rate = int(self.baud_list.currentText())
        self.settings.setValue('comm/baud', baud_rate)

        self.accept()
