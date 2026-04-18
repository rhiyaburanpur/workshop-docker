from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Docker Workshop Demo</h1>
    <p>This app is running inside a Docker container.</p>
    <ul>
        <li><a href="/info">/info</a> — container info</li>
        <li><a href="/health">/health</a> — health check</li>
    </ul>
    """

@app.route("/info")
def info():
    return jsonify({
        "hostname": socket.gethostname(),
        "environment": os.environ.get("APP_ENV", "not set"),
        "message": "Hello from inside the container!"
    })

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
