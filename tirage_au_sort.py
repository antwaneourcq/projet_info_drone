import geometry as geo, lecture_drones as lect_dr, mappy
import random
from random import uniform, randint, choice
import matplotlib.pyplot as plt

NMAX_CL = 50 #nombre maximal de clients autorisés
NMAX_EN = 10 #nombre maximal d'entrepôts autorisés
#carte est une liste de 2 tuples, donnant le coin supérieur gauche et le coin inférieur droit
class Entrepot(geo.Point):
    
    def __init__(self, x, y, z, models):
        super().__init__(x, y, z)
        self.drones = {}
        for model in models:
            self.drones[str(model)] = 0
    
    def __repr__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ',' + str(self.z) +')\n' + 'drones : ' +str(self.drones)
    
def points_utiles(carte):
    '''renvoie la liste des entrepôts et des clients
    uniform génère un nombre réel aléatoire dans l'intervalle donné
    je decoupe le contour en quatre espace , 1=espace superieur , 2= espace droit , 3= espace inferieur , 4= espace gauche
    p est assimilé à l'un de ces espaces alétoirement'''

    nbr_entrepots , nbr_clients = random.randint(5, NMAX_EN) , random.randint(0, NMAX_CL)
    A_ext, C_ext = mappy.conversion_deg_m(carte[0]) , mappy.conversion_deg_m(carte[1])
    l_entrepots, l_clients = [] , []
    A_int, C_int = mappy.carre_int(A_ext, C_ext)
    carre_ext = [[(A_ext.x , A_int.x),(A_ext.y , C_int.y)] , [(A_ext.x , C_int.x),( C_int.y, C_ext.y)] , [( C_int.x, C_ext.x),(A_int.y , C_ext.y)] , [(A_int.x , C_ext.x),(A_ext.x, A_int.x)]]
    for _ in range(nbr_entrepots) :
        p = randint(0, 3)
        x,y = random.uniform(carre_ext[p][0][0],carre_ext[p][0][1]),random.uniform(carre_ext[p][1][0],carre_ext[p][1][1])
        l_entrepots.append(Entrepot(x, y, 0, models))
    for _ in range(nbr_clients):
        l_clients.append(geo.Point(random.uniform(A_int.x,C_int.x) ,random.uniform(A_int.y,C_int.y) , 0))
    return l_entrepots,l_clients , carre_ext

def drones_utiles(dico, entrepots):
    '''renvoie un dictionnaire assimilant entre 1 et 10 drones à un entrepot'''
    models = lect_dr.listmodels(dico)

    for entrepot in l_entrepots:
        p=randint(1,10)
        p = 50
        for _ in range (p) :
            drone = random.choice(models)
            entrepot.drones[str(drone)] += 1
    return entrepots


def test():
    dico = lect_dr.read("aircraft.json")
    model = lect_dr.listmodels(dico)
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












