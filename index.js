var express = require('express');
var app = express();
var server = require('http').createServer(app);
var io = require('socket.io').listen(server);
var SerialPort = require('serialport').SerialPort;

server.listen(8000);

app.use(express.static(__dirname + '/client'));

io.sockets.on('connection', function(socket) {
	socket.on('control', function(data) {
		//console.log(data);
		var buf = new Uint8Array(4);
		var speed = Math.round(data.speed) + 127;
		var turn = Math.round(data.turn) + 127;
		buf[0] = 'T'.charCodeAt(0);
		buf[1] = speed;
		buf[2] = 'P'.charCodeAt(0);
		buf[3] = turn;
		console.log(buf);
		serialPort.write(buf);
	});
});

var serialPort = new SerialPort('COM27', {
	baudrate: 9600,
	databits: 8,
	stopbits: 1,
	parity: 'none'
});

serialPort.on('data', function(data) {
});