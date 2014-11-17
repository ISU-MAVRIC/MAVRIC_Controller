from PySide import QtCore

class DriveController(QtCore.QObject):

    width = 0.5
    lead = 0.5
    lag = 0.5

    def __init__(self, parent=None):
        super(DriveController, self).__init__(parent)

    def compute(self, left, right):
        left_drive = int(round((127.0 * left) + 127))
        right_drive = int(round((127.0 * right) + 127))

        return [left_drive, left_drive, left_drive,
            right_drive, right_drive, right_drive], [0, 0, 0, 0, 0, 0]
