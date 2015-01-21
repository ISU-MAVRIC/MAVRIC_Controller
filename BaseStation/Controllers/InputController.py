import math

from pygame import event, joystick
from PySide import QtCore

class InputController(QtCore.QObject):
    """A class to interface with the joysticks."""

    def __init__(self, controller, parent):
        """Construct and initialize a InputController.

        Args:
            controller (CommandController): CommandController instance for
                encoding and decoding commands.
            parent (QObject): Parent Qt object.
        """
        super(InputController, self).__init__(parent)
        self.controller = controller

        self.settings = QtCore.QSettings()
        self.primary = None
        self.secondary = None

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self._update)

        self.configure()

    def configure(self):
        """Load the configuration from the application settings object."""
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

        self.arm_azimuth = {
            'control': self.settings.value('input/map/arm_azimuth/control'),
            'axis': self.settings.value('input/map/arm_azimuth/axis'),
            'expo': float(self.settings.value('input/map/arm_azimuth/expo')),
            'reverse': self.settings.value('input/map/arm_azimuth/reverse') == 'true'
        }

        self.arm_shoulder = {
            'control': self.settings.value('input/map/arm_shoulder/control'),
            'axis': self.settings.value('input/map/arm_shoulder/axis'),
            'expo': float(self.settings.value('input/map/arm_shoulder/expo')),
            'reverse': self.settings.value('input/map/arm_shoulder/reverse') == 'true'
        }

        self.arm_elbow = {
            'control': self.settings.value('input/map/arm_elbow/control'),
            'axis': self.settings.value('input/map/arm_elbow/axis'),
            'expo': float(self.settings.value('input/map/arm_elbow/expo')),
            'reverse': self.settings.value('input/map/arm_elbow/reverse') == 'true'
        }

    def _update(self):
        """Timer callback function."""
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

        if self.arm_azimuth['control'] == 0:
            arm_azimuth_stick = self.primary
        else:
            arm_azimuth_stick = self.secondary
        azimuth_raw = arm_azimuth_stick.get_axis(self.arm_azimuth['axis'])
        azimuth_out = self.expo(azimuth_raw, self.arm_azimuth['expo'])
        if self.arm_azimuth['reverse']: azimuth_out = -1.0 * azimuth_out

        if self.arm_shoulder['control'] == 0:
            arm_shoulder_stick = self.primary
        else:
            arm_shoulder_stick = self.secondary
        shoulder_raw = arm_shoulder_stick.get_axis(self.arm_shoulder['axis'])
        shoulder_out = self.expo(shoulder_raw, self.arm_shoulder['expo'])
        if self.arm_shoulder['reverse']: shoulder_out = -1.0 * shoulder_out

        if self.arm_elbow['control'] == 0:
            arm_elbow_stick = self.primary
        else:
            arm_elbow_stick = self.secondary
        elbow_raw = arm_elbow_stick.get_axis(self.arm_elbow['axis'])
        elbow_out = self.expo(elbow_raw, self.arm_elbow['expo'])
        if self.arm_elbow['reverse']: elbow_out = -1.0 * elbow_out

        #self.controller.arm_speed_command(azimuth_out, shoulder_out, elbow_out)
        self.controller.camera_pos_command(azimuth_out, shoulder_out)


    @staticmethod
    def expo(raw, expo):
        uraw = abs(raw)
        out = math.pow(uraw, expo)
        return math.copysign(uraw, raw)
