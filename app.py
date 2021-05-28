import os
import socket

from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "I am from " + socket.gethostbyname(socket.gethostname())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)