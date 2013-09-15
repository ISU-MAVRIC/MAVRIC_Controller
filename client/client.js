var maxSpeed = 4;
var maxTurn = 4;

var keyArray = {};
var controlStatus = {
	speed: 0,
	turn: 0
};


// Setup the map
var map = L.map('map').setView([42.03,-93.62], 13);
L.tileLayer('http://{s}.tile.stamen.com/terrain/{z}/{x}/{y}.jpg', {
	attribution: 'Tiles courtesy of <a href="http://www.stamen.com">Stamen</a>'
}).addTo(map);
handleResize();
$(window).resize(handleResize);

function handleResize() {
	var mapContainer = $('#map');
	mapContainer.height(0.75 * mapContainer.width());
}

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
	var controller = getGamepads();
	if(controller) {
		controlStatus.speed = maxSpeed * controller.axes[1];
		controlStatus.turn = maxTurn * -controller.axes[0];
		if(Math.abs(controller.axes[0]) < 0.15) controlStatus.turn = 0;
		if(Math.abs(controller.axes[1]) < 0.15) controlStatus.speed = 0;
	}
	socket.emit('control', controlStatus);
	//requestAnimationFrame(update);
}

function getGamepads() {
	var gamepads = navigator.webkitGetGamepads();
	for(var i = 0; i < gamepads.length; i++) {
		if(typeof gamepads[i] !== 'undefined') return gamepads[i];
	}
	return;
}

//requestAnimationFrame(update);
setInterval(update, 100);

var socket = io.connect('http://localhost:8000');

window.onkeydown = function(e) {
	keyArray[e.keyCode] = true;
};
window.onkeyup = function(e) {
	keyArray[e.keyCode] = false;
};