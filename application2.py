from flask import Flask
import time
import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

app = Flask(__name__)

@app.route('/')
def index():
    current_time = time.strftime("%H:%M:%S")
    return f"{current_time} - Serving from {hostname} ({ip_address})\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

