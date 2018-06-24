from flask import Flask, render_template, request
from flask_socketio import SocketIO, send
from time import time as now
import socket
import funktions

s = socket.socket()
server_ip = '192.168.0.103' # ip of the computer
port = 10000

s.bind((server_ip, port))
app = Flask(__name__, static_url_path='/static')
socketio = SocketIO(app)

# s.listen(5)

# test.tanks = funktions.connect_tanks(s)
class id_save():
    def __init__(self):
        self.id = None

curr_tank = id_save()
tanks = funktions.connect_tanks(s)

@app.route('/')
def index():
    return render_template('index.html')


# Make page for each tank
@app.route("/tank/<int:tank>")
def tank_page(tank):

    if tanks[tank]:
        curr_tank.id = tank
        print(tanks[curr_tank.id])
        stream_addr = 'http://' + str(tanks[curr_tank.id]['adress']) + ':8080/stream/video.mjpeg'
        return render_template('tank.html', stream_addr=stream_addr, tank=tank)
    else:
        return render_template('index.html')




@socketio.on('input')
def recive_derection(data):
    print(data)
    print(tanks[curr_tank.id]['connection'])
    tanks[curr_tank.id]['connection'].send(data.encode())


@socketio.on('shoot')
def recive_shoot(aim_pos):
    id = str(request.base_url)
    if (int(now()) - tanks[id]['timer']) > 1:
        tanks[id]['timer'] = funktions.shoot(tank=tanks[id], aim_pos=aim_pos)


if __name__ == '__main__':
    print('run app')
    app.run(host='0.0.0.0')

    app.run()
