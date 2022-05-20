import base64
import io

import numpy as np
import ps as ps
from PIL import Image
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from face_detector import *

app = Flask(__name__)
app.config['MASTER_KEY'] = 'admin'
socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template("index.html")


'''
@socketio.on("my event")
def test_message(message):
    emit("my response", {"data": message["data"]})

@socketio.on("my broadcast event")
def test_message(message):
    emit("my respones", {"data": message["data"]}, broadcast=True)
'''


@socketio.on("connect")
def connect():
    print("User connected")


@socketio.on("image")
def get_face_coordinates(base64_data):
    im = Image.open(io.BytesIO(base64.b64decode(base64_data)))
    im.save('image.png', 'PNG')

    '''
    (x, y, w, h) = create_coordinates(img)
    emit("face_coordinates", {"x": x, "y": y, "w": w, "h": h})
    '''

if __name__ == "__main__":
    socketio.run(app)
