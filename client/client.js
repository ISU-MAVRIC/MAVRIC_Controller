var maxSpeed = 64;
var maxTurn = 64;

var keyArray = {};
var controlStatus = {
	speed: 0,
	turn: 0
};

// Setup requestAnimationFrame
(function() {
	// Find proper method with fallbacks
	var requestAnimationFrame = window.requestAnimationFrame || window.mozRequestAnimationFrame ||
		window.webkitRequestAnimationFrame || window.msRequestAnimationFrame;
	// Set the proper method
	window.requestAnimationFrame = requestAnimationFrame;
})();

function update(timestamp) {
	if(keyArray[83]) controlStatus.speed = -maxSpeed;
	if(keyArray[87]) controlStatus.speed = maxSpeed;
	if(!keyArray[83] && !keyArray[87]) controlStatus.speed = 0;
	if(keyArray[65]) controlStatus.turn = -maxTurn;
	if(keyArray[68]) controlStatus.turn = maxTurn;
	if(!keyArray[65] && !keyArray[68]) controlStatus.turn = 0;
	if(navigator.webkitGetGamepads()[1]) {
		var controller = navigator.webkitGetGamepads()[1];
		controlStatus.speed = maxSpeed * -controller.axes[1];
		controlStatus.turn = maxTurn * controller.axes[0];
		if(Math.abs(controller.axes[0]) < 0.15) controlStatus.turn = 0;
		if(Math.abs(controller.axes[1]) < 0.15) controlStatus.speed = 0;
	}
	socket.emit('control', controlStatus);
	requestAnimationFrame(update);
}

requestAnimationFrame(update);

var socket = io.connect('http://localhost:8000');

window.onkeydown = function(e) {
	keyArray[e.keyCode] = true;
};
window.onkeyup = function(e) {
	keyArray[e.keyCode] = false;
};