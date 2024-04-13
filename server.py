from flask import Flask, request, render_template
from flask_socketio import SocketIO

app = Flask(__name__, static_url_path='/static')
socketio = SocketIO(app)

@app.route("/", methods=["GET","POST"])
def hello_world():
    if request.method == "POST":
        # User message recieved, process it.

        # Get message from user
        message = request.form.get('message')
        return "<p>Hello, World!</p>"
    else:
        # Send HTML Page
        return render_template('index.html')
    
@socketio.on('chatroom')
def handle_message(message):
    print(message['data'])

if __name__ == "__main__":
    socketio.run(app)