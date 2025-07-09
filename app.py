from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import numpy as np

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
CORS(app)  # Allow Cross-Origin Request for WebGPU and SocketIO
socketio = SocketIO(app)

# In-memory storage for chat messages
chat_messages = []

@app.route('/')
def home():
    return render_template('index.html')  # Serve the HTML for the front end

@socketio.on('send_message')
def handle_send_message(data):
    print('Received message:', data)
    chat_messages.append(data)  # Store the message
    emit('receive_message', data, broadcast=True)  # Broadcast to all users

@socketio.on('get_messages')
def handle_get_messages():
    emit('receive_all_messages', chat_messages)  # Send all messages to the user

if __name__ == '__main__':
    socketio.run(app, debug=True)
