import socket
import sys

PORT = 5000
HOST = socket.gethostbyname(socket.gethostname())


def client_start(server, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ADDR = (server, port)
    client_socket.connect(ADDR)
    client_address = client_socket.getsockname()

    message = input(f"[CLIENT {client_address}]: ")

    while message.lower().strip() != 'terminate':
        if message.strip():
            client_socket.send(message.encode())
            reply = client_socket.recv(1024).decode()
            print("[FROM SERVER]: " + reply)

            message = input(f"[CLIENT {client_address}]: ")
        else:
            message = input(f"[CLIENT {client_address}]: ")
    
    print(f"[SESSION {client_address} TERMINATED]")
    client_socket.close()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("FORMAT: python client.py SERVER_IP SERVER_PORT")
        sys.exit(0)

    input_server = sys.argv[1]
    input_port = int(sys.argv[2])

    if(input_port != PORT):
        print("Invalid Server Port Given")
        sys.exit(0)

    if(input_server != HOST):
        print("Invalid Server IP Given")
        sys.exit(0)


    client_start(input_server, input_port)
