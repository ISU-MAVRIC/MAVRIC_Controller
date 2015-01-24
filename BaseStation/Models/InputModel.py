from PySide import QtCore


class InputModel(QtCore.QObject):

    def __init__(self):

        super(InputModel, self).__init__()
        self.drive_left_in = 0.0
        self.drive_right_in = 0.0

        self.arm_azimuth_in = 0.0
        self.arm_shoulder_in = 0.0
        self.arm_elbow_in = 0.0

        self.pan_in = 0.0
        self.tilt_in = 0.0
