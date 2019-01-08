
import random
from random import randint
import geometry as geo, lecture_drones as lect_dr, mappy


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
            self.models[str(model)] = 1
        #self.drones = []
        self.id = random.randint(0,100)
    
    def __repr__(self):
        return 'identificateur' + str(self.id) + '(' + str(self.x) + ',' + str(self.y) + ',' + str(self.z) +')' + ' drones : ' +str(self.models)
    
    def addDrone(self, drone):
        # model= str(drone.model)
        self.models[str(drone.model)] += 1
    
    def remove_drone(self, drone):
        if self.models[str(drone)] > 0 : self.models[str(drone)] -= 1
    
    #def maj_drone_effectifs(self):
    #    '''met à jour le dictionnaire de "drones_effectifs" par rapport aux données du dictionnaire "drones"'''
    #    for model in self.models:
    #        pass

        
def points_utiles(carte):
    '''renvoie la liste des entrepôts et des clients
    uniform génère un nombre réel aléatoire dans l'intervalle donné
    je decoupe le contour en quatre espace , 0=espace droit , 1= espace supérieur , 2= espace gauche , 4= espace inférieur
    p est assimilé à l'un de ces espaces alétoirement
    l_clients est une liste d'objets de la classe client , t est en secondes et correspond à l'instant ou le client confirme sa commande et que le drone peut apparaitre sur la carte '''


    nbr_entrepots = random.randint(5, NMAX_EN)
    nbr_clients = random.randint(nbr_entrepots , NMAX_CL)
    l_entrepots, l_clients = [] , []
    A_int, C_int , A_ext , C_ext = mappy.carre_int(carte)
    carre_ext = [[(A_ext.x , A_int.x),(A_ext.y , C_int.y)] , [(A_ext.x , C_int.x),( C_int.y, C_ext.y)] , [( C_int.x, C_ext.x),(A_int.y , C_ext.y)] , [(A_int.x , C_ext.x),(A_ext.x, A_int.x)]]
    for _ in range(nbr_entrepots):
        p = randint(0, 3)
        #une des sources du problèmes....l_entrepots.append(geo.Point(x,y,z))
        x,y = random.uniform(carre_ext[p][0][0],carre_ext[p][0][1]),random.uniform(carre_ext[p][1][0],carre_ext[p][1][1])
        l_entrepots.append(Entrepot(x, y, 0, MODELS))
    for _ in range(nbr_clients):
        x,y,z,t = random.uniform(A_int.x,C_int.x) ,random.uniform(A_int.y,C_int.y) , 0 , random.uniform(0,86400)
        l_clients.append(geo.Timed_Point(x,y,z,t))
    return l_entrepots,l_clients , carre_ext




def drones_utiles(dico, entrepots):
    '''renvoie un dictionnaire assimilant entre 1 et 10 drones à un entrepot'''
    models = lect_dr.listmodels(dico)

    for entrepot in entrepots:
        p=randint(1,NMAX_DR)
        for _ in range (p) :
            drone = random.choice(models)
            entrepot.addDrone(drone)
    return entrepots















