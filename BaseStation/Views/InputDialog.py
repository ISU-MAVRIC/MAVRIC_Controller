from pygame import joystick
from PySide import QtCore, QtGui

class InputDialog(QtGui.QDialog):
    """A dialog to configure input settings and devices."""

    # List of controller names
    controllers = ['Primary', 'Secondary']
    # List of axes
    axes = ['0', '1', '2', '3', '4', '5', '6', '7']

    def __init__(self, parent):
        """Create and initialize an InputDialog.

        Args:
            parent (QWidget): Parent Qt widget.
        """
        super(InputDialog, self).__init__(parent)
        self.setWindowTitle('Configure input devices')

        # Get an instance of the settings object
        self.settings = QtCore.QSettings()

        # Setup the UI
        self._initUI()

    def _initUI(self):
        """ A private method to setup the UI."""
        # Get a list of connected joysticks
        joysticks = self.get_joystick_list()

        # Main layout
        layout = QtGui.QVBoxLayout()
        self.setLayout(layout)

        # Form layout for input devices
        form = QtGui.QFormLayout()
        layout.addLayout(form)

        # Primary controller selection
        self.primary_list = QtGui.QComboBox(self)
        self.primary_list.addItems(joysticks)
        self.primary_list.setCurrentIndex(0)
        # Attempt to get saved value
        primary_index = self.settings.value('input/primary/index')
        if primary_index is not None:
            # Ensure the controller exists
            if primary_index < (len(joysticks) - 1):
                # Set the controller
                self.primary_list.setCurrentIndex(
                    primary_index + 1
                )
        form.addRow("Primary Input:", self.primary_list)

        # Secondary controller selection
        self.secondary_list = QtGui.QComboBox(self)
        self.secondary_list.addItems(joysticks)
        self.secondary_list.setCurrentIndex(0)
        # Attempt to get saved value
        secondary_index = self.settings.value('input/secondary/index')
        if secondary_index is not None:
            # Ensure the controller exists
            if secondary_index < (len(joysticks) - 1):
                # Set the controller
                self.secondary_list.setCurrentIndex(
                    secondary_index + 1
                )
        form.addRow("Secondary Input:", self.secondary_list)

        # Create a divider
        divider = QtGui.QFrame(self)
        divider.setFrameShape(QtGui.QFrame.Shape.HLine)
        divider.setFrameShadow(QtGui.QFrame.Shadow.Sunken)
        layout.addWidget(divider)

        # Control map layout
        map_layout = QtGui.QGridLayout()
        layout.addLayout(map_layout)

        # Control map headings
        map_layout.addWidget(QtGui.QLabel('Controller:', self), 0, 1)
        map_layout.addWidget(QtGui.QLabel('Axis:', self), 0, 2)
        map_layout.addWidget(QtGui.QLabel('Expo:', self), 0, 3)
        map_layout.addWidget(QtGui.QLabel('Invert:', self), 0, 4)
        map_layout.addWidget(QtGui.QLabel('Use\nAxis:', self), 0, 5)
        map_layout.addWidget(QtGui.QLabel('Button Assign:', self), 0, 6)
        map_layout.addWidget(QtGui.QLabel('Button Speed:', self), 0, 7)

        # Get saved left_drive settings
        left_control_index = self.settings.value('input/map/left_drive/control')
        left_axis_index = self.settings.value('input/map/left_drive/axis')
        left_expo = self.settings.value('input/map/left_drive/expo', 1.5)
        left_invert = self.settings.value('input/map/left_drive/invert') == 'true'

        # Get saved right_drive settings
        right_control_index = self.settings.value('input/map/right_drive/control')
        right_axis_index = self.settings.value('input/map/right_drive/axis')
        right_expo = self.settings.value('input/map/right_drive/expo', 1.5)
        right_invert = self.settings.value('input/map/right_drive/invert') == 'true'

        # Get saved arm_azimuth settings
        azimuth_control_index = self.settings.value('input/map/arm_azimuth/control')
        azimuth_axis_index = self.settings.value('input/map/arm_azimuth/axis')
        azimuth_expo = self.settings.value('input/map/arm_azimuth/expo', 1.5)
        azimuth_invert = self.settings.value('input/map/arm_azimuth/invert') == 'true'

        # Get saved arm_shoulder settings
        shoulder_control_index = self.settings.value('input/map/arm_shoulder/control')
        shoulder_axis_index = self.settings.value('input/map/arm_shoulder/axis')
        shoulder_expo = self.settings.value('input/map/arm_shoulder/expo', 1.5)
        shoulder_invert = self.settings.value('input/map/arm_shoulder/invert') == 'true'

        # Get saved arm_elbow settings
        elbow_control_index = self.settings.value('input/map/arm_elbow/control')
        elbow_axis_index = self.settings.value('input/map/arm_elbow/axis')
        elbow_expo = self.settings.value('input/map/arm_elbow/expo', 1.5)
        elbow_invert = self.settings.value('input/map/arm_elbow/invert') == 'true'

        # Get saved camera_pan settings
        pan_control_index = self.settings.value('input/map/camera_pan/control')
        pan_use_axis = self.settings.value('input/map/camera_pan/use_axis') == 'true'
        pan_axis_index = self.settings.value('input/map/camera_pan/axis')
        pan_button_p = self.settings.value('input/map/camera_pan/button_p')
        pan_button_n = self.settings.value('input/map/camera_pan/button_n')
        pan_button_speed = self.settings.value('input/map/camera_pan/button_speed', 0.1)
        pan_expo = self.settings.value('input/map/camera_pan/expo', 1.5)
        pan_invert = self.settings.value('input/map/camera_pan/invert') == 'true'

        # Get saved camera_tilt settings
        tilt_control_index = self.settings.value('input/map/camera_tilt/control')
        tilt_use_axis = self.settings.value('input/map/camera_tilt/use_axis') == 'true'
        tilt_axis_index = self.settings.value('input/map/camera_tilt/axis')
        tilt_button_p = self.settings.value('input/map/camera_tilt/button_p')
        tilt_button_n = self.settings.value('input/map/camera_tilt/button_n')
        tilt_button_speed = self.settings.value('input/map/camera_tilt/button_speed', 0.1)
        tilt_expo = self.settings.value('input/map/camera_tilt/expo', 1.5)
        tilt_invert = self.settings.value('input/map/camera_tilt/invert') == 'true'


        # left_drive setting widgets
        map_layout.addWidget(QtGui.QLabel('Left Drive:', self), 1, 0,
            QtCore.Qt.AlignmentFlag.AlignRight)
        self.left_control = QtGui.QComboBox(self)
        self.left_control.addItems(self.controllers)
        if left_control_index is not None:
            self.left_control.setCurrentIndex(left_control_index)
        map_layout.addWidget(self.left_control, 1, 1)
        self.left_axis = QtGui.QComboBox(self)
        self.left_axis.addItems(self.axes)
        if left_axis_index is not None:
            self.left_axis.setCurrentIndex(left_axis_index)
        map_layout.addWidget(self.left_axis, 1, 2)
        self.left_expo = QtGui.QLineEdit(self)
        if left_expo is not None:
            self.left_expo.setText(str(left_expo))
        map_layout.addWidget(self.left_expo, 1, 3)
        self.left_invert = QtGui.QCheckBox(self)
        if left_invert is not None:
            self.left_invert.setChecked(left_invert)
        map_layout.addWidget(self.left_invert, 1, 4)

        # right_drive setting widgets
        map_layout.addWidget(QtGui.QLabel('Right Drive:', self), 2, 0,
            QtCore.Qt.AlignmentFlag.AlignRight)
        self.right_control = QtGui.QComboBox(self)
        self.right_control.addItems(self.controllers)
        if right_control_index is not None:
            self.right_control.setCurrentIndex(right_control_index)
        map_layout.addWidget(self.right_control, 2, 1)
        self.right_axis = QtGui.QComboBox(self)
        self.right_axis.addItems(self.axes)
        if right_axis_index is not None:
            self.right_axis.setCurrentIndex(right_axis_index)
        map_layout.addWidget(self.right_axis, 2, 2)
        self.right_expo = QtGui.QLineEdit(self)
        if right_expo is not None:
            self.right_expo.setText(str(right_expo))
        map_layout.addWidget(self.right_expo, 2, 3)
        self.right_invert = QtGui.QCheckBox(self)
        if right_invert is not None:
            self.right_invert.setChecked(right_invert)
        map_layout.addWidget(self.right_invert, 2, 4)

        # arm_azimuth setting widgets
        map_layout.addWidget(QtGui.QLabel('Arm Azimuth:', self), 3, 0,
            QtCore.Qt.AlignmentFlag.AlignRight)
        self.azimuth_control = QtGui.QComboBox(self)
        self.azimuth_control.addItems(self.controllers)
        if azimuth_control_index is not None:
            self.azimuth_control.setCurrentIndex(azimuth_control_index)
        map_layout.addWidget(self.azimuth_control, 3, 1)
        self.azimuth_axis = QtGui.QComboBox(self)
        self.azimuth_axis.addItems(self.axes)
        if azimuth_axis_index is not None:
            self.azimuth_axis.setCurrentIndex(azimuth_axis_index)
        map_layout.addWidget(self.azimuth_axis, 3, 2)
        self.azimuth_expo = QtGui.QLineEdit(self)
        if azimuth_expo is not None:
            self.azimuth_expo.setText(str(azimuth_expo))
        map_layout.addWidget(self.azimuth_expo, 3, 3)
        self.azimuth_invert = QtGui.QCheckBox(self)
        if azimuth_invert is not None:
            self.azimuth_invert.setChecked(azimuth_invert)
        map_layout.addWidget(self.azimuth_invert, 3, 4)

        # arm_shoulder setting widgets
        map_layout.addWidget(QtGui.QLabel('Arm Shoulder:', self), 4, 0,
            QtCore.Qt.AlignmentFlag.AlignRight)
        self.shoulder_control = QtGui.QComboBox(self)
        self.shoulder_control.addItems(self.controllers)
        if shoulder_control_index is not None:
            self.shoulder_control.setCurrentIndex(shoulder_control_index)
        map_layout.addWidget(self.shoulder_control, 4, 1)
        self.shoulder_axis = QtGui.QComboBox(self)
        self.shoulder_axis.addItems(self.axes)
        if shoulder_axis_index is not None:
            self.shoulder_axis.setCurrentIndex(shoulder_axis_index)
        map_layout.addWidget(self.shoulder_axis, 4, 2)
        self.shoulder_expo = QtGui.QLineEdit(self)
        if shoulder_expo is not None:
            self.shoulder_expo.setText(str(shoulder_expo))
        map_layout.addWidget(self.shoulder_expo, 4, 3)
        self.shoulder_invert = QtGui.QCheckBox(self)
        if shoulder_invert is not None:
            self.shoulder_invert.setChecked(shoulder_invert)
        map_layout.addWidget(self.shoulder_invert, 4, 4)

        # arm_elbow setting widgets
        map_layout.addWidget(QtGui.QLabel('Arm Elbow:', self), 5, 0,
            QtCore.Qt.AlignmentFlag.AlignRight)
        self.elbow_control = QtGui.QComboBox(self)
        self.elbow_control.addItems(self.controllers)
        if elbow_control_index is not None:
            self.elbow_control.setCurrentIndex(elbow_control_index)
        map_layout.addWidget(self.elbow_control, 5, 1)
        self.elbow_axis = QtGui.QComboBox(self)
        self.elbow_axis.addItems(self.axes)
        if elbow_axis_index is not None:
            self.elbow_axis.setCurrentIndex(elbow_axis_index)
        map_layout.addWidget(self.elbow_axis, 5, 2)
        self.elbow_expo = QtGui.QLineEdit(self)
        if elbow_expo is not None:
            self.elbow_expo.setText(str(elbow_expo))
        map_layout.addWidget(self.elbow_expo, 5, 3)
        self.elbow_invert = QtGui.QCheckBox(self)
        if elbow_invert is not None:
            self.elbow_invert.setChecked(elbow_invert)
        map_layout.addWidget(self.elbow_invert, 5, 4)

        ###############################
        #  camera_pan setting widgets #
        ###############################
        map_layout.addWidget(QtGui.QLabel('Camera Pan:', self), 6, 0,
                             QtCore.Qt.AlignmentFlag.AlignRight)
        # controller entry
        self.pan_control = QtGui.QComboBox(self)
        self.pan_control.addItems(self.controllers)
        if pan_control_index is not None:
            self.pan_control.setCurrentIndex(pan_control_index)
        map_layout.addWidget(self.pan_control, 6, 1)
        # axis entry
        self.pan_axis = QtGui.QComboBox(self)
        self.pan_axis.addItems(self.axes)
        if pan_axis_index is not None:
            self.pan_axis.setCurrentIndex(pan_axis_index)
        map_layout.addWidget(self.pan_axis, 6, 2)
        # expo entry
        self.pan_expo = QtGui.QLineEdit(self)
        if pan_expo is not None:
            self.pan_expo.setText(str(pan_expo))
        map_layout.addWidget(self.pan_expo, 6, 3)
        # invert controls check box
        self.pan_invert = QtGui.QCheckBox(self)
        if pan_invert is not None:
            self.pan_invert.setChecked(pan_invert)
        map_layout.addWidget(self.pan_invert, 6, 4)
        # use axis/buttons checkbox
        self.pan_use_axis = QtGui.QCheckBox(self)
        if pan_use_axis is not None:
            self.pan_use_axis.setChecked(pan_use_axis)
        self.pan_use_axis.setToolTip("Check to use axis instead of buttons")
        map_layout.addWidget(self.pan_use_axis, 6, 5)

        # positive and negative button boxes
        pan_buttons_layout = QtGui.QGridLayout()

        # positive button entry
        pan_buttons_layout.addWidget(QtGui.QLabel('Positive', self), 0, 0)
        self.pan_button_p = QtGui.QLineEdit(self)
        if pan_button_p is not None:
            self.pan_button_p.setText(str(pan_button_p))
        pan_buttons_layout.addWidget(self.pan_button_p, 0, 1)

        # negative button entry
        pan_buttons_layout.addWidget(QtGui.QLabel('Negative', self), 1, 0)
        self.pan_button_n = QtGui.QLineEdit(self)
        if pan_button_n is not None:
            self.pan_button_n.setText(str(pan_button_n))
        pan_buttons_layout.addWidget(self.pan_button_n, 1, 1)

        # add positive and negative button entries to main grid layout
        map_layout.addLayout(pan_buttons_layout, 6, 6)

        # button speed entry
        self.pan_button_speed = QtGui.QLineEdit(self)
        if pan_button_speed is not None:
            self.pan_button_speed.setText(str(pan_button_speed))
        map_layout.addWidget(self.pan_button_speed, 6, 7)

        ###############################
        # camera_tilt setting widgets #
        ###############################
        map_layout.addWidget(QtGui.QLabel('Camera Tilt:', self), 7, 0,
                             QtCore.Qt.AlignmentFlag.AlignRight)
        # controller entry
        self.tilt_control = QtGui.QComboBox(self)
        self.tilt_control.addItems(self.controllers)
        if tilt_control_index is not None:
            self.tilt_control.setCurrentIndex(tilt_control_index)
        map_layout.addWidget(self.tilt_control, 7, 1)
        # axis entry
        self.tilt_axis = QtGui.QComboBox(self)
        self.tilt_axis.addItems(self.axes)
        if tilt_axis_index is not None:
            self.tilt_axis.setCurrentIndex(tilt_axis_index)
        map_layout.addWidget(self.tilt_axis, 7, 2)
        # expo entry
        self.tilt_expo = QtGui.QLineEdit(self)
        if tilt_expo is not None:
            self.tilt_expo.setText(str(tilt_expo))
        map_layout.addWidget(self.tilt_expo, 7, 3)
        # invert controls check box
        self.tilt_invert = QtGui.QCheckBox(self)
        if tilt_invert is not None:
            self.tilt_invert.setChecked(tilt_invert)
        map_layout.addWidget(self.tilt_invert, 7, 4)
        # use axis/buttons checkbox
        self.tilt_use_axis = QtGui.QCheckBox(self)
        if tilt_use_axis is not None:
            self.tilt_use_axis.setChecked(tilt_use_axis)
        self.tilt_use_axis.setToolTip("Check to use axis instead of buttons")
        map_layout.addWidget(self.tilt_use_axis, 7, 5)

        # positive and negative button boxes
        tilt_buttons_layout = QtGui.QGridLayout()

        # positive button entry
        tilt_buttons_layout.addWidget(QtGui.QLabel('Positive', self), 0, 0)
        self.tilt_button_p = QtGui.QLineEdit(self)
        if tilt_button_p is not None:
            self.tilt_button_p.setText(str(tilt_button_p))
        tilt_buttons_layout.addWidget(self.tilt_button_p, 0, 1)

        # negative button entry
        tilt_buttons_layout.addWidget(QtGui.QLabel('Negative', self), 1, 0)
        self.tilt_button_n = QtGui.QLineEdit(self)
        if tilt_button_n is not None:
            self.tilt_button_n.setText(str(tilt_button_n))
        tilt_buttons_layout.addWidget(self.tilt_button_n, 1, 1)

        # add positive and negative button entries to main grid layout
        map_layout.addLayout(tilt_buttons_layout, 7, 6)

        # button speed entry
        self.tilt_button_speed = QtGui.QLineEdit(self)
        if tilt_button_speed is not None:
            self.tilt_button_speed.setText(str(tilt_button_speed))
        map_layout.addWidget(self.tilt_button_speed, 7, 7)







        # Ok/cancel buttons
        buttons = QtGui.QHBoxLayout()
        buttons.addStretch(1)
        layout.addLayout(buttons)
        no_button = QtGui.QPushButton("Cancel", self)
        no_button.clicked.connect(self.reject)
        buttons.addWidget(no_button)
        ok_button = QtGui.QPushButton("OK", self)
        ok_button.setDefault(True)
        ok_button.clicked.connect(self.ok_action)
        buttons.addWidget(ok_button)



    def get_joystick_list(self):
        """Get a list of connected joysticks.

        Returns:
            List of strings describing connected joysticks.
        """
        joystick.init()
        joysticks = ['None']
        for i in range(joystick.get_count()):
            stick = joystick.Joystick(i)
            joysticks.append(
                "{0}: {1}".format(i, stick.get_name())
            )

        return joysticks

    def ok_action(self):
        """Action handler for ok button."""
        # Save the primary controller index
        primary_index = self.primary_list.currentIndex() - 1
        if primary_index < 0:
            primary_index = None
        self.settings.setValue('input/primary/index', primary_index)

        # Save the secondary controller index
        secondary_index = self.secondary_list.currentIndex() - 1
        if secondary_index < 0:
            secondary_index = None
        self.settings.setValue('input/secondary/index', secondary_index)

        # Save left_drive settings
        left_control_index = self.left_control.currentIndex()
        self.settings.setValue('input/map/left_drive/control', left_control_index)
        left_axis_index = self.left_axis.currentIndex()
        self.settings.setValue('input/map/left_drive/axis', left_axis_index)
        left_expo = float(self.left_expo.text())
        self.settings.setValue('input/map/left_drive/expo', left_expo)
        left_invert = self.left_invert.isChecked()
        self.settings.setValue('input/map/left_drive/invert', left_invert)

        # Save right_drive settings
        right_control_index = self.right_control.currentIndex()
        self.settings.setValue('input/map/right_drive/control', right_control_index)
        right_axis_index = self.right_axis.currentIndex()
        self.settings.setValue('input/map/right_drive/axis', right_axis_index)
        right_expo = float(self.right_expo.text())
        self.settings.setValue('input/map/right_drive/expo', right_expo)
        right_invert = self.right_invert.isChecked()
        self.settings.setValue('input/map/right_drive/invert', right_invert)

        # Save arm_azimuth settings
        azimuth_control_index = self.azimuth_control.currentIndex()
        self.settings.setValue('input/map/arm_azimuth/control', azimuth_control_index)
        azimuth_axis_index = self.azimuth_axis.currentIndex()
        self.settings.setValue('input/map/arm_azimuth/axis', azimuth_axis_index)
        azimuth_expo = float(self.azimuth_expo.text())
        self.settings.setValue('input/map/arm_azimuth/expo', azimuth_expo)
        azimuth_invert = self.azimuth_invert.isChecked()
        self.settings.setValue('input/map/arm_azimuth/invert', azimuth_invert)

        # Save arm_shoulder settings
        shoulder_control_index = self.shoulder_control.currentIndex()
        self.settings.setValue('input/map/arm_shoulder/control', shoulder_control_index)
        shoulder_axis_index = self.shoulder_axis.currentIndex()
        self.settings.setValue('input/map/arm_shoulder/axis', shoulder_axis_index)
        shoulder_expo = float(self.shoulder_expo.text())
        self.settings.setValue('input/map/arm_shoulder/expo', shoulder_expo)
        shoulder_invert = self.shoulder_invert.isChecked()
        self.settings.setValue('input/map/arm_shoulder/invert', shoulder_invert)

        # Save arm_elbow settings
        elbow_control_index = self.elbow_control.currentIndex()
        self.settings.setValue('input/map/arm_elbow/control', elbow_control_index)
        elbow_axis_index = self.elbow_axis.currentIndex()
        self.settings.setValue('input/map/arm_elbow/axis', elbow_axis_index)
        elbow_expo = float(self.elbow_expo.text())
        self.settings.setValue('input/map/arm_elbow/expo', elbow_expo)
        elbow_invert = self.elbow_invert.isChecked()
        self.settings.setValue('input/map/arm_elbow/invert', elbow_invert)

        # Save camera_pan settings
        pan_control_index = self.pan_control.currentIndex()
        self.settings.setValue('input/map/camera_pan/control', pan_control_index)
        pan_use_axis = self.pan_use_axis.isChecked()
        self.settings.setValue('input/map/camera_pan/use_axis', pan_use_axis)
        pan_axis_index = self.pan_axis.currentIndex()
        self.settings.setValue('input/map/camera_pan/axis', pan_axis_index)
        pan_button_p = int(self.pan_button_p.text())
        self.settings.setValue('input/map/camera_pan/button_p', pan_button_p)
        pan_button_n = int(self.pan_button_n.text())
        self.settings.setValue('input/map/camera_pan/button_n', pan_button_n)
        pan_button_speed = float(self.pan_button_speed.text())
        self.settings.setValue('input/map/camera_pan/button_speed', pan_button_speed)
        pan_expo = float(self.pan_expo.text())
        self.settings.setValue('input/map/camera_pan/expo', pan_expo)
        pan_invert = self.pan_invert.isChecked()
        self.settings.setValue('input/map/camera_pan/invert', pan_invert)

        # Save camera_tilt settings
        tilt_control_index = self.tilt_control.currentIndex()
        self.settings.setValue('input/map/camera_tilt/control', tilt_control_index)
        tilt_use_axis = self.tilt_use_axis.isChecked()
        self.settings.setValue('input/map/camera_tilt/use_axis', tilt_use_axis)
        tilt_axis_index = self.tilt_axis.currentIndex()
        self.settings.setValue('input/map/camera_tilt/axis', tilt_axis_index)
        tilt_button_p = int(self.tilt_button_p.text())
        self.settings.setValue('input/map/camera_tilt/button_p', tilt_button_p)
        tilt_button_n = int(self.tilt_button_n.text())
        self.settings.setValue('input/map/camera_tilt/button_n', tilt_button_n)
        tilt_button_speed = float(self.tilt_button_speed.text())
        self.settings.setValue('input/map/camera_tilt/button_speed', tilt_button_speed)
        tilt_expo = float(self.tilt_expo.text())
        self.settings.setValue('input/map/camera_tilt/expo', tilt_expo)
        tilt_invert = self.tilt_invert.isChecked()
        self.settings.setValue('input/map/camera_tilt/invert', tilt_invert)

        # Notify the input controller
        QtGui.QApplication.instance().input_controller.configure()

        # Cleanup the dialog
        self.accept()
