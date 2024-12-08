import socket
from datetime import datetime

# Server configuration
HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port to listen on

try:
    # Create and configure the server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"[{datetime.now()}] Socket successfully created")
    
    server_socket.bind((HOST, PORT))  # Bind to address and port
    print(f"[{datetime.now()}] Socket bound to {HOST}:{PORT}")
    
    server_socket.listen(5)  # Allow up to 5 queued connections
    print(f"[{datetime.now()}] Socket is listening for incoming connections")
    
    while True:
        # Accept a connection
        client_socket, client_address = server_socket.accept()
        print(f"[{datetime.now()}] Connected from: {client_address}")
        
        # Send a message to the client
        greeting_message = "Hello, how are you?"
        client_socket.send(greeting_message.encode())
        print(f"[{datetime.now()}] Sent to client: {greeting_message}")
        
        # Receive a response from the client
        response = client_socket.recv(1024).decode()
        if response:
            print(f"[{datetime.now()}] Client says: {response}")
        else:
            print(f"[{datetime.now()}] No response received from client.")
        
        # Close the client connection
        client_socket.close()
        print(f"[{datetime.now()}] Connection closed")
except KeyboardInterrupt:
    print(f"\n[{datetime.now()}] Server shutting down...")
except Exception as e:
    print(f"[{datetime.now()}] An error occurred: {e}")
finally:
    # Ensure the server socket is closed on exit
    server_socket.close()
    print(f"[{datetime.now()}] Server socket closed")
