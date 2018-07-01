from flask import Flask, render_template, request
from flask_socketio import SocketIO, send
import socket
import thread
import json
from funktions import tank_connections

s = socket.socket()
server_ip = '192.168.1.64' # ip of the computer
port = 10000

s.bind((server_ip, port))
app = Flask(__name__, static_url_path='/static')
socketio = SocketIO(app)
clients = tank_connections()
thread.start_new_thread(clients.on_new_client, (s,))

@app.route('/')
def index():
    clients.give_id()
    return render_template('index.html', active_clients = clients.tanks)


# Make page for each tank
@app.route("/tank/<int:tank>")
def tank_page(tank):
    try:
        stream_addr = 'http://' + str(clients.tanks[tank]['adress']) + ':8080/stream/video.mjpeg'
        return render_template('tank.html', stream_addr=stream_addr, tank=tank)
    except:
        print('no tank on this adress', tank)

@socketio.on('input')
def receive_input(direction, aim_pos, url):
    id = int(url[-1:]) # the duplicate bug is back now.
    dir_loaded = json.loads(direction)
    dir_loaded['32'] = clients.fire(dir_loaded, aim_pos, id)
    inputs = json.dumps(dir_loaded)
    inputs += '\n' # Helps the tank split the multiple inputs if they get sent at the same time(delay)
    clients.tanks[id]['connection'].sendall(inputs.encode())


if __name__ == '__main__':
    print('run app')
    app.run(host='0.0.0.0')

    app.run()
