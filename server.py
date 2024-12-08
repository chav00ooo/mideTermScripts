import socket

# Server Configuration
HOST = '127.0.0.1'  # Bind to localhost for testing
PORT = 65432        # Port to listen on

try:
    # Create and configure the server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")
    
    server_socket.bind((HOST, PORT))
    print(f"Socket bound to {HOST}:{PORT}")
    
    server_socket.listen(5)  # Allow up to 5 queued connections
    print("Socket is listening for incoming connections")
    
    while True:
        # Accept a connection
        client_socket, client_address = server_socket.accept()
        print("Connected from: ", client_address)
        
        # Receive and print the message from the client
        client_message = client_socket.recv(1024).decode()
        print(f"Client says: {client_message}")
        
        # Send a message to the client
        message = "Hello, how are you?"
        client_socket.send(message.encode())
        
        # Close the client connection
        client_socket.close()
        print("Connection closed")
except KeyboardInterrupt:
    print("\nServer shutting down...")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Ensure the server socket is closed on exit
    server_socket.close()
    print("Server socket closed")

