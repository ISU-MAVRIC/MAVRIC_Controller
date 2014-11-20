from PySide import QtCore

class ArmController(QtCore.QObject):

    azimuth_speed = 1.0
    shoulder_speed = 1.0
    elbow_speed = 1.0

    def __init__(self, parent=None):
        super(ArmController, self).__init__(parent)

    def compute_speed(self, azimuth, shoulder, elbow):
        a = int(round((127.0 * azimuth * self.azimuth_speed) + 127))
        s = int(round((127.0 * shoulder * self.shoulder_speed) + 127))
        e = int(round((127.0 * elbow * self.elbow_speed) + 127))

        return a, s, e
