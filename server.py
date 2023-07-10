import socket
import threading
import sys

PORT = 5000
HOST = socket.gethostbyname(socket.gethostname())
ADDR = (HOST, PORT)


def server_start(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(ADDR)
    print("[STARTING] server is starting...")
    server_socket.listen()
    print(f"[LISTENING] Server is listening on {HOST}")

    while True:
        conn, address = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(conn,address))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


def handle_client(conn, address):
    print(f"[NEW CONNECTION] {address}")

    


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("FORMAT: python server.py PORT")
        sys.exit(0)

    input_port = int(sys.argv[1])

    if(input_port != 5000):
        print("Invalid Port Given")
        sys.exit(0)

    server_start(input_port)
