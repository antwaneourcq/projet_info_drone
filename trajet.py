import Timer
import random
import lecture_drones as lect_dr
import geometry as geo
import math
import tirage_au_sort as tas
import conflits
import math


class Mission:

    def __init__(self, client): #client est un objet de la classe Client
        self.client = client
        self.entrepot = None
        self.heure_dmde = client.t
        self.drone = None
        self.alti = [tas.alt_random()]
        self.deviation = []
        
    def __repr__(self):
        return 'mission :  entrepot : ' + str(self.entrepot) +'\nMission retour ligne\n' #+ ', client : ' + str(self.client) + ', temps : ' + str(self.heure_dmde) + ', drone : ' + str(self.drone)

    def decoupe_trajet(self):
        # renvoie un tuple de 4 points et une durée
        # print('Client : ::: ', mission.client, '\nEntrepot : ', mission.entrepot, '\nDrone : ', mission.drone)
        arr, dep, drone = self.client, self.entrepot, self.drone
        alt = tas.alt_random()
        distance = calcule_distance(self.client, self.entrepot)
        p1 = geo.Timed_Point(dep.x, dep.y, 0, self.heure_dmde)  # 0 correspond à la coordonnée en altitude que je rajoute aux coordonnées de point p1
        p2 = geo.Timed_Point(dep.x, dep.y, alt, distance/self.drone.h_speed_max)
        p3 = geo.Timed_Point(arr.x, arr.y, alt, distance/self.drone.v_speed_max)
        p4 = geo.Timed_Point(arr.x, arr.y, 0)
        return p1, p2, p3, p4, calcul_duree_mission(self.drone, p1, p4)


    def changer_altitude(self,I) :
    # permet de changer l'altitude pendant une mission en cas de conflits
        a = tas.alt_random()
        while a == self.alti[0]:
            a = tas.alt_random()
        self.alti.append(a)
        p2, p3 = self.decoupe_trajet[1] , self.decoupe_trajet(self)[2]
        a,b = conflits.a(p2,p3) , conflits.b(p2,p3)
        angle = math.tan(p3.x/p3.y)
        de1 , de2 = geo.Point()


class Entrepot(geo.Point):

    def __init__(self, x, y, z, models):  # models: liste de modèle de drones
        super().__init__(x, y, z)
        self.models = {}
        for mod in models:
            self.models[str(mod)] = 1
        self.id = random.randint(0, 100)

    def __repr__(self):
        return 'identificateur ' + str(self.id) + '(' + str(self.x) + ',' + str(self.y) + ',' + str(
            self.z) + ')' + ' drones : ' + str(self.models)

    def addDrone(self, drone):
        self.models[str(drone.model)] += 1

    def remove_drone(self, drone):
        if self.models[str(drone)] > 0: self.models[str(drone)] -= 1



class Client(geo.Timed_Point):

    def __init__(self, x, y, z, t, entrepot):
        super().__init__(x, y, z, t)
        self.entrepot = entrepot
        #self.t = t


def ordre_priorite_drones(drones): 
#prend en argument une liste de drones à trier selon leur vitesse maximale
	drones.sort(key = lambda drone : drone.v_speed_max, reverse = True) #on trie les drones de l'entrepot le plus proche par ordre décroissant de vitesse maximale en route (tri en place)
	return drones
	
def calcule_distance(cli,entrepot):
	return math.sqrt((cli.x-entrepot.x)**2+(cli.y-entrepot.y)**2)


def capacite_drone(entrepot, client):
# calcule le drone le plus rapide de l'entrepot capable d'aller livrer jusqu'à chez le client
    distance = calcule_distance(client,entrepot)
    #print('distance =', distance)
    # drones = entrepot.drones
    vit = 1
    for drone in entrepot.models:
        if entrepot.models[drone]>0:
            dro = lect_dr.Drone(drone, geo.Point(entrepot.x, entrepot.y, entrepot.z))
            if dro.range >= distance:
                if dro.v_speed_max > vit:
                    drone_correct = dro
                    vit = dro.v_speed_max
    try:
        return drone_correct  # drone est un objet de la classe Drone du module lecture_drone
    except UnboundLocalError:
        return None


def attribuer_entrepot(entrepots,clients):
    l = len(entrepots)
    for cli in clients :
        if cli.entrepot == None :
            p = random.randint(l-1)
            cli.entepot = entrepots[p]



def attribuer_missions(clients): #clients est une liste d'objets de la classe Client

    '''renvoie une liste de missions , determinées en fonction des clients et entrepots tirés au sort'''
    file_attente = []
    missions = []
    correctness = 0
    drones_non_traites = 0
    for cli in clients:
        e = cli.entrepot
        drone = capacite_drone(e, cli)
        m = Mission(cli)
        if drone != None:
            correctness += 1 
            m.entrepot = e
            m.drone = drone
            e.models[str(drone.model)] -= 1
        else :
            #traiter le cas où le drone est None
            drones_non_traites += 1
            file_attente.append(cli)
        missions.append(m)
        # print('MISSSIONSSSS : ', missions, '\n\nla mission : ', m)
    return missions, file_attente
    #print('\ndrone correct', correctness, 'drones non traités ', drones_non_traites)






def calcul_duree_mission(drone, p1, p4):
    # drone est on objet de la classe Drone du module lecture_drones
    # calcul le temps que met le drone pour faire un aller-retour de p1 à p4
    vit_vert = drone.h_speed_max
    vit_hori = drone.v_speed_max
    distance = calcule_distance(p1,p4)
    return 2 * (drone.current_position.z / vit_vert) + 2 * (distance / vit_hori)



def decoupe_trajet(mission):
    # renvoie un tuple de 4 points et une durée
    #print('Client : ::: ', mission.client, '\nEntrepot : ', mission.entrepot, '\nDrone : ', mission.drone)
    arr, dep, drone = mission.client, mission.entrepot, mission.drone
    p1 = geo.Point(dep.x, dep.y,0)  # 0 correspond à la coordonnée en altitude que je rajoute aux coordonnées de point p1
    alt = mission.alti
    alt = tas.alt_random()
    p1 = geo.Point(dep.x, dep.y,0)  # 0 correspond à la coordonnée en altitude que je rajoute aux coordonnées de point p1
    p2 = geo.Point(dep.x, dep.y, alt)
    p3 = geo.Point(arr.x, arr.y, alt)
    p4 = geo.Point(arr.x, arr.y, 0)
    return p1, p2, p3, p4, calcul_duree_mission(drone, p1, p4)



def liste_mission(carte):
    #cumulation de attribuer mission et decoupe trajet
	l=attribuer_missions(carte)
	nb_missions=len(l)
	s=[0]*nb_missions
	for i in range(nb_missions):
		s[i]=l[i].decoupe_trajet()
	return s



def retour(mission): #drone est un objet de la classe Drone et mission un objet de la classe Mission
    client = mission.client
    entrepot = mission.entrepot
    distance = calcule_distance(client, entrepot)
    temps_arrivee = distance/(2 * mission.drone.h_speed_max + mission.drone.v_speed_max) #l'heure à laquelle le drone livre le client
    if (Timer.time - mission.heure_dmde) == mission.decoupe_trajet()[4]:
        entrepot.models[str(mission.drone.model)] += 1
    return temps_arrivee



def drone_optimal(drone, mission): #prend en parametre un objet mission de la classe Mission et un objet drone de la classe Drone7
    pass