var express = require('express');
var app = express();
var server = require('http').createServer(app);
var io = require('socket.io').listen(server);
var SerialPort = require('serialport').SerialPort;

server.listen(8000);

app.use(express.static(__dirname + '/client'));

app.get('/stream.mp4', function(req, res) {
	res.set('content-type', 'video/mp4');
	res.send(200);
});

io.sockets.on('connection', function(socket) {
	socket.on('control', function(data) {
		console.log(data);
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