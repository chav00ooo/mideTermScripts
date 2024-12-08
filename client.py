import socket
from datetime import datetime

try:
    # Create a client socket
    client_socket = socket.socket()
    port = 65432
    client_socket.connect(('127.0.0.1', port))  # Connect to the server
    print(f"[{datetime.now()}] Connected to the server")

    # Receive and print the server's message
    greeting_message = client_socket.recv(1024).decode()
    print(f"[{datetime.now()}] Server says: {greeting_message}")

    # Send a response back to the server
    response_message = "I'm doing great, thanks!"
    print(f"[{datetime.now()}] Preparing to send: {response_message}")
    client_socket.send(response_message.encode())
    print(f"[{datetime.now()}] Message sent to the server.")
except ConnectionRefusedError:
    print(f"[{datetime.now()}] Error: Unable to connect to the server. Is it running?")
except KeyboardInterrupt:
    print(f"[{datetime.now()}] Client script interrupted by user.")
except Exception as e:
    print(f"[{datetime.now()}] An unexpected error occurred: {e}")
finally:
    client_socket.close()
    print(f"[{datetime.now()}] Client socket closed")
