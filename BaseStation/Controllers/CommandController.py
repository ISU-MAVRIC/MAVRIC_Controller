import sys

from PySide import QtCore

class CommandController(QtCore.QObject):

    def __init__(self, parent=None):
        super(CommandController, self).__init__(parent)

        self.state = "none"
        self.buffer = bytearray()

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
