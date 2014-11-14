import math

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
        if joystick.get_count() == 0:
            print "No controls detected!"
            return

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
            print "{0:+0.4f} {1:+0.4f} {2:+0.4f} {3:+0.4f}".format(
                self.expo(self.primary.get_axis(0), 1.5),
                self.expo(self.primary.get_axis(1), 1.5),
                self.expo(self.primary.get_axis(2), 1.0),
                self.expo(self.primary.get_axis(3), 1.5)
            )

    @staticmethod
    def expo(raw, expo):
        uraw = abs(raw)
        out = math.pow(uraw, expo)
        return math.copysign(uraw, raw)
