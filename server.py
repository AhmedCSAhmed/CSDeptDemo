from flask import Flask, request, render_template, jsonify
from flask_socketio import SocketIO
from profanity_check import predict

app = Flask(__name__, static_url_path='/static')
socketio = SocketIO(app)

@app.route("/", methods=["GET","POST"])
def hello_world():
    if request.method == "POST":
        # User message recieved, process it.

        email = request.json.get('email')
        message = request.json.get('message')
        
        if predict([message])[0] == 0:
            # If the message is clean. Emit then send success response.
            if len(message) > 128:
                return jsonify(
                    {
                        "status": "error",
                        "message": "Message is too long."
                    }
                )
            
            socketio.emit('chatroom', {'data': message, 'email': email})
            return jsonify(
                {
                    "status": "success"
                }
            )
        else:
            # If the message isn't clean.
            return jsonify(
                {
                    "status": "error",
                    "message": "Message contains inappropriate content."
                }
            )
    else:
        # Send HTML Page
        return render_template('index.html')
    

if __name__ == "__main__":
    socketio.run(app)