import geometry

import drones
import numpy as np
dico = drones.read("aircraft.json")
import random
from random import uniform, randint, choice


NMAX_CL = 50 #nombre maximal de clients autorisés
NMAX_EN = 50 #nombre maximal d'entrepôts autorisés
#carte est une liste de 2 points, donnant le coin inférieur gauche et le coin supérieur droit


def bordure (p,carte):
    '''renvoie true si le point appartient à la bordure'''
    l_x , l_y = carte[1].x -  carte[0].x , carte[1].y -  carte[0].y
    return 0 < p.x < 0.1*l_x or 0.9*l_x < p.x < l_x or 0 < p.y < 0.1*l_y or 0.9*l_y < p.y < l_y




def points_utiles(carte):
    '''renvoie la liste des entrepots et des clients
    uniform genere un nombre réel aléatoire dans l'intervalle donné
    je decoupe le contour en quatre espace , 1=espace superieur , 2= espace droit , 3= espace inferieur , 4= espace gauche

    p est assimilé à l'un de ces espaces alétoirement'''
    nbr_entrepots , nbr_clients = random.randint(5, NMAX_EN) , random.randint(0, NMAX_CL)
    l_x, l_y = carte[1].x - carte[0].x, carte[1].y - carte[0].y
    l_entrepots, l_clients = [] , []
    while len(l_entrepots)!= nbr_entrepots :
        p = geometry.Point(random.uniform(0,l_x), random.uniform(0,l_y),0)
        if bordure(p,carte) :
            l_entrepots.append(p)
        elif len(l_clients) < nbr_clients :
            l_clients.append(p)
    while len(l_clients) != nbr_clients :
        p = geometry.Point(random.uniform(0,l_x), random.uniform(0,l_y), 0)
        if not bordure(p, carte) :
            l_clients.append(p)
    return [l_entrepots , l_clients]









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
carte = (geometry.Point(0,0,0),geometry.Point(10,10,0))
print(points_utiles(carte)[0])
entrepots_x , entrepots_y = np.array([Point.x for Point in points_utiles(carte)[0]]) , np.array([Point.y for Point in points_utiles(carte)[0]])
clients_x , clients_y = np.array([Point.x for Point in points_utiles(carte)[1]]) , np.array([Point.y for Point in points_utiles(carte)[1]])

plt.plot(entrepots_x,entrepots_y)
l=plt.plot(clients_x , clients_y)
plt.setp(l,markersize = 10)
plt.setp(l,markerfacecolor='C0')

plt.show()










