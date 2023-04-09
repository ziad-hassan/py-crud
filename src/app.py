from flask import Flask, jsonify, render_template
import socket

app = Flask(__name__)

# Functions
def fetchDetails():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return hostname, ip

# Routes
@app.route("/")
def hello_world():
    return "<p>Default Webpage</p>"

@app.route("/health")
def health():
    return jsonify(
            STATUS="UP"
        )

@app.route("/details")
def details():
    hostname, ip = fetchDetails()
    return render_template('index.html', HOSTNAME=hostname, IP=ip)

if __name__ == '__main__':
    fetchDetails()
    app.run(host="127.0.0.1", port=5000)