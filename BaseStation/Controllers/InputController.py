import math

from pygame import event, joystick
from PySide import QtCore

class InputController(QtCore.QObject):

    def __init__(self, controller, parent):
        super(InputController, self).__init__(parent)
        self.controller = controller

        self.settings = QtCore.QSettings()
        self.primary = None
        self.secondary = None

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update)

        self.configure()

    def configure(self):
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

        secondary_index = self.settings.value('input/secondary/index')
        if secondary_index is not None:
            self.secondary = joystick.Joystick(secondary_index)
            self.secondary.init()

        self.left_drive = {
            'control': self.settings.value('input/map/left_drive/control'),
            'axis': self.settings.value('input/map/left_drive/axis'),
            'expo': float(self.settings.value('input/map/left_drive/expo')),
            'reverse': self.settings.value('input/map/left_drive/reverse') == 'true'
        }

        self.right_drive = {
            'control': self.settings.value('input/map/right_drive/control'),
            'axis': self.settings.value('input/map/right_drive/axis'),
            'expo': float(self.settings.value('input/map/right_drive/expo')),
            'reverse': self.settings.value('input/map/right_drive/reverse') == 'true'
        }

    def update(self):
        event.pump()

        if self.left_drive['control'] == 0:
            left_drive_stick = self.primary
        else:
            left_drive_stick = self.secondary
        left_raw = left_drive_stick.get_axis(self.left_drive['axis'])
        left_out = self.expo(left_raw, self.left_drive['expo'])
        if self.left_drive['reverse']: left_out = -1.0 * left_out

        if self.right_drive['control'] == 0:
            right_drive_stick = self.primary
        else:
            right_drive_stick = self.secondary
        right_raw = right_drive_stick.get_axis(self.right_drive['axis'])
        right_out = self.expo(right_raw, self.right_drive['expo'])
        if self.right_drive['reverse']: right_out = -1.0 * right_out

        self.controller.drive_command(left_out, right_out)

    @staticmethod
    def expo(raw, expo):
        uraw = abs(raw)
        out = math.pow(uraw, expo)
        return math.copysign(uraw, raw)
