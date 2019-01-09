
import random
import lecture_drones as lect_dr
import geometry as geo
import math
import mappy 
import tirage_au_sort as tas

ALTI_CROIS = 200  # en mètres


class Mission:

    def __init__(self, client):
        self.client = client
        self.entrepot = None
        self.heure_dmde = client.t
        self.drone = None
        self.deviation = []
        
    def __repr__(self):
        return 'mission :  entrepot : ' + str(self.entrepot) +'\n' #+ ', client : ' + str(self.client) + ', temps : ' + str(self.heure_dmde) + ', drone : ' + str(self.drone)

    def changer_altitude(self):
        

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
            dro = lect_dr.Drone(drone, geo.Point(0, 0, 0))
            if dro.range >= distance:
                if dro.v_speed_max > vit:
                    drone_correct = dro
                    vit = dro.v_speed_max
    try:
        return drone_correct  # drone est un objet de la classe Drone du module lecture_drone
    except UnboundLocalError:
        return None


def attribuer_missions(carte):
    drone_correct = None
    for drone in entrepot.models: #models
        #if entrepot.models[drone] : print('entréeeee   ', entrepot.models[drone], drone)
        if entrepot.models[drone]>0: #s'il y a au moins un exemplaire de ce drone dans l'entrepot
            dro = lect_dr.Drone(drone, geo.Point(0, 0, 0))
            if dro.range >= distance:
                if dro.v_speed_max > vit:
                    drone_correct = dro
                    vit = dro.v_speed_max
    if drone_correct: entrepot.remove_drone(drone_correct)
    #if drone_correct == None:
    #    print('\néchec\t', entrepot)
    return drone_correct    
#    try:
#        return drone_correct  # drone est un objet de la classe Drone du module lecture_drone
#    except UnboundLocalError:
#        return None

def attribuer_missions(entrepots , clients):

    '''renvoie une liste de missions , determinées en fonction des clients et entrepots tirés au sort'''
    l_entrepots , l_clients = entrepots, clients
    missions = []
    nb_entrepots = len(l_entrepots)
    correctness = 0
    drones_non_traites = 0
    drone_correct = None
    for cli in l_clients:
        m = Mission(cli)
        e = l_entrepots[0]
        distance = calcule_distance(cli,e)
        for i in range(nb_entrepots):
            if calcule_distance(cli,l_entrepots[i]) < distance: #calcule l'entrepot le plus proche du client cli
                distance = calcule_distance(cli,l_entrepots[i])
                e = l_entrepots[i]
            drone_correct = capacite_drone(e, cli)
        if drone_correct != None:
            correctness += 1 
            m.entrepot = e
            m.heure_livr =random.randint(0,24)
            m.drone = drone_correct
            m.heure_livr =random.randint(0,24) #à modifier avec ordre/file à priorité
            m.drone = drone_correct
            e.models[str(drone_correct.model)]-=1
        else :
            #traiter le cas où le drone est None
            drones_non_traites += 1
            pass
        missions.append(m)
        # print('MISSSIONSSSS : ', missions, '\n\nla mission : ', m)
    print('\ndrone correct', correctness, 'drones non traités ', drones_non_traites)
    return missions





def calcul_duree_mission(drone, p1, p4):
    # drone est on objet de la classe Drone du module lecture_drones
    # calcul le temps que met le drone pour faire un aller-retour de p1 à p4
    vit_vert = drone.h_speed_max
    vit_hori = drone.v_speed_max
    distance = calcule_distance(p1,p4)
    return 2 * (ALTI_CROIS / vit_vert) + 2 * (distance / vit_hori)


def decoupe_trajet(mission):
    # renvoie un tuple de 4 points et une durée
    #print('Client : ::: ', mission.client, '\nEntrepot : ', mission.entrepot, '\nDrone : ', mission.drone)
    arr, dep, drone = mission.client, mission.entrepot, mission.drone
    p1 = geo.Point(dep.x, dep.y,0)  # 0 correspond à la coordonnée en altitude que je rajoute aux coordonnées de point p1
    p2 = geo.Point(dep.x, dep.y, ALTI_CROIS)
    p3 = geo.Point(arr.x, arr.y, ALTI_CROIS)
    p4 = geo.Point(arr.x, arr.y, 0)
    return p1, p2, p3, p4, calcul_duree_mission(drone, p1, p4)


def liste_mission(carte):
    #cumulation de attribuer mission et decoupe trajet
	l=attribuer_missions(carte)
	nb_missions=len(l)
	s=[0]*nb_missions
	for i in range(nb_missions):
		s[i]=decoupe_trajet(l[i])
	return s



def retour(drone, mission): #drone est un objet de la classe Drone et mission un objet de la classe Mission
    client = mission.client
    entrepot = mission.entrepot
    distance = calcule_distance(client, entrepot)
    temps_arrivee = distance/(2 * drone.h_speed_max + drone.v_speed_max) #l'heure à laquelle le drone livre le client
    if (time - mission.heure_dmde) == decoupe_trajet(mission)[4]:
        entrepot.models[str(drone.model)] += 1
    return temps_arrivee



def drone_optimal(mission,drone): #prend en parametre un objet mission de la classe Mission et un objet drone de la classe Drone
    pass


