from pygame import event, joystick
from PySide import QtCore

class InputController(QtCore.QObject):

    def __init__(self, parent):
        super(InputController, self).__init__(parent)

        self.settings = QtCore.QSettings()
        self.primary = None

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update)

        self.configure_input()

    def configure_input(self):
        primary_index = self.settings.value('input/primary/index')
        if primary_index is not None:
            self.primary = joystick.Joystick(primary_index)
            self.primary.init()
            self.timer.start(100)
        else:
            self.timer.stop()

    def update(self):
        event.pump()
        if self.primary is not None:
            print "{0} {1} {2} {3}".format(
                self.primary.get_axis(0),
                self.primary.get_axis(1),
                self.primary.get_axis(2),
                self.primary.get_axis(3),
            )
