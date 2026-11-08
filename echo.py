import socket #la bibliotheque socket permet la creation de sockets

UDP_IP = "127.0.0.1" #IP du recepteur (ici adresse de rebouclage)
UDP_PORT = 7777 #port 7 pour respecter la specification de RFC 862 (7777 en vrai ici, mais c'est pour que ca marche comme dit dans le sujet TP)
BUFFER_SIZE = 1024 #taille du tampon, par convention 10 octets

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #creation socket en ipv4(AF_INET) via UDP(SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT)) #on lie le port 5005 a l'adreese IP de la machine pour l'ecoute

while True: #boucle infinie
    data, addr = sock.recvfrom(BUFFER_SIZE) #attente de reception du couple message envoye en bytes encodes utf-8/adresse en datagramme UDP
    sock.sendto(data, addr) #renvoie immediat du meme message vers l'emmeteur (on connais addr et data)
    