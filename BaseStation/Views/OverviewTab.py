from PySide import QtCore, QtGui

from ArmFrame import *
from CameraFrame import *
from PropulsionFrame import *

class OverviewTab(QtGui.QWidget):
    """A view for overall operating status of the rover."""

    def __init__(self, parent=None):
        """Create and initialize an OverviewTab.

        Args:
            parent (QWidget): Parent Qt widget.
        """
        super(OverviewTab, self).__init__(parent)

        self._initUI()

    def _initUI(self):
        """A private method to setup the UI."""
        # Create the main layout
        layout = QtGui.QHBoxLayout()
        self.setLayout(layout)

        # Create an adjustable horizontal split
        splitter = QtGui.QSplitter(QtCore.Qt.Horizontal)
        layout.addWidget(splitter)

        # Create a frame for status widgets
        info_frame = QtGui.QFrame(self)
        splitter.addWidget(info_frame)
        info_layout = QtGui.QHBoxLayout()
        info_frame.setLayout(info_layout)

        # Create a layout to stack the leftmost widgets
        left_layout = QtGui.QVBoxLayout()
        info_layout.addLayout(left_layout)

        # Camera info frame
        camera_frame = CameraFrame(info_frame)
        left_layout.addWidget(camera_frame)

        # Propulsion info frame
        propulsion_frame = PropulsionFrame(info_frame)
        left_layout.addWidget(propulsion_frame)

        # Arm info frame
        arm_frame = ArmFrame(info_frame)
        info_layout.addWidget(arm_frame)

        # Create a frame for the map info
        map_frame = QtGui.QFrame(self)
        splitter.addWidget(map_frame)
        map_layout = QtGui.QVBoxLayout()
        map_frame.setLayout(map_layout)
        map_layout.addWidget(QtGui.QLabel("Map", map_frame))
        map_layout.addStretch(1)
