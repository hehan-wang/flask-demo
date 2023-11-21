# 引入 Flask 和 Flask-SocketIO 的必要组件
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

# 创建 Flask 应用实例
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'  # 设置一个秘钥，用于会话安全

# 创建 SocketIO 实例，并与 Flask 应用关联
socketio = SocketIO(app)

# 定义路由，当访问网站根目录时返回 index.html 页面
@app.route('/')
def index():
    return render_template('index.html')

# SocketIO 事件处理器。当服务器接收到客户端发送的 'message' 事件时触发
@socketio.on('message')
def handle_message(message):
    emit('message','服务端收到了：'+ message+ ' 并进行返回', broadcast=True)  # 将收到的消息广播给所有连接的客户端

# 启动 Flask 应用，debug=True 表示开启调试模式
if __name__ == '__main__':
    socketio.run(app, debug=True)
