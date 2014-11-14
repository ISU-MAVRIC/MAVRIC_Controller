from pygame import joystick
from PySide import QtGui

class InputDialog(QtGui.QDialog):

    def __init__(self, parent):
        super(InputDialog, self).__init__(parent)
        self.setWindowTitle('Configure input devices')
        self.initUI()
        self.primary = None

    def initUI(self):
        joysticks = self.get_joystick_list()

        layout = QtGui.QVBoxLayout()
        self.setLayout(layout)

        form = QtGui.QFormLayout()
        layout.addLayout(form)
        self.primary_list = QtGui.QComboBox(self)
        self.primary_list.addItems(joysticks)
        form.addRow("Primary Input:", self.primary_list)

        buttons = QtGui.QHBoxLayout()
        buttons.addStretch(1)
        layout.addLayout(buttons)
        no_button = QtGui.QPushButton("Cancel", self)
        no_button.clicked.connect(self.reject)
        buttons.addWidget(no_button)
        ok_button = QtGui.QPushButton("OK", self)
        ok_button.setDefault(True)
        ok_button.clicked.connect(self.ok_action)
        buttons.addWidget(ok_button)

        self.get_joystick_list()

    def get_joystick_list(self):
        joystick.init()
        joysticks = []
        for i in range(joystick.get_count()):
            stick = joystick.Joystick(i)
            joysticks.append(
                "{0}: {1}".format(i, stick.get_name())
            )

        return joysticks

    def ok_action(self):
        self.primary = self.primary_list.currentIndex()
        self.accept()

    def get_primary(self):
        return self.primary
