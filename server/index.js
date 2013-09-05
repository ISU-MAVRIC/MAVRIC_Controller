var SerialPort = require('serialport').SerialPort;

var serialPort = new SerialPort('/dev/ttyUSB0', {
	baudrate: 9600,
	databits: 8,
	stopbits: 1,
	parity: 'none'
});

serialPort.on('data', function(data) {
});