from PySide import QtCore

class ArmController(QtCore.QObject):
    """A class to abstract controlling the arm."""

    azimuth_speed = 1.0
    shoulder_speed = 1.0
    elbow_speed = 1.0

    def __init__(self, parent=None):
        """Construct and initialize an ArmController.

        Args:
            parent (QObject): Parent Qt object.
        """
        super(ArmController, self).__init__(parent)

    def compute_speed(self, azimuth, shoulder, elbow):
        """Compute the speed values to send to the rover.

        Args:
            azimuth (float): Float [-1,1] representing the speed of azimuth rotation.
            shoulder (float): Float [-1,1] representing the speed of shoulder rotation.
            elbow (float): Float [-1,1] representing the speed of elbow rotation.

        Returns:
            Azimuth output  int [0,255].
            Shoulder output int [0,255].
            Elbow output int [0,255].
        """
        a = int(round((127.0 * azimuth * self.azimuth_speed) + 127))
        s = int(round((127.0 * shoulder * self.shoulder_speed) + 127))
        e = int(round((127.0 * elbow * self.elbow_speed) + 127))

        return a, s, e
