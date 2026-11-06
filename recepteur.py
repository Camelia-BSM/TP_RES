import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
BUFFER_SIZE = 1024

Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
Socket.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = Socket.recvfrom(BUFFER_SIZE)
    print(data.decode('utf-8'))