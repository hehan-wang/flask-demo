from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    emit('message','服务端收到了：'+ message+ ' 并进行返回', broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
