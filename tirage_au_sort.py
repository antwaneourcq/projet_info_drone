import random
import lecture_drones as ldr
import mappy
import trajet






NMAX_CL = 150#nombre maximal de clients autorisés
NMAX_EN = 10 #nombre maximal d'entrepôts autorisés
NMAX_DR = 10 #nombre maximal de drones autorisés

#plage d'altitude de mouvement des drones
Z_ALT_MIN = 300
Z_ALT_MAX = 600
STEP = 25

FILE = "aircraft.json"
dico = ldr.read(FILE)
MODELS = ldr.listmodels(dico)


def points_utiles(carte): #changer le nom de la fonction
    '''renvoie la liste des entrepôts et des clients et carte est une liste de 2 tuples de coordonnées, donnant le coin supérieur gauche et le coin inférieur droit'''

    nbr_entrepots = random.randint(5, NMAX_EN)
    nbr_clients = random.randint(nbr_entrepots, NMAX_CL)
    l_entrepots, l_clients = [], []    #l_clients: liste d'objets de la classe client, l_entrepots: liste d'objets de la classe entrepots
    A_int, C_int, A_ext, C_ext = mappy.carre_int(carte)
    
    zone_droite = [A_ext.x, A_int.x, A_ext.y, C_int.y]       #0
    zone_sup = [A_ext.x, C_int.x, C_int.y, C_ext.y]          #1
    zone_gauche = [C_int.x, C_ext.x, A_int.y, C_ext.y]       #2
    zone_inf = [A_int.x, C_ext.x, A_ext.y, A_int.y]          #3
    zones = [ zone_droite, zone_sup, zone_gauche, zone_inf ]
    
    for id in range(1, nbr_entrepots):
        p = random.randint(0, 3)   #p est assimilé à l'une des zones alétoirement
        x, y = random.uniform(zones[p][0], zones[p][1]), random.uniform(zones[p][2], zones[p][3])
        l_entrepots.append(trajet.Entrepot(x, y, 0, MODELS, id))
    
    for _ in range(nbr_clients):
        x, y, z, t = random.uniform(A_int.x,C_int.x), random.uniform(A_int.y,C_int.y), 0, random.randint(0, 86400)
        #à l'instant t le client confirme sa commande
        l_clients.append(trajet.Client(x, y, z, t))
    return l_entrepots, l_clients




def drones_utiles(entrepots):
    '''renvoie un dictionnaire assimilant entre 1 et 10 drones à un entrepot'''
    for entr in entrepots:   #entr: objet de la classe Entrepot
        p = random.randint(1, NMAX_DR)
        for _ in range(p):
            drone = random.choice(MODELS) 
            entr.add_drone(drone)
    return entrepots


def alt_random():
    '''donne aleatoirement un palier d'altitude'''
    return random.randrange(Z_ALT_MIN, Z_ALT_MAX, STEP)











