from PySide import QtCore


class DriveController(QtCore.QObject):
    """A class to abstract controlling the drive."""

    width = 0.5
    lead = 0.5
    lag = 0.5

    def __init__(self, parent=None):
        """Create an initialize a DriveController.

        Args:
            parent (QObject): Parent Qt object.
        """
        super(DriveController, self).__init__(parent)

    def compute(self, left, right):
        """

        Args:
            left (float): Float [-1,1] representing the speed of the left side.
            right (float): Float [-1,1] representing the speed of the right side.

        Returns:
            An array of ints [0,255] representing the speed of each wheel.
            An array of ints [0,255] representing the steering angle of each wheel.
        """
        left_drive = int(round((127.0 * left) + 127))
        right_drive = int(round((127.0 * right) + 127))

        return [left_drive, left_drive, left_drive,
                right_drive, right_drive, right_drive], [0, 0, 0, 0, 0, 0]
