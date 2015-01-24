from PySide import QtCore

class CameraController(QtCore.QObject):

    def __init__(self, input_model, camera_model, parent):
        """Construct and initialize a CameraController.

        Args:
            parent (QObject): Parent Qt object.
        """
        super(CameraController, self).__init__(parent)

        self.input_model = input_model
        self.camera_model = camera_model

    def _update(self):
        """Compute the position values to send to the rover

        Args:
            pan (float): Float [-1,1] representing the position of panning.
            tilt (float): Float [-1,1] representing the position of tilting.

        Returns:
            Pan output  int [0,255].
            Tilt output int [0,255].
        """

        self.camera_model.pan_pos += int(self.input_model.pan_in * self.pan_speed)
        self.camera_model.pan_pos = clamp(self.pan_pos, 0, 255)
        self.camera_model.tilt_pos += int(self.input_model.tilt_in * self.tilt_speed)
        self.camera_model.tilt_pos = clamp(self.tilt_pos, 0, 255)

        # should be somewhere else, here for the POC

        print "<cc {:03d} {:03d} >".format(
            self.camera_model.pan_pos,
            self.camera_model.tilt_pos
        )


def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)