import sys

from PySide import QtCore

from DriveController import *

class CommandController(QtCore.QObject):

    def __init__(self, parent=None):
        super(CommandController, self).__init__(parent)

        self.drive_control = DriveController(self)

        self.state = "none"
        self.buffer = bytearray()

    def drive_command(self, left, right):
        drive, angle = self.drive_control.compute(left, right)

        print "<cm {0:03d} {1:03d} {2:03d} {3:03d} {4:03d} {5:03d} >".format(
            drive[0], drive[1], drive[2], drive[3], drive[4], drive[5]
        )
        print "<cs {0:03d} {1:03d} {2:03d} {3:03d} {4:03d} {5:03d} >".format(
            angle[0], angle[1], angle[2], angle[3], angle[4], angle[5]
        )

        drive_cmd = "<cm{:s}{:s}{:s}{:s}{:s}{:s}>\n".format(
            chr(drive[0]), chr(drive[1]), chr(drive[2]),
            chr(drive[3]), chr(drive[4]), chr(drive[5])
        )
        self.parent().port_controller.write(drive_cmd)

    def parse(self, byte):
        if self.state == "none":
            if byte == '<':
                self.state = "started"
                self.buffer = bytearray()
                print "" + self.state
        elif self.state == "started":
            if byte == 's':
                self.state = "status"
                print " " + self.state
            else:
                print "\tInvalid packet type: {:s}".format(byte)
                self.state = "none"
        elif self.state == "status":
            if byte == 'm':
                self.state = "status.motor"
                print "  " + self.state
            elif byte == 's':
                self.state = "status.steering"
                print "  " + self.state
            elif byte == 'a':
                self.state = "status.arm"
                print "  " + self.state
            elif byte == 'c':
                self.state = "status.camera"
                print "  " + self.state
            else:
                print self.state
                print "\t\tInvalid status packet type: {:s}".format(byte)
                self.state = "none"
        elif self.state == "status.motor":
            if len(self.buffer) > 5:
                if byte == '>':
                    for i in range(6):
                        print "Motor {:d}: {:d}".format(i+1, self.buffer[i])

                    print "end"
                    self.state = "none"
                else:
                    print "Unexpected data!"
                    self.state = "none"
                return
            else:
                self.buffer.append(byte)
        elif self.state == "status.steering":
            if len(self.buffer) > 5:
                if byte == '>':
                    for i in range(6):
                        print "Steering {:d}: {:d}".format(i+1, self.buffer[i])

                    print "end"
                    self.state = "none"
                else:
                    print "Unexpected data!"
                    self.state = "none"
                return
            else:
                self.buffer.append(byte)
        elif self.state == "status.arm":
            if len(self.buffer) > 2:
                if byte == '>':
                    print "Arm Rotation: {:d}".format(self.buffer[0])
                    print "Arm Shoulder: {:d}".format(self.buffer[1])
                    print "Arm Elbow: {:d}".format(self.buffer[2])

                    print "end"
                    self.state = "none"
                else:
                    print "Unexpected data!"
                    self.state = "none"
                return
            else:
                self.buffer.append(byte)
        elif self.state == "status.camera":
            if len(self.buffer) > 2:
                if byte == '>':
                    print "Cam Pan: {:d}".format(self.buffer[0])
                    print "Cam Tilt: {:d}".format(self.buffer[1])
                    print "Cam Zoom: {:d}".format(self.buffer[2])

                    print "end"
                    self.state = "none"
                else:
                    print "Unexpected data!"
                    self.state = "none"
                return
            else:
                self.buffer.append(byte)
        else:
            print "Unknown parser state!"
            self.state = "none"

        if byte == '>':
            print "Unexpected packet end! - {:s}".format(self.state)
            self.state = "none"
