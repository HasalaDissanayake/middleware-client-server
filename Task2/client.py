import socket
import sys
import threading


def handle_received_data(client_socket):    # print data sent by the server

    try:            # when "terminate" given thread will give a exqception
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            print(f"\nRecieved Message : {data}")

    except:
        pass


def start_client(server_ip, port, category):      # start the client

    client_socket = socket.socket()
    client_socket.connect((server_ip, port))

    print(f"Connected to server {server_ip} on {port}")

    client_socket.send(f"{category}".encode())

    if category == "SUBSCRIBER":        # filter subscribers from the clients
        receive_thread = threading.Thread(
            target=handle_received_data, args=(client_socket,))
        receive_thread.start()

    while True:
        message = input("\nEnter a message (type 'terminate' to exit): ")
        client_socket.send(f"{message}".encode())
        if message == "terminate":
            break

    print("Disconnected from server")

    client_socket.close()


if __name__ == '__main__':

    # Checking for the required format
    if len(sys.argv) != 4:
        print("FORMAT: python client.py SERVER_IP PORT CATEGORY")
        sys.exit(1)

    server_ip = sys.argv[1]
    port = int(sys.argv[2])
    category = sys.argv[3]

    # Checking for the valid port number
    if (port <= 1024 or port > 65535):
        print("Invalid port number (Try a port between 1025 and 65535)")
        sys.exit(1)

    # Cheking for the valid category
    if (category != "PUBLISHER" and category != "SUBSCRIBER"):
        print("Invalid category (Try PUBLISHER or SUBSCRIBER)")
        sys.exit(1)

    start_client(server_ip, port, category)
