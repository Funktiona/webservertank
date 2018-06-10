from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
#OG
import socket
import time

s = socket.socket()
<<<<<<< HEAD
#hosta = '192.168.0.121'
#host = '0.0.0.0'
hosta = '192.168.1.137'
=======
host = '192.168.0.121'
#host = '0.0.0.0'
>>>>>>> 1
# host = '192.168.0.123' #ip of raspberry pi Erik
port = 10000
s.bind((hosta, port))
# hello
c = None
addr = None

app = Flask(__name__, static_url_path='/static')
socketio = SocketIO(app)


s.listen(5)
while True:
    c, addr = s.accept()
    print(c)
    c.send('test')
    break

@app.route('/')
@app.route('/index')
def index():
    
    return render_template('index.html')
    #return 'Hello, World!'

@socketio.on('direction')
def recive_derection(data):
    print(data)
    c.send(data)

if __name__ == '__main__':
    print('run app')
<<<<<<< HEAD
    app.run(host='0.0.0.0')
=======
    app.run()
>>>>>>> 1

