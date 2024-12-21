import socket
from datetime import datetime

# Server configuration
HOST = '127.0.0.1'  # The server will bind to localhost
PORT = 65432        # Port on which the server will listen for connections

try:
    # Create and configure the server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4, TCP socket
    print(f"[{datetime.now()}] Socket successfully created")
    
    # Bind the socket to the specified host and port
    server_socket.bind((HOST, PORT))
    print(f"[{datetime.now()}] Socket bound to {HOST}:{PORT}")
    
    # Start listening for incoming connections, allowing up to 5 queued clients
    server_socket.listen(5)
    print(f"[{datetime.now()}] Socket is listening for incoming connections")
    
    while True:
        # Accept an incoming connection from a client
        client_socket, client_address = server_socket.accept()  # Blocks until a client connects
        print(f"[{datetime.now()}] Connected from: {client_address}")
        
        # Send a greeting message to the connected client
        greeting_message = "Hello, how are you?"
        client_socket.send(greeting_message.encode())  # Send the message in encoded format
        print(f"[{datetime.now()}] Sent to client: {greeting_message}")
        
        # Wait for a response from the client
        response = client_socket.recv(1024).decode()  # Receive up to 1024 bytes and decode it
        if response:
            print(f"[{datetime.now()}] Client says: {response}")  # Log the client's response
        else:
            print(f"[{datetime.now()}] No response received from client.")  # Handle empty response
        
        # Close the connection with the current client
        client_socket.close()
        print(f"[{datetime.now()}] Connection closed")
except KeyboardInterrupt:
    # Gracefully handle a manual interruption (Ctrl+C)
    print(f"\n[{datetime.now()}] Server shutting down...")
except Exception as e:
    # Catch and report any unexpected errors
    print(f"[{datetime.now()}] An error occurred: {e}")
finally:
    # Ensure the server socket is properly closed on exit
    server_socket.close()
    print(f"[{datetime.now()}] Server socket closed")
