#! /usr/bin/env python3

# boolean func to check localhost and network connectivity - Internet access

import requests
import socket
def check_localhost():
    localhost = socket.gethostbyname ('localhost')
    if localhost == '127.0.0.1':
        return True
    return False
def check_connectivity():
    request = requests.get('http://www.google.com')
    response = request.status_code
    if response == 200:
        return True
    return False