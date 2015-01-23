import math

from pygame import event, joystick, error
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

        try:
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

        # pygame error
        except error as message:
            print "Error restoring saved joystick configuration ..."
            print message

        """
        SETTINGS GUIDE
        **************
        control: joystick number
        use_axis: true if using axis, false if using button(s)
        axis: axis number
        button_p: button number for the positive side of the action
        button_n: button number for the negative side of the action
        button_speed: [0 - 1.0] button push should emulate axis value at this level
        expo: exponential response for axis control
        invert: true if forward on axis should equal negative value
        """

        """Resets all expo values if one of them is unset/invalid"""
        try:
            # left_drive chosen for no particular reason. Change this to check all vals later
            float(self.settings.value('input/map/left_drive/expo'))
        except TypeError:
            self.settings.setValue('input/map/left_drive/expo', 1.5)
            self.settings.setValue('input/map/right_drive/expo', 1.5)
            self.settings.setValue('input/map/arm_azimuth/expo', 1.5)
            self.settings.setValue('input/map/arm_shoulder/expo', 1.5)
            self.settings.setValue('input/map/arm_elbow/expo', 1.5)
            self.settings.setValue('input/map/camera_pan/expo', 1.5)
            self.settings.setValue('input/map/camera_tilt/expo', 1.5)

        self.left_drive = {
            'control': self.settings.value('input/map/left_drive/control'),
            'axis': self.settings.value('input/map/left_drive/axis'),
            'expo': float(self.settings.value('input/map/left_drive/expo')),
            'invert': self.settings.value('input/map/left_drive/invert') == 'true'
        }

        self.right_drive = {
            'control': self.settings.value('input/map/right_drive/control'),
            'axis': self.settings.value('input/map/right_drive/axis'),
            'expo': float(self.settings.value('input/map/right_drive/expo')),
            'invert': self.settings.value('input/map/right_drive/invert') == 'true'
        }

        self.arm_azimuth = {
            'control': self.settings.value('input/map/arm_azimuth/control'),
            'axis': self.settings.value('input/map/arm_azimuth/axis'),
            'expo': float(self.settings.value('input/map/arm_azimuth/expo')),
            'invert': self.settings.value('input/map/arm_azimuth/invert') == 'true'
        }

        self.arm_shoulder = {
            'control': self.settings.value('input/map/arm_shoulder/control'),
            'axis': self.settings.value('input/map/arm_shoulder/axis'),
            'expo': float(self.settings.value('input/map/arm_shoulder/expo')),
            'invert': self.settings.value('input/map/arm_shoulder/invert') == 'true'
        }

        self.arm_elbow = {
            'control': self.settings.value('input/map/arm_elbow/control'),
            'axis': self.settings.value('input/map/arm_elbow/axis'),
            'expo': float(self.settings.value('input/map/arm_elbow/expo')),
            'invert': self.settings.value('input/map/arm_elbow/invert') == 'true'
        }

        # using input instead of axis since many functions will be mapped to buttons
        self.camera_pan = {
            'control': self.settings.value('input/map/camera_pan/control'),
            'use_axis': self.settings.value('input/map/camera_pan/use_axis'),
            'axis': self.settings.value('input/map/camera_pan/axis'),
            'button_p': self.settings.value('input/map/camera_pan/button_p'),
            'button_n': self.settings.value('input/map/camera_pan/button_n'),
            'button_speed': self.settings.value('input/map/camera_pan/button_speed'),
            'expo': float(self.settings.value('input/map/camera_pan/expo')),
            'invert': self.settings.value('input/map/camera_pan/invert') == 'true'
        }

        self.camera_tilt = {
            'control': self.settings.value('input/map/camera_tilt/control'),
            'use_axis': self.settings.value('input/map/camera_tilt/use_axis'),
            'axis': self.settings.value('input/map/camera_tilt/axis'),
            'button_p': self.settings.value('input/map/camera_pan/button_p'),
            'button_n': self.settings.value('input/map/camera_pan/button_n'),
            'button_speed': self.settings.value('input/map/camera_pan/button_speed'),
            'expo': float(self.settings.value('input/map/camera_tilt/expo')),
            'invert': self.settings.value('input/map/camera_tilt/invert') == 'true'
        }

    def _update(self):
        """Timer callback function."""
        event.pump()

        """LEFT DRIVE"""
        if self.left_drive['control'] == 0:
            left_drive_stick = self.primary
        else:
            left_drive_stick = self.secondary
        left_raw = left_drive_stick.get_axis(self.left_drive['axis'])
        left_out = self.expo(left_raw, self.left_drive['expo'])
        if self.left_drive['invert']: left_out = -1.0 * left_out

        """RIGHT DRIVE"""
        if self.right_drive['control'] == 0:
            right_drive_stick = self.primary
        else:
            right_drive_stick = self.secondary
        right_raw = right_drive_stick.get_axis(self.right_drive['axis'])
        right_out = self.expo(right_raw, self.right_drive['expo'])
        if self.right_drive['invert']: right_out = -1.0 * right_out

        self.controller.drive_command(left_out, right_out)

        """ARM AZIMUTH"""
        if self.arm_azimuth['control'] == 0:
            arm_azimuth_stick = self.primary
        else:
            arm_azimuth_stick = self.secondary
        azimuth_raw = arm_azimuth_stick.get_axis(self.arm_azimuth['axis'])
        azimuth_out = self.expo(azimuth_raw, self.arm_azimuth['expo'])
        if self.arm_azimuth['invert']: azimuth_out = -1.0 * azimuth_out

        """ARM SHOULDER"""
        if self.arm_shoulder['control'] == 0:
            arm_shoulder_stick = self.primary
        else:
            arm_shoulder_stick = self.secondary
        shoulder_raw = arm_shoulder_stick.get_axis(self.arm_shoulder['axis'])
        shoulder_out = self.expo(shoulder_raw, self.arm_shoulder['expo'])
        if self.arm_shoulder['invert']: shoulder_out = -1.0 * shoulder_out

        """ARM ELBOW"""
        if self.arm_elbow['control'] == 0:
            arm_elbow_stick = self.primary
        else:
            arm_elbow_stick = self.secondary
        elbow_raw = arm_elbow_stick.get_axis(self.arm_elbow['axis'])
        elbow_out = self.expo(elbow_raw, self.arm_elbow['expo'])
        if self.arm_elbow['invert']: elbow_out = -1.0 * elbow_out

        # self.controller.arm_speed_command(azimuth_out, shoulder_out, elbow_out)

        """CAMERA PAN"""
        if self.camera_pan['control'] == 0:
            camera_pan_stick = self.primary
        else:
            camera_pan_stick = self.secondary

        if self.camera_pan['use_axis']:
            pan_raw = camera_pan_stick.get_axis(self.camera_pan['axis'])
            pan_out = self.expo(pan_raw, self.camera_pan['expo'])
            if self.camera_pan['invert']:
                pan_out *= -1.0
        else:
            # pressing both buttons causes them to cancel out
            pan_raw = camera_pan_stick.get_button(self.camera_pan['button_p']) - \
                      camera_pan_stick.get_button(self.camera_pan['button_n'])
            pan_out = pan_raw * self.camera_pan['button_speed']

        # """CAMERA TILT"""
        # if self.camera_tilt['control'] == 0:
        #     camera_tilt_stick = self.primary
        # else:
        #     camera_tilt_stick = self.secondary
        #
        # if self.camera_tilt['use_axis']:
        #     tilt_raw = camera_tilt_stick.get_axis(self.camera_tilt['axis'])
        #     tilt_out = self.expo(tilt_raw, self.camera_tilt['expo'])
        #     if self.camera_tilt['invert']:
        #         tilt_out *= -1.0
        # else:
        #     # pressing both buttons causes them to cancel out
        #     tilt_raw = camera_tilt_stick.get_button(self.camera_tilt['button_p']) - \
        #                camera_tilt_stick.get_button(self.camera_tilt['button_n'])
        #     tilt_out = tilt_raw * self.camera_tilt['button_speed']

        tilt_out = 255

        self.controller.camera_pos_command(pan_out, tilt_out)


    @staticmethod
    def expo(raw, expo):
        uraw = abs(raw)
        out = math.pow(uraw, expo)
        return math.copysign(uraw, raw)
