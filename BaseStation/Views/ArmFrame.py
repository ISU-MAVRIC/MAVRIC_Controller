from PySide import QtGui

class ArmFrame(QtGui.QGroupBox):
    """A widget to display info about the arm system."""

    def __init__(self, parent):
        """Create and initialize an ArmFrame.

        Args:
            parent (QWidget): Parent Qt widget.
        """
        super(ArmFrame, self).__init__('Arm', parent)

        self._initUI()

    def _initUI(self):
        """A private method to setup the UI."""
        # Main layout
        arm_layout = QtGui.QVBoxLayout()
        self.setLayout(arm_layout)

        # Graphical display frame
        arm_display_frame = QtGui.QFrame(self)
        arm_layout.addWidget(arm_display_frame)

        # Info layout
        arm_info_layout = QtGui.QFormLayout()
        arm_layout.addLayout(arm_info_layout)

        # Azimuth display
        azimuth_layout = QtGui.QHBoxLayout()
        self.azimuth_field = QtGui.QLineEdit(self)
        self.azimuth_field.setReadOnly(True)
        self.azimuth_bar = QtGui.QProgressBar(self)
        azimuth_layout.addWidget(self.azimuth_field)
        azimuth_layout.addWidget(self.azimuth_bar)
        arm_info_layout.addRow('Azimuth Angle:', azimuth_layout)

        # Shoulder display
        shoulder_layout = QtGui.QHBoxLayout()
        self.shoulder_field = QtGui.QLineEdit(self)
        self.shoulder_field.setReadOnly(True)
        self.shoulder_bar = QtGui.QProgressBar(self)
        shoulder_layout.addWidget(self.shoulder_field)
        shoulder_layout.addWidget(self.shoulder_bar)
        arm_info_layout.addRow('Shoulder Angle:', shoulder_layout)

        # Elbow display
        elbow_layout = QtGui.QHBoxLayout()
        self.elbow_field = QtGui.QLineEdit(self)
        self.elbow_field.setReadOnly(True)
        self.elbow_bar = QtGui.QProgressBar(self)
        elbow_layout.addWidget(self.elbow_field)
        elbow_layout.addWidget(self.elbow_bar)
        arm_info_layout.addRow('Elbow Angle:', elbow_layout)
