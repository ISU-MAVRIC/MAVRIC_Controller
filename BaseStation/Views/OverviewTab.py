from PySide import QtCore, QtGui

from ArmFrame import *
from CameraFrame import *
from PropulsionFrame import *

class OverviewTab(QtGui.QWidget):

    def __init__(self, parent=None):
        super(OverviewTab, self).__init__(parent)
        self.initUI()

    def initUI(self):
        layout = QtGui.QHBoxLayout()
        splitter = QtGui.QSplitter(QtCore.Qt.Horizontal)

        info_frame = QtGui.QFrame(self)
        splitter.addWidget(info_frame)
        info_layout = QtGui.QHBoxLayout()
        info_frame.setLayout(info_layout)

        left_layout = QtGui.QVBoxLayout()

        camera_frame = CameraFrame(info_frame)
        left_layout.addWidget(camera_frame)

        propulsion_frame = PropulsionFrame(info_frame)
        left_layout.addWidget(propulsion_frame)

        info_layout.addLayout(left_layout)

        arm_frame = ArmFrame(info_frame)
        info_layout.addWidget(arm_frame)

        map_frame = QtGui.QFrame(self)
        splitter.addWidget(map_frame)
        map_layout = QtGui.QVBoxLayout()
        map_frame.setLayout(map_layout)
        map_layout.addWidget(QtGui.QLabel("Map", map_frame))
        map_layout.addStretch(1)

        layout.addWidget(splitter)
        self.setLayout(layout)
