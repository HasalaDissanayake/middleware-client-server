import socket
import sys
import threading

clients = {}    # to store and manage active clients


def manage_client(client_socket, client_address):   # to handle a specific client

    print(f"New client connected from {client_address}")

    data = client_socket.recv(1024).decode()
    category = data         # assigned the category of the client

    clients[client_address] = {'socket': client_socket, 'type': category}

    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break

        if data == "terminate":
            break
        else:
            print(f"Received from client {client_address}: {data}")
            handle_message(client_socket, data)

    del clients[client_address]

    print(f"Client {client_address} disconnected")
    client_socket.close()


# publish message for interested subscribers
def handle_message(sender_socket, content):

    for subscriber_socket in clients:
        # even for a subscriber, the message is not sent to the sender
        if clients[subscriber_socket]['type'] == "SUBSCRIBER" and clients[subscriber_socket]['socket'] != sender_socket:
            clients[subscriber_socket]['socket'].send(content.encode())


def start_server(port):     # start server

    server_socket = socket.socket()
    server_socket.bind(('localhost', port))
    server_socket.listen()

    print(f"Server started and listening on port {port}")

    while True:
        client_socket, client_address = server_socket.accept()

        client_thread = threading.Thread(
            target=manage_client, args=(client_socket, client_address))
        client_thread.start()       # start threading for each client


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
