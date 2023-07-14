import socket
import threading
import sys

PORT = 5000
HOST = socket.gethostbyname(socket.gethostname())


def server_start(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ADDR = (HOST, port)
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
    print(f"[NEW CONNECTION] {address} connected..")

    while True:
        message = conn.recv(1024).decode()
        if not message:
            break
        print(f"[FROM {address}]: " + message)

        reply = input("[FROM SERVER]: ")
        
        while not reply.strip():
            reply = input("[FROM SERVER]: ")

        conn.send(reply.encode())
  
    
    conn.close()



if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("FORMAT: python server.py PORT")
        sys.exit(0)

    input_port = int(sys.argv[1])

    if(input_port != PORT):
        print("Invalid Port Given")
        sys.exit(0)

    server_start(input_port)
