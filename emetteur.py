## Malo BOUDIER AEBISCHER, Camelia BENSEMMANE

import socket #la bibliotheque socket permet la creation de sockets

UDP_IP = "127.0.0.1" #IP du recepteur (ici adresse de rebouclage)
UDP_PORT = 5005 #port du recepteur
BUFFER_SIZE = 1024 #taille du tampon, par convention 10 octets

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #creation socket en ipv4(AF_INET) via UDP(SOCK_DGRAM)

while True: #boucle infinie d'envoie de message
    msg = input("Entrez votre message envoyé au serveur: ") #on invite l'emetteur a rentrer un message
    data = msg.encode("utf-8") #on encode le message d'un str vers des bytes en utf-8 pour l'envoi
    sock.sendto(data, (UDP_IP, UDP_PORT)) #on envoie les donnees "data" vers le recepteur en UDP