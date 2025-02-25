import os
import pty
import subprocess
import select
import threading
from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

process = None

def read_from_process(fd):
    """ Continuously read output from the pseudo-terminal and send to frontend """
    while True:
        ready, _, _ = select.select([fd], [], [], 0.1)
        if ready:
            output = os.read(fd, 1024).decode("utf-8")
            socketio.emit("terminal_output", {"output": output})

@socketio.on("terminal_input")
def handle_terminal_input(data):
    """ Receive input from frontend and send to the terminal process """
    global process
    if process:
        os.write(process, data["input"].encode("utf-8"))

if __name__ == "__main__":
    # Start a new pseudo-terminal session
    process, master_fd = pty.openpty()
    subprocess.Popen(["python3", "py/comma_separated.py"], stdin=process, stdout=process, stderr=process, close_fds=True)

    threading.Thread(target=read_from_process, args=(master_fd,), daemon=True).start()
    print("Terminal Ready. Access via frontend.")

    socketio.run(app, host="127.0.0.1", port=5000, allow_unsafe_werkzeug=True)
