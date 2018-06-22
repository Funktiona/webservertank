from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit
import socket
import time
import funktions

s = socket.socket()

# Server ip
# OG

#hosta = '192.168.0.121'

# Erik

# Andre

hosta = '192.168.1.184'

port = 10000
s.bind((hosta, port))

c = None
addr = None


#Old tank
tank_1_c = None
tank_1_addr = None

#New tank
tank_2_c = None
tank_2_addr = None

app = Flask(__name__, static_url_path='/static')
socketio = SocketIO(app)

s.listen(5)


#tank_1_c, tank_1_addr, tank_2_c, tank_2_addr = funktions.connect_tanks(s)
tank_1_c, tank_1_addr = funktions.connect_tanks(s)

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

'''
s.listen(5)
while True:
    c, addr = s.accept()
    print(c)
    c.send('test')
    break
'''

@app.route('/')
@app.route('/index')
def index():
    
    return render_template('index.html')
    #return 'Hello, World!'


#Make page for each tank
@app.route("/tank/<int:tank>", methods=['GET', 'POST'])
def tank_page(tank):
	print tank 
	if request.method == 'GET':

		if tank == 1:
			stream_addr = 'http://' + str(tank_1_addr[0]) + ':8080/stream/video.mjpeg'
			return render_template('tank.html', stream_addr = stream_addr, tank=1)

		if tank == 2:
			stream_addr = 'http://' + str(tank_2_addr[0]) + ':8080/stream/video.mjpeg'
			return render_template('tank.html', stream_addr = stream_addr, tank=2)

	else:

		if tank == 1:
			stream_addr = 'http://' + str(tank_1_addr[0]) + ':8080/stream/video.mjpeg'
			return render_template('tank.html', stream_addr = stream_addr)

		if tank == 2:
			stream_addr = 'http://' + str(tank_2_addr[0]) + ':8080/stream/video.mjpeg'
			return render_template('tank.html', stream_addr = stream_addr)


@socketio.on('direction')
def recive_derection(data):
    print(data)
    c.send(data)

@socketio.on('shoot')
def recive_shoot(aim_pos):
	print aim_pos
	funktions.shoot(tank=1, aim_pos=aim_pos)

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

if __name__ == '__main__':
    print('run app')
    app.run(host='0.0.0.0')

    app.run()

