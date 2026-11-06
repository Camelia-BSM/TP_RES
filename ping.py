
import socket
import time
UDP_IP = "127.0.0.1"
UDP_PORT = 7777
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
counter = 0
while True:
    msg = input("Entrez votre message envoyé au serveur : ")
    t1 = time.time()
    data = msg.encode("utf-8")
    print(f"Sent 'ping {counter}' to {UDP_IP}")
    sock.sendto(data, (UDP_IP, UDP_PORT))
    data_reçue, addr = sock.recvfrom(BUFFER_SIZE)
    t2 = time.time()
    RTT = t2-t1
    print(f"Received 'ping {counter}' from {UDP_IP}, RTT = {RTT}")
    counter=counter+1
    

