from PySide import QtCore, QtGui

class VitalsWidget(QtGui.QDockWidget):
    """A dockable widget to display rover vitals."""

    def __init__(self, parent=None):
        """Create and initialize a VitalsWidget.

        Args:
            parent (QWidget): Parent Qt widget.
        """
        super(VitalsWidget, self).__init__("Vitals", parent)
        self.setAllowedAreas(
            QtCore.Qt.DockWidgetArea.LeftDockWidgetArea |
            QtCore.Qt.DockWidgetArea.RightDockWidgetArea)
        self._initUI()

    def _initUI(self):
        """Private method to setup the widget UI."""
        # Create content frame
        frame = QtGui.QFrame()
        self.setWidget(frame)

        # Create primary layout
        layout = QtGui.QVBoxLayout()
        frame.setLayout(layout)

        # Battery voltage display
        layout.addWidget(QtGui.QLabel("Voltage:", frame))
        self.voltage_display = QtGui.QLCDNumber(frame)
        self.voltage_display.setDigitCount(4)
        self.voltage_display.setSegmentStyle(QtGui.QLCDNumber.SegmentStyle.Flat)
        self.voltage_display.display(12.4)
        layout.addWidget(self.voltage_display)
        self.voltage_bar = QtGui.QProgressBar(frame)
        self.voltage_bar.setTextVisible(True)
        layout.addWidget(self.voltage_bar)

        # Current consumption display
        layout.addWidget(QtGui.QLabel("Current:", frame))
        self.current_bar = QtGui.QProgressBar(frame)
        self.current_bar.setTextVisible(True)
        layout.addWidget(self.current_bar)

        # Radio link health display
        layout.addWidget(QtGui.QLabel("Packet Rate:", frame))
        self.packet_bar = QtGui.QProgressBar(frame)
        self.packet_bar.setTextVisible(True)
        layout.addWidget(self.packet_bar)

        # Expand layout to fill bottom of frame
        layout.addStretch(1)
