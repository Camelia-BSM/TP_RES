## Malo BOUDIER AEBISCHER, Camelia BENSEMMANE

import socket #la bibliotheque socket permet la creation de sockets
import time #la bibliotheque time est indispensable pour connaitre de RTT

UDP_IP = "127.0.0.1" #IP du recepteur (ici adresse de rebouclage)
UDP_PORT = 7777 #port 7 pour respecter la specification de RFC 862 (7777 en vrai ici, mais c'est pour que ca marche comme dit dans le sujet TP)
BUFFER_SIZE = 1024 #taille du tampon, par convention 10 octets

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #creation socket en ipv4(AF_INET) via UDP(SOCK_DGRAM)
nb = int(input("how many ping would you like to sent toward"+UDP_IP+"? :")) # on demande le nombre de ping a faire
RTT = [] #liste RTT, bien pratique pour les calcul a posteriori

for counter in range(nb): # on effectue le nombre voulu de ping
    msg = "ping "+str(counter)
    data_send = msg.encode("utf-8") #on encode ce message en utf-8
    print("Sent 'ping"+str(counter)+"' to "+UDP_IP) #on previent de l'envoie de message AVANT de lancer l'envoi pour les delais d'affichage
    t1 = time.time() #on lance le chronometre
    sock.sendto(data_send, (UDP_IP, UDP_PORT)) #on envoie les donnees "data" vers le recepteur en UDP
    data_get, addr = sock.recvfrom(BUFFER_SIZE) #attente de reception du couple message envoye en bytes encodes utf-8/adresse en datagramme UDP
    t2 = time.time() #on a recu le paquet, on stop le chronometre 
    RTT.append((t2-t1)*1000) #le RTT en ms
    print("Received 'ping "+str(counter)+"' from "+UDP_IP+", RTT = "+str(RTT[counter])+"ms") # on affiche le message voulue
    assert data_send == data_get #cela ne coute rien de verifier la non alteration des datas

print("Min RTT "+str(min(RTT))+"ms")
print("Avg RTT" +str(sum(RTT)/len(RTT))+"ms")
print("Max RTT "+str(max(RTT))+"ms")
