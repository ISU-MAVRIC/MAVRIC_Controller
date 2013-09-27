// Axes
// 0: Left Stick X
// 1: Left Stick Y
// 2: Right Stick X
// 3: Right Stick Y

// Buttons
// 0: A
// 1: B
// 2: X
// 3: Y
// 4: Left Bumper
// 5: Right Bumper
// 6: Left Trigger
// 7: Right Trigger
// 8: Back Button
// 9: Start Button
// 10: Left Stick
// 11: Right Stick
// 12: Up
// 13: Down
// 14: Left
// 15: Right

// Control Mapping
var turnAxis = 0;
var speedAxis = 1;
var panAxis = 2;
var tiltAxis = 3;
var speedBtn = 10;
var zoomBtn = 11;

// Control setup
var speedExpo = 0.5;
var turnExpo = 0.5;
var camExpo = 1.0;
var lowSpeed = 32;
var highSpeed = 64;
var turnSpeed = 16;
var camSpeed = 4;

// Control input tracking
var keyArray = {};
var btnArray = {};

// State Variables
var lastUpdate = Date.now();
var highSpeedMode = false;

// Setup the map
var map = L.map('map').setView([42.03,-93.62], 15);
L.tileLayer('http://{s}.tile.stamen.com/terrain/{z}/{x}/{y}.jpg', {
	attribution: 'Tiles courtesy of <a href="http://www.stamen.com">Stamen</a>'
}).addTo(map);
handleResize();
$(window).resize(handleResize);

jwplayer("player").setup({
	'file': 'http://127.0.0.1:8080/stream.flv',
	'debug': {
		'levels': 'all'
	}
});

var roverSvg = d3.select('#rover').append('svg')
			.style('background-color', 'gray')
			.style('height', '300px');

function update(timestamp) {
	var time = Date.now();
	if(time - lastUpdate < 50) {
		requestAnimationFrame(update);
		return;
	}
	lastUpdate = time;
	var controlStatus = {};
	var controller = getGamepads();
	if(controller) {
		// Get axes
		var speed = -sign(controller.axes[speedAxis]) * Math.pow(controller.axes[speedAxis], 1 / speedExpo);
		var turn = sign(controller.axes[turnAxis]) * Math.pow(controller.axes[turnAxis], 1 / turnExpo);
		var pan = sign(controller.axes[panAxis]) * Math.pow(controller.axes[panAxis], 1 / camExpo);
		var tilt = -sign(controller.axes[tiltAxis]) * Math.pow(controller.axes[tiltAxis], 1 / camExpo);

		if(buttonDown(controller, speedBtn)) highSpeedMode = !highSpeedMode;
		var curSpeed = highSpeedMode ? highSpeed : lowSpeed;

		controlStatus.speed = [
			Math.round(speed*curSpeed + turn*turnSpeed),
			Math.round(speed*curSpeed + turn*turnSpeed),
			Math.round(speed*curSpeed + turn*turnSpeed),
			Math.round(speed*curSpeed - turn*turnSpeed),
			Math.round(speed*curSpeed - turn*turnSpeed),
			Math.round(speed*curSpeed - turn*turnSpeed)
		];
		controlStatus.steer = [0, 0, 0, 0, 0, 0];
		controlStatus.camPos = [
			Math.round(pan*camSpeed),
			Math.round(tilt*camSpeed)
		];

		btnArray = controller.buttons;
	}
	socket.emit('control', controlStatus);
	requestAnimationFrame(update);
}

requestAnimationFrame(update);

var socket = io.connect('http://localhost:8000');

/* Helper Functions */

// Setup requestAnimationFrame
(function() {
	// Find proper method with fallbacks
	var requestAnimationFrame = window.requestAnimationFrame || window.mozRequestAnimationFrame ||
		window.webkitRequestAnimationFrame || window.msRequestAnimationFrame;
	// Set the proper method
	window.requestAnimationFrame = requestAnimationFrame;
})();

// Get the active gamepad
function getGamepads() {
	var gamepads = navigator.webkitGetGamepads();
	for(var i = 0; i < gamepads.length; i++) {
		if(typeof gamepads[i] !== 'undefined') return gamepads[i];
	}
	return;
}

function buttonDown(controller, btn) {
	if(controller.buttons[btn] < 0.5) return false;
	if(btnArray[btn] < 0.5) return true;
}

function buttonPressed(controller, btn) {
	if(controller.buttons[btn] > 0.5) return true;
	return false;
}

// Return sign of number
function sign(x) {
	return x ? x < 0 ? -1 : 1 : 0;
}

// Resize the elements of the page
function handleResize() {
	var mapContainer = $('#map');
	mapContainer.height(0.75 * mapContainer.width());
}

window.onkeydown = function(e) {
	keyArray[e.keyCode] = true;
};

window.onkeyup = function(e) {
	keyArray[e.keyCode] = false;
};