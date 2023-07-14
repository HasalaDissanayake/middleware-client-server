import socket
import sys


def start_client(server_ip, port):
    client_socket = socket.socket()
    client_socket.connect((server_ip, port))

    print(f"Connected to server {server_ip} on {port}")

    while True:
        message = input("Enter a message (type 'terminate' to exit): ")
        client_socket.send(message.encode())
        if message == "terminate":
            break

    print("Disconnected from server")

    client_socket.close()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("FORMAT: python client.py SERVER_IP PORT")
        sys.exit(1)

    server_ip = sys.argv[1]
    port = int(sys.argv[2])
    start_client(server_ip, port)
