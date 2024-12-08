import socket

try:
    s = socket.socket()
    port = 65432
    s.connect(('127.0.0.1', port))
    print(s.recv(1024).decode())
    
except ConnectionRefusedError:
    print("Error: Unable to connect to the server. Is it running?")
except socket.gaierror:
    print("Error: Invalid hostname or IP address.")
except ConnectionResetError:
    print("Error: The server closed the connection unexpectedly.")
except KeyboardInterrupt:
    print("Client script interrupted by user.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    s.close()
    
   
    
