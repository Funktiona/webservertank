from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
#loiskkl
import socket
import time

s = socket.socket()
host = '192.168.1.239'
# host = '192.168.0.123' #ip of raspberry pi
port = 10000
s.bind((host, port))
# hello
c = None
addr = None

s.listen(5)
while True:
    c, addr = s.accept()
    print('after')




app = Flask(__name__, static_url_path='/static')
socketio = SocketIO(app)
