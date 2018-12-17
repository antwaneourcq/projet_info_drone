
import trajet
import geometry as geo, lecture_drones as lect_dr, mappy
import numpy as np
import random
from random import uniform, randint, choice
import matplotlib.pyplot as plt



dico = lect_dr.read("aircraft.json")

NMAX_CL = 50 #nombre maximal de clients autorisés
NMAX_EN = 10 #nombre maximal d'entrepôts autorisés
NMAX_DR = 10
#carte est une liste de 2 tuples, donnant le coin supérieur gauche et le coin inférieur droit

MODELS = lect_dr.listmodels(dico)
    
class Entrepot(geo.Point):
    
    def __init__(self, x, y, z, models):
        super().__init__(x, y, z)
        self.models = {}
        for model in models:
            self.models[str(model)] = 0
        self.drones = []
    
    def __repr__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ',' + str(self.z) +')' + ' drones : ' +str(self.drones)
    
    def addDrone(self, drone):
        model= str(drone.model)
        self.models[model] += 1
        if self.models[model] == 1:
            self.drones.append(model)
    
    #def maj_drone_effectifs(self):
    #    '''met à jour le dictionnaire de "drones_effectifs" par rapport aux données du dictionnaire "drones"'''
    #    for model in self.models:
    #        pass

        
def points_utiles(carte):
    '''renvoie la liste des entrepôts et des clients
    uniform génère un nombre réel aléatoire dans l'intervalle donné
    je decoupe le contour en quatre espace , 1=espace superieur , 2= espace droit , 3= espace inferieur , 4= espace gauche
    p est assimilé à l'un de ces espaces alétoirement'''


    nbr_entrepots , nbr_clients = random.randint(5, NMAX_EN) , random.randint(0, NMAX_CL)
    A_ext, C_ext = mappy.conversion_deg_m(carte[0]) , mappy.conversion_deg_m(carte[1])
    l_entrepots, l_missions = [] , []
    A_int, C_int = mappy.carre_int(A_ext, C_ext)
    carre_ext = [[(A_ext.x , A_int.x),(A_ext.y , C_int.y)] , [(A_ext.x , C_int.x),( C_int.y, C_ext.y)] , [( C_int.x, C_ext.x),(A_int.y , C_ext.y)] , [(A_int.x , C_ext.x),(A_ext.x, A_int.x)]]
    for _ in range(nbr_entrepots) :
        p = randint(0, 3)
        x,y,z = random.uniform(carre_ext[p][0][0],carre_ext[p][0][1]),random.uniform(carre_ext[p][1][0],carre_ext[p][1][1]),0
        l_entrepots.append(geo.Point(x,y,z))
        x,y = random.uniform(carre_ext[p][0][0],carre_ext[p][0][1]),random.uniform(carre_ext[p][1][0],carre_ext[p][1][1])
        l_entrepots.append(Entrepot(x, y, 0, MODELS))
    for _ in range(nbr_clients):
        client = geo.Point(random.uniform(A_int.x,C_int.x) ,random.uniform(A_int.y,C_int.y) , 0)
        mission= trajet.mission(client, carte)
        mission.heure_livr = random.randint(0,24)
        l_missions.append(trajet.mission.client(random.uniform(A_int.x,C_int.x) ,random.uniform(A_int.y,C_int.y) , 0))
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






def drones_utiles(dico, entrepots):
    '''renvoie un dictionnaire assimilant entre 1 et 10 drones à un entrepot'''
    models = lect_dr.listmodels(dico)

    for entrepot in entrepots:
        p=randint(1,NMAX_DR)
        for _ in range (p) :
            drone = random.choice(models)
            entrepot.addDrone(drone)
    #return entrepots


def test():
    dico = lect_dr.read("aircraft.json")
    models = lect_dr.listmodels(dico)
    carte = (mappy.A, mappy.C)
    l_entrepots, l_clients, carre_ext = points_utiles(carte)
    x_entrepots,y_entrepots , x_clients, y_clients =[],[] , [],[]
    for i in range(len(l_entrepots)):
        x_entrepots.append(l_entrepots[i].x)
        y_entrepots.append(l_entrepots[i].y)
    for i in range(len(l_clients)):
        x_clients.append(l_clients[i].x)
        y_clients.append(l_clients[i].y)
    plt.plot(x_entrepots,y_entrepots, '.')
    plt.plot(x_clients,y_clients, '.')
    plt.show()
    print(drones_utiles(dico, l_entrepots))
#test()












