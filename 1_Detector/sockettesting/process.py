from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['MASTER_KEY'] = '12345'
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
def test_connect():
    emit("my response", {"data": "Connected"})


@socketio.on("receive")
def receive_something(data):
    print("received message: " + data)


if __name__ == "__main__":
    socketio.run(app)
