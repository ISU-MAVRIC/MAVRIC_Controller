import signal
import sys

from PySide import QtCore
from serial import Serial

class Simulator(QtCore.QObject):

    def __init__(self, port, baud, parent=None):
        super(Simulator, self).__init__(parent)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update)

        print "Connecting to port {:s} at {:d} baud".format(port, baud)
        self.port = Serial(port, baud)

        self.timer.start(50)

    def update(self):
        while self.port.inWaiting() > 0:
            byte = self.port.read()
            sys.stdout.write(byte)

    def close(self, signal, frame):
        print "Closing..."
        QtCore.QCoreApplication.instance().quit()

def main():
    app = QtCore.QCoreApplication(sys.argv)

    args = app.arguments()

    sim = Simulator(str(args[-2]), int(args[-1]))

    signal.signal(signal.SIGINT, sim.close)

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
