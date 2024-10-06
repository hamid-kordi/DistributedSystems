import socket
from socket import AF_INET, SOCK_STREAM


def start_client():
    new_socket = socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)

    new_socket.connect(("localhost", 55440))

    try:
        new_socket.sendall("server how are you ".encode("utf-8"))
        data = new_socket.recv(1024)
        print(f"this is data recieved {data.decode()}")

    finally:
        new_socket.close()


if __name__ == "__main__":
    start_client()
