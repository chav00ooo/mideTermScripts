import socket

s = socket.socket()
print("Socket successfully created")  
port = 65432 
s.bind(('', port))
print(f'socket binded to {port}')
s.listen(5)
print("socket is listening")
while True:
    c, addr = s.accept()
    print("Connected from: ", addr)
    message = "Hello, how are you?"
    c.send(message.encode())
    c.close() 

