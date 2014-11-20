from pygame import joystick
from PySide import QtCore, QtGui

class InputDialog(QtGui.QDialog):

    controllers = ['Primary', 'Secondary']
    axes = ['0', '1', '2', '3', '4', '5', '6', '7']

    def __init__(self, parent):
        super(InputDialog, self).__init__(parent)
        self.setWindowTitle('Configure input devices')

        self.settings = QtCore.QSettings()

        self.initUI()

    def initUI(self):
        joysticks = self.get_joystick_list()

        layout = QtGui.QVBoxLayout()
        self.setLayout(layout)

        form = QtGui.QFormLayout()
        layout.addLayout(form)

        self.primary_list = QtGui.QComboBox(self)
        self.primary_list.addItems(joysticks)
        self.primary_list.setCurrentIndex(0)
        primary_index = self.settings.value('input/primary/index')
        if primary_index is not None:
            if primary_index < (len(joysticks) - 1):
                self.primary_list.setCurrentIndex(
                    primary_index + 1
                )
        form.addRow("Primary Input:", self.primary_list)

        self.secondary_list = QtGui.QComboBox(self)
        self.secondary_list.addItems(joysticks)
        self.secondary_list.setCurrentIndex(0)
        secondary_index = self.settings.value('input/secondary/index')
        if secondary_index is not None:
            if secondary_index < (len(joysticks) - 1):
                self.secondary_list.setCurrentIndex(
                    secondary_index + 1
                )
        form.addRow("Secondary Input:", self.secondary_list)

        divider = QtGui.QFrame(self)
        divider.setFrameShape(QtGui.QFrame.Shape.HLine)
        divider.setFrameShadow(QtGui.QFrame.Shadow.Sunken)
        layout.addWidget(divider)

        map_layout = QtGui.QGridLayout()
        layout.addLayout(map_layout)
        map_layout.addWidget(QtGui.QLabel('Controller:', self), 0, 1)
        map_layout.addWidget(QtGui.QLabel('Axis:', self), 0, 2)
        map_layout.addWidget(QtGui.QLabel('Expo:', self), 0, 3)
        map_layout.addWidget(QtGui.QLabel('Reverse:', self), 0, 4)

        left_control_index = self.settings.value('input/map/left_drive/control')
        left_axis_index = self.settings.value('input/map/left_drive/axis')
        left_expo = self.settings.value('input/map/left_drive/expo')
        left_reverse = self.settings.value('input/map/left_drive/reverse') == 'true'

        right_control_index = self.settings.value('input/map/right_drive/control')
        right_axis_index = self.settings.value('input/map/right_drive/axis')
        right_expo = self.settings.value('input/map/right_drive/expo')
        right_reverse = self.settings.value('input/map/right_drive/reverse') == 'true'

        azimuth_control_index = self.settings.value('input/map/arm_azimuth/control')
        azimuth_axis_index = self.settings.value('input/map/arm_azimuth/axis')
        azimuth_expo = self.settings.value('input/map/arm_azimuth/expo')
        azimuth_reverse = self.settings.value('input/map/arm_azimuth/reverse') == 'true'

        shoulder_control_index = self.settings.value('input/map/arm_shoulder/control')
        shoulder_axis_index = self.settings.value('input/map/arm_shoulder/axis')
        shoulder_expo = self.settings.value('input/map/arm_shoulder/expo')
        shoulder_reverse = self.settings.value('input/map/arm_shoulder/reverse') == 'true'

        elbow_control_index = self.settings.value('input/map/arm_elbow/control')
        elbow_axis_index = self.settings.value('input/map/arm_elbow/axis')
        elbow_expo = self.settings.value('input/map/arm_elbow/expo')
        elbow_reverse = self.settings.value('input/map/arm_elbow/reverse') == 'true'

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
        self.left_reverse = QtGui.QCheckBox(self)
        if left_reverse is not None:
            self.left_reverse.setChecked(left_reverse)
        map_layout.addWidget(self.left_reverse, 1, 4)

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
        self.right_reverse = QtGui.QCheckBox(self)
        if right_reverse is not None:
            self.right_reverse.setChecked(right_reverse)
        map_layout.addWidget(self.right_reverse, 2, 4)

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
        self.azimuth_reverse = QtGui.QCheckBox(self)
        if azimuth_reverse is not None:
            self.azimuth_reverse.setChecked(azimuth_reverse)
        map_layout.addWidget(self.azimuth_reverse, 3, 4)

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
        self.shoulder_reverse = QtGui.QCheckBox(self)
        if shoulder_reverse is not None:
            self.shoulder_reverse.setChecked(shoulder_reverse)
        map_layout.addWidget(self.shoulder_reverse, 4, 4)

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
        self.elbow_reverse = QtGui.QCheckBox(self)
        if elbow_reverse is not None:
            self.elbow_reverse.setChecked(elbow_reverse)
        map_layout.addWidget(self.elbow_reverse, 5, 4)

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
        joystick.init()
        joysticks = ['None']
        for i in range(joystick.get_count()):
            stick = joystick.Joystick(i)
            joysticks.append(
                "{0}: {1}".format(i, stick.get_name())
            )

        return joysticks

    def ok_action(self):
        primary_index = self.primary_list.currentIndex() - 1
        if primary_index < 0:
            primary_index = None
        self.settings.setValue('input/primary/index', primary_index)

        secondary_index = self.secondary_list.currentIndex() - 1
        if secondary_index < 0:
            secondary_index = None
        self.settings.setValue('input/secondary/index', secondary_index)

        left_control_index = self.left_control.currentIndex()
        self.settings.setValue('input/map/left_drive/control', left_control_index)
        left_axis_index = self.left_axis.currentIndex()
        self.settings.setValue('input/map/left_drive/axis', left_axis_index)
        left_expo = float(self.left_expo.text())
        self.settings.setValue('input/map/left_drive/expo', left_expo)
        left_reverse = self.left_reverse.isChecked()
        self.settings.setValue('input/map/left_drive/reverse', left_reverse)

        right_control_index = self.right_control.currentIndex()
        self.settings.setValue('input/map/right_drive/control', right_control_index)
        right_axis_index = self.right_axis.currentIndex()
        self.settings.setValue('input/map/right_drive/axis', right_axis_index)
        right_expo = float(self.right_expo.text())
        self.settings.setValue('input/map/right_drive/expo', right_expo)
        right_reverse = self.right_reverse.isChecked()
        self.settings.setValue('input/map/right_drive/reverse', right_reverse)

        azimuth_control_index = self.azimuth_control.currentIndex()
        self.settings.setValue('input/map/arm_azimuth/control', azimuth_control_index)
        azimuth_axis_index = self.azimuth_axis.currentIndex()
        self.settings.setValue('input/map/arm_azimuth/axis', azimuth_axis_index)
        azimuth_expo = float(self.azimuth_expo.text())
        self.settings.setValue('input/map/arm_azimuth/expo', azimuth_expo)
        azimuth_reverse = self.azimuth_reverse.isChecked()
        self.settings.setValue('input/map/arm_azimuth/reverse', azimuth_reverse)

        shoulder_control_index = self.shoulder_control.currentIndex()
        self.settings.setValue('input/map/arm_shoulder/control', shoulder_control_index)
        shoulder_axis_index = self.shoulder_axis.currentIndex()
        self.settings.setValue('input/map/arm_shoulder/axis', shoulder_axis_index)
        shoulder_expo = float(self.shoulder_expo.text())
        self.settings.setValue('input/map/arm_shoulder/expo', shoulder_expo)
        shoulder_reverse = self.shoulder_reverse.isChecked()
        self.settings.setValue('input/map/arm_shoulder/reverse', shoulder_reverse)

        elbow_control_index = self.elbow_control.currentIndex()
        self.settings.setValue('input/map/arm_elbow/control', elbow_control_index)
        elbow_axis_index = self.elbow_axis.currentIndex()
        self.settings.setValue('input/map/arm_elbow/axis', elbow_axis_index)
        elbow_expo = float(self.elbow_expo.text())
        self.settings.setValue('input/map/arm_elbow/expo', elbow_expo)
        elbow_reverse = self.elbow_reverse.isChecked()
        self.settings.setValue('input/map/arm_elbow/reverse', elbow_reverse)

        QtGui.QApplication.instance().input_controller.configure()

        self.accept()
