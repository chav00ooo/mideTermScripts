import socket
from datetime import datetime

try:
    # Create a client socket
    # This socket will establish a connection to the server
    client_socket = socket.socket()  # Default: IPv4 and TCP
    port = 65432  # Port to connect to on the server

    # Attempt to connect to the server at the specified address and port
    client_socket.connect(('127.0.0.1', port))
    print(f"[{datetime.now()}] Connected to the server")  # Confirm successful connection

    # Receive a message from the server
    # The recv() method fetches up to 1024 bytes of data from the server
    greeting_message = client_socket.recv(1024).decode()  # Decode received bytes into a string
    print(f"[{datetime.now()}] Server says: {greeting_message}")  # Display the server's message

    # Prepare and send a response back to the server
    # This response confirms successful bidirectional communication
    response_message = "I'm doing great, thanks!"
    print(f"[{datetime.now()}] Preparing to send: {response_message}")  # Log the response
    client_socket.send(response_message.encode())  # Encode and send the response message
    print(f"[{datetime.now()}] Message sent to the server.")  # Confirm the message was sent
except ConnectionRefusedError:
    # Handle the case where the server is not running or cannot be reached
    print(f"[{datetime.now()}] Error: Unable to connect to the server. Is it running?")
except KeyboardInterrupt:
    # Gracefully handle manual interruption (e.g., Ctrl+C)
    print(f"[{datetime.now()}] Client script interrupted by user.")
except Exception as e:
    # Catch and report any unexpected runtime errors
    print(f"[{datetime.now()}] An unexpected error occurred: {e}")
finally:
    # Ensure the client socket is properly closed after execution
    client_socket.close()
    print(f"[{datetime.now()}] Client socket closed")  # Confirm resource cleanup
