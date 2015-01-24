from PySide import QtCore


class CameraModel(QtCore.QObject):

    def __init__(self):

        super(CameraModel, self).__init__()
        self.azimuth_pos = 127
        self.pan_pos = 127
        self.tilt_pos = 127
