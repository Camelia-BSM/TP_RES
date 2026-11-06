import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("Entrez votre message envoyé au serveur")
    data = msg.encode("utf-8")
    sock.sendto(data, (UDP_IP, UDP_PORT))