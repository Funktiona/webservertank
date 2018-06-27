var socket = io.connect('http://' + document.domain + ':' + location.port);
            socket.on('connect', function() {
            socket.emit('my event', {data: 'I\'m connected!'});
            });



var keys = {32:false, 37: false, 39: false, 65:false, 68: false, 83: false, 87: false};
var prv_keys = {};
var valid_keys = {32:false, 37: false, 39: false, 65: false, 68: false, 83: false, 87: false};
document.addEventListener('keydown',activated_keys);
document.addEventListener('keyup',activated_keys);

function copy_obj(original){
	/*Makes a new object from the old one*/
    let copy = Object.assign({}, original);
    return copy;
}
function activated_keys(e)
{
  /*Saves the keyboard inputs in a object.
    Stores the value in keys and makes a
    copy in prv_keys to check for a change.
    If a change has occurred i.e a key has been
    released or pressed.
    The change will be sent to the server.
    */

     for(var key in valid_keys)
     {
        if (e.keyCode == key)
        {
           if (e.type == 'keyup')
           {
               keys[e.keyCode] = false;
           }
           if (e.type == 'keydown')
           {
               keys[e.keyCode] = true;
           }
           /* Stringify the objects making it easier to compare them.*/
           let key_json = JSON.stringify(keys);
           let copy_json = JSON.stringify(prv_keys);

           if (key_json !== copy_json)
           {
               //Only sends keys when something have changed.
               socket.emit('input', key_json + '\n', aim_pos,document.URL);
               prv_keys = copy_obj(keys);
           }
        }
     }
}


document.onkeydown = checkKey;

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
		socket.emit('shoot', aim_pos, document.URL);
	}
	else if (e.keyCode == '37'){
		socket.emit('direction', 'tower_left');
	}
	else if (e.keyCode ==  '39'){
		socket.emit('direction', 'tower_right');
	}
}


aim_pos = [320,240];
aim_angle = 90;

function draw_hair(){
	var c=document.getElementById("myCanvas");
	var ctx=c.getContext("2d");

	ctx.clearRect(0, 0, 640, 480);
	ctx.beginPath();

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

	//center
	ctx.rect(aim_pos[0],aim_pos[1],1,1);
	ctx.stroke();

}

window.setInterval("refreshCanvas()", 30);
function refreshCanvas(){
	draw_hair();
//	console.log('render');
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

