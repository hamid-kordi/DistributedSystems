import socket
from socket import AF_INET,SOCK_STREAM



def start_connection():
    new_socket = socket.socket(family=AF_INET,type=SOCK_STREAM,proto=0,fileno=None)
    new_socket.bind(('localhost',55440))
    new_socket.listen(5)

    while True:
        clinet_socket, client_address = new_socket.accept()
        data = clinet_socket.recv(1024)
        if data:
            print(f"{data.decode()} recievd from client")
            print(f"{client_address}   this is the client address")

            print("hello clinet")
        clinet_socket.close()


if __name__ == "__main__":
    start_connection()
        





