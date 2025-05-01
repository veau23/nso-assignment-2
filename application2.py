import flask
import time
import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

app = Flask(_name_)

@app.route('/')
def index():
    current_time = time.strftime("%H:%M:%S")
    return f"{current_time} - Serving from {hostname} ({ip_address})\n"

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=8000,debug=True)
    

