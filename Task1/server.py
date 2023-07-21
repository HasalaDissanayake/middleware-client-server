import socket
import sys


def start_server(port):  # start server

    server_socket = socket.socket()
    # bind the socket to localhost ip address which is 127.0.0.1 and port number
    server_socket.bind(('localhost', port))
    server_socket.listen()

    print(f"Server started and listening on port {port}")

    client_socket, client_address = server_socket.accept()
    print(f"Client connected from {client_address}")

    while True:
        data = client_socket.recv(1024).decode()
        if data == "terminate":
            break
        print(f"Received from client {client_address} : {data}")

    print(f"Client {client_address} disconnected")

    # close the client socket
    client_socket.close()


if __name__ == '__main__':

    # Checking for the required format
    if len(sys.argv) != 2:
        print("FORMAT: python server.py PORT")
        sys.exit(1)

    port = int(sys.argv[1])

    # Checking for the valid port number
    if (port <= 1024 or port > 65535):
        print("Invalid port number (Try a port between 1025 and 65535)")
        sys.exit(1)

    start_server(port)
