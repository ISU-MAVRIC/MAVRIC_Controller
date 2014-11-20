from PySide import QtGui

class CameraFrame(QtGui.QGroupBox):
    """A widget to display info about the camera system."""

    def __init__(self, parent=None):
        """Create and initialize a CameraFrame.

        Args:
            parent (QWidget): Parent Qt widget.
        """
        super(CameraFrame, self).__init__('Camera', parent)

        self._initUI()

    def _initUI(self):
        """A private method to setup the UI."""
        # Create the main layout
        layout = QtGui.QFormLayout()
        self.setLayout(layout)

        # Pan display widgets
        pan_layout = QtGui.QHBoxLayout()
        self.pan_field = QtGui.QLineEdit(self)
        self.pan_field.setReadOnly(True)
        pan_layout.addWidget(self.pan_field)
        self.pan_bar = QtGui.QProgressBar(self)
        pan_layout.addWidget(self.pan_bar)
        layout.addRow('Pan:', pan_layout)

        # Tilt display widgets
        tilt_layout = QtGui.QHBoxLayout()
        self.tilt_field = QtGui.QLineEdit(self)
        self.tilt_field.setReadOnly(True)
        tilt_layout.addWidget(self.tilt_field)
        self.tilt_bar = QtGui.QProgressBar(self)
        tilt_layout.addWidget(self.tilt_bar)
        layout.addRow('Tilt:', tilt_layout)

        # Zoom display widgets
        zoom_layout = QtGui.QHBoxLayout()
        self.zoom_field = QtGui.QLineEdit(self)
        self.zoom_field.setReadOnly(True)
        zoom_layout.addWidget(self.zoom_field)
        self.zoom_bar = QtGui.QProgressBar(self)
        zoom_layout.addWidget(self.zoom_bar)
        layout.addRow('Zoom:', zoom_layout)
