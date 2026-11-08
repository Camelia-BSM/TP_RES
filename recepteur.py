import socket #la bibliotheque socket permet la creation de sockets

UDP_IP = "127.0.0.1" #IP du recepteur (ici adresse de rebouclage)
UDP_PORT = 5005 #port du recepteur
BUFFER_SIZE = 1024 #taille du tampon, par convention 10 octets

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #creation socket en ipv4(AF_INET) via UDP(SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT)) #on lie le port 5005 a l'adreese IP de la machine pour l'ecoute

while True: #recpetion continue
    data, addr = sock.recvfrom(BUFFER_SIZE) #attente de reception du couple message envoye en bytes encodes utf-8/adresse en datagramme UDP
    print(data.decode('utf-8')) #messge utf-8 vers str puis affichage