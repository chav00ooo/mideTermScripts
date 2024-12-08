import socket

try:
    s = socket.socket()
    port = 65432
    s.connect(('127.0.0.1', port))
    print(s.recv(1024).decode())
except ConnectionRefusedError:
    print("Error: Unable to connect to the server. Is it running?")
finally:
    s.close()
