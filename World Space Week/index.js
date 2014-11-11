var express = require('express');
var app = express();
var server = require('http').createServer(app);
var io = require('socket.io').listen(server);
var SerialPort = require('serialport').SerialPort;

server.listen(8000);

app.use(express.static(__dirname + '/client'));

io.sockets.on('connection', function(socket) {
	socket.on('control', function(data) {
		//console.log(data.speed);
		if(data.speed) {
			var buf = Uint8Array(10);
			buf[0] = 0x3c;
			buf[1] = 0x43;
			buf[2] = 0x4d;
			buf[3] = data.speed[0] + 127;
			buf[4] = data.speed[1] + 127;
			buf[5] = data.speed[2] + 127;
			buf[6] = data.speed[3] + 127;
			buf[7] = data.speed[4] + 127;
			buf[8] = data.speed[5] + 127;
			buf[9] = 0x3e;
			//console.log(buf);
			serialPort.write(buf);
		}
	});
});

var serialPort = new SerialPort('COM31', {
	baudrate: 57600,
	databits: 8,
	stopbits: 1,
	parity: 'none'
});

serialPort.on('data', function(data) {
	console.log(data);
});