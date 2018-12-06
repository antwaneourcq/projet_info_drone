import geometry

import drones
import map
dico = drones.read("aircraft.json")
import random
from random import uniform, randint, choice


NMAX_CL = 50 #nombre maximal de clients autorisés
NMAX_EN = 50 #nombre maximal d'entrepôts autorisés
#carte est une liste de 2 tuples, donnant le coin supérieur gauche et le coin inférieur droit





def points_utiles(carte):
    '''renvoie la liste des entrepots et des clients
    uniform genere un nombre réel aléatoire dans l'intervalle donné
    50 correspond au nombre maximum de clients ou d'entrepots , choisi arbitrairement
    uniform génère un nombre réel aléatoire dans l'intervalle donné

    je decoupe le contour en quatre espace , 1=espace superieur , 2= espace droit , 3= espace inferieur , 4= espace gauche

    carre_ext est la list de l'intervalle des abcisses et de l'intervalle des ordonnées pour chaque espace 1,2,3,4

    p est assimilé à l'un de ces espaces alétoirement'''
    nbr_entrepots = uniform(5, NMAX_EN)
    nbr_clients = uniform(0, NMAX_CL)

    l_entrepots = []
    l_clients =[]
    
    A,C = map.carre_int(carte)
    a, b, c, d = carte[0].x, carte[0].y, carte[1].x, carte[1].y
    carre_ext = [[(A.x , c),(C.y , d)] , [(C.x , c),(b , C.y)] , [(a , C.x),(b , A.y)] , [(a , A.x),(A.y, d)]]
    for _ in range(nbr_entrepots) :
        p = randint(1, 4)
        x,y,z = random.uniform(carre_ext[p][0]),random.uniform(carre_ext[p][1],0)
        l_entrepots.append(geometry.Point(x,y,z))

    for _ in range(nbr_clients):
        x,y,z = random.uniform(A.x,C.y) , random.uniform(A.y,C.y) , 0
        l_clients.append(geometry.Point(x,y,z))

    return l_entrepots,l_clients




'''def drones_utiles(dictionnary0,carte):
    renvoie un dictionnaire assimilaant entre 1 et 10 drones à un entrepot
    l_entrepots = points_utiles(carte)[0]
    l_drones_entrepots = {}

    for entrepots in l_entrepots:
        p=randint(1,10)
        for i in range (p) :
            drone = random.choice(drones.drones_list(dictionnary0))
            if not_in_L(drone,drones):
                drones.append((drone,1))
            else: 
                l_drones_entrepots.append(entrepots,drones)

    return l_drones_entrepots'''


import matplotlib.pyplot as plt
carte = (geometry.Point(0,0,0),geometry.Point(20,20,0))
entrepots_x , entrepots_y = [Point.x for Point in points_utiles(carte)[0]] , [Point.y for Point in points_utiles(carte)[0]]
clients_x , clients_y = [Point.x for Point in points_utiles(carte)[1]] , [Point.y for Point in points_utiles(carte)[1]]
plt.plot(entrepots_x,entrepots_y)
plt.plot(clients_x , clients_y)
plt.show()










