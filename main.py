from flask import Flask, render_template, request
from flask_socketio import SocketIO, send,
from time import time as now
import socket
import funktions

s = socket.socket()
server_ip = '192.168.1.184'
port = 10000

s.bind((server_ip, port))
app = Flask(__name__, static_url_path='/static')
socketio = SocketIO(app)

s.listen(5)

tanks = funktions.connect_tanks(s)

@app.route('/')
def index():
    return render_template('index.html')


# Make page for each tank
@app.route("/tank/<int:tank>", methods=['GET', 'POST'])
def tank_page(tank):

    print(request.method)
    if request.method == 'GET':
        stream_addr = 'http://' + str(tanks[tank]['adress']) + ':8080/stream/video.mjpeg'

        return render_template('tank.html', stream_addr=stream_addr, tank=tank)

    else:
        stream_addr = 'http://' + str(tanks[tank]['adress']) + ':8080/stream/video.mjpeg'
        return render_template('tank.html', stream_addr=stream_addr, tank=tank)


@socketio.on('direction')
def recive_derection(data):
    print(data)
    print(type(request.base_rule))
    id = str(request.base_rule[:1])
    tanks[id]['connection'].send(data)


@socketio.on('shoot')
def recive_shoot(aim_pos):
    id = str(request.base_rule[:1])
    if (int(now()) - tanks[id]['timer']) > 1:
        tanks[id]['timer'] = funktions.shoot(tank=tanks[id], aim_pos=aim_pos)


if __name__ == '__main__':
    print('run app')
    app.run(host='0.0.0.0')

    app.run()
