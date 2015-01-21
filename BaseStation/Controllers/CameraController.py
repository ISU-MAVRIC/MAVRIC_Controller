from PySide import QtCore


class CameraController(QtCore.QObject):
    """A class to abstract controlling the arm."""

    pan_speed = 5
    tilt_speed = 5

    pan_pos = 127;
    tilt_pos = 127;

    def __init__(self, parent=None):
        """Construct and initialize an ArmController.

        Args:
            parent (QObject): Parent Qt object.
        """
        super(CameraController, self).__init__(parent)

    def compute(self, pan, tilt):
        """Compute the speed values to send to the rover.

        Args:
            pan (float): Float [-1,1] representing the position of panning.
            tilt (float): Float [-1,1] representing the position of tilting.
            elbow (float): Float [-1,1] representing the speed of elbow rotation.

        Returns:
            Azimuth output  int [0,255].
            Shoulder output int [0,255].
            Elbow output int [0,255].
        """
        self.pan_pos += int(pan * self.pan_speed)
        self.pan_pos = clamp(self.pan_pos, 0, 255)
        self.tilt_pos += int(tilt * self.tilt_speed)
        self.tilt_pos = clamp(self.tilt_pos, 0, 255)

        return self.pan_pos, self.tilt_pos


def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)