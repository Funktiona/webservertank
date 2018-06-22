var socket = io.connect('http://' + document.domain + ':' + location.port);
            socket.on('connect', function() {
            socket.emit('my event', {data: 'I\'m connected!'});
            });

document.onkeydown = checkKey;

function checkKey(e) {

        e = e || window.event;

	if (e.keyCode == '38') {
		socket.emit('direction', 'up');
        }
        else if (e.keyCode == '40') {
		socket.emit('direction', 'down');
        }
        else if (e.keyCode == '37') {
		socket.emit('direction', 'left');
	}
        else if (e.keyCode == '39') {
                socket.emit('direction', 'right');
        }
	else if (e.keyCode == '65'){
		socket.emit('direction', 'tower_left');
	}
	else if (e.keyCode ==  '68'){
		socket.emit('direction', 'tower_right');
	}
}


