from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static')

@app.route("/", methods=["GET","POST"])
def hello_world():
    if request.method == "POST":
        # User message recieved, process it.
        return "<p>Hello, World!</p>"
    else:
        # Send HTML Page
        return render_template('index.html')