
import geometry
import mappy


import numpy as np


import random
from random import uniform, randint, choice
import matplotlib.pyplot as plt



NMAX_CL = 50 #nombre maximal de clients autorisés
NMAX_EN = 50 #nombre maximal d'entrepôts autorisés
#carte est une liste de 2 points, donnant le coin inférieur gauche et le coin supérieur droit





def points_utiles(carte):
    '''renvoie la liste des entrepots et des clients
    uniform genere un nombre réel aléatoire dans l'intervalle donné
    je decoupe le contour en quatre espace , 1=espace superieur , 2= espace droit , 3= espace inferieur , 4= espace gauche


    p est assimilé à l'un de ces espaces alétoirement'''

    nbr_entrepots , nbr_clients = random.randint(5, NMAX_EN) , random.randint(0, NMAX_CL)
    A_ext, C_ext = mappy.conversion_deg_m(carte[0]) , mappy.conversion_deg_m(carte[1])
    l_entrepots, l_clients = [] , []
    A_int, C_int = mappy.carre_int(carte)
    print('int', A_int, C_int, '\n')
    print('ext', A_ext, C_ext, '\n')

    carre_ext = [[(A_ext.x , A_int.x),(A_ext.y , C_int.y)] , [(A_ext.x , C_int.x),( C_int.y, C_ext.y)] , [( C_int.x, C_ext.x),(A_int.y , C_ext.y)] , [(A_int.x , C_ext.x),(A_ext.x, A_int.x)]]
    for _ in range(nbr_entrepots) :
        p = randint(0, 3)
        x,y,z = random.uniform(carre_ext[p][0][0],carre_ext[p][0][1]),random.uniform(carre_ext[p][1][0],carre_ext[p][1][1]),0
        l_entrepots.append(geometry.Point(x,y,z))
    for _ in range(nbr_clients):
        l_clients.append(geometry.Point(random.uniform(A_int.x,C_int.x) ,random.uniform(A_int.y,C_int.y) , 0))
    return l_entrepots,l_clients , carre_ext

 
    

carte = (mappy.A, mappy.C)
l_entrepots, l_clients, carre_ext =points_utiles(carte)
print(l_entrepots)
print(l_clients)
print(carre_ext)
x_entrepots,y_entrepots , x_clients, y_clients =[],[] , [],[]
for i in range(len(l_entrepots)):
    x_entrepots.append(l_entrepots[i].x)
    y_entrepots.append(l_entrepots[i].y)
for i in range(len(l_clients)):
    x_clients.append(l_clients[i].x)
    y_clients.append(l_clients[i].y)
plt.plot(x_entrepots,y_entrepots, 'x')
plt.plot(x_clients,y_clients , 'x')
plt.show()


'''def drones_utiles(dictionnary0,carte):
    renvoie un dictionnaire assimilant entre 1 et 10 drones à un entrepot
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

















