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

function checkKey(e) {

	e = e || window.event;

	if (e.keyCode == '38') {
		if(aim_pos[1] > 150) aim_pos[1] -= 10;
		socket.emit('direction', 'up');
		socket.emit('aim', aim_pos[1]);

	}
	else if (e.keyCode == '40') {
		//socket.emit('direction', 'down');
		if(aim_pos[1] < 380) aim_pos[1] += 10;
		socket.emit('aim', aim_pos[1]);
	}
	else if(e.keyCode == '32'){
		console.log('shoot');
		console.log(aim_pos);
		socket.emit('shoot', aim_pos);
	}
	else if (e.keyCode == '37'){
		socket.emit('direction', 'tower_left');
	}
	else if (e.keyCode ==  '39'){
		socket.emit('direction', 'tower_right');
	}
	//Drive tank
	else if (e.keyCode == '87') {
		socket.emit('direction', 'up');
        }
        else if (e.keyCode == '83') {
		socket.emit('direction', 'down');
        }
        else if (e.keyCode == '65') {
		socket.emit('direction', 'left');
	}
        else if (e.keyCode == '68') {
                socket.emit('direction', 'right');
        }
	
}


aim_pos = [320,240];
aim_angle = 90;

function draw_hair(){
	var c=document.getElementById("myCanvas");
	var ctx=c.getContext("2d");

	ctx.clearRect(0, 0, 640, 480);
	ctx.beginPath();

	//var img = new Image();
	//img.src = "http://192.168.1.247:8080/stream/video.mjpeg"
	//img.src = "http://192.168.1.247:8080/stream/snapshot.jpeg?delay_s=0"
	//img.onload = function() {
	//ctx.drawImage(img, 0, 0);
	//};
	//var theDate = new Date();
	ctx.fillStyle = 'green';
	ctx.rect(aim_pos[0]-40, aim_pos[1]-40, 80, 80);
	//Left
	//ctx.fillRect(aim_pos[0]-50, aim_pos[1]-7, 40, 14);
	//Right
	//ctx.fillRect(aim_pos[0]+10, aim_pos[1]-7, 40, 14);
	//Top 
	//ctx.fillRect(aim_pos[0]-7, aim_pos[1]-50, 14, 40);
	//Bottom
	//ctx.fillRect(aim_pos[0]-7, aim_pos[1]+10, 14, 40);
	
	//Aim angle
	ctx.rect(50, 40, 540, 50);
	
	ctx.fillRect(30 + (aim_angle/180)*540, 40, 40, 50);

	
	//img.src = "http://192.168.1.247:8080/stream/video.mjpeg"
	//img.src = "http://192.168.1.247:8080/stream/snapshot.jpeg?delay_s=0"

	//center
	ctx.rect(aim_pos[0],aim_pos[1],1,1);
	ctx.stroke(); 

}

window.setInterval("refreshCanvas()", 30);
function refreshCanvas(){
	draw_hair();
	console.log('render');
 	//ctx.drawImage(img, 0, 0);
};

function mainLoop() {
    //update();
    draw_hair();
    console.log('render');
	
    requestAnimationFrame(mainLoop);
}
 
refreshCanvas()
// Start things off
//requestAnimationFrame(mainLoop);

