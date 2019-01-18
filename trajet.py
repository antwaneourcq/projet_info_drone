import random
import lecture_drones as ldr
import geometrie as geo
import tirage_au_sort as tas
import conflits
import math


class Mission:

    def __init__(self, client, id): #client est un objet de la classe Client
        self.client = client
        self.entrepot = client.entrepot
        self.heure_dmde = client.t
        self.drone = None
        self.alti = [tas.alt_random()]
        self.trajet = []
        self.duree = 0
        self.id = id
        
    def __repr__(self):
        return 'mission : '+ str(self.id) + ' (entrepot : ' + str(self.entrepot) +')'
        #+ ', client : ' + str(self.client) + ', temps : ' + str(self.heure_dmde) + ', drone : ' + str(self.drone)


    def decoupe_trajet(self):
        '''Découpe la trajectoire de la mission en 7 points timés stockés dans l'attribut trajet'''
        # print('Client : ::: ', mission.client, '\nEntrepot : ', mission.entrepot, '\nDrone : ', mission.drone)
        arr, dep, drone = self.client, self.entrepot, self.drone
        alt = tas.alt_random()
        distance = calcule_distance(self.client)
        t_courant = self.heure_dmde
        t_largage = 10 #temps où le drone reste posé pour larguer le colis
        temps_montee = round(alt/self.drone.v_speed_max)
        p1 = geo.Timed_Point(dep.x, dep.y, 0, t_courant)  # 0 correspond à la coordonnée en altitude
        t_courant += temps_montee
        p2 = geo.Timed_Point(dep.x, dep.y, alt, t_courant)
        temps_palier = round(distance/self.drone.h_speed_max)
        t_courant += temps_palier
        p3 = geo.Timed_Point(arr.x, arr.y, alt, t_courant)
        t_courant += temps_montee
        p4 = geo.Timed_Point(arr.x, arr.y, 0, t_courant)
        self.trajet = [p1, p2 , p3 , p4]
        t_courant += t_largage
        self.trajet.append(geo.Timed_Point(arr.x, arr.y, 0, t_courant))
        t_courant += temps_montee
        p5 = geo.Timed_Point(p3.x, p3.y, p3.z, t_courant)
        t_courant += temps_palier
        p6 = geo.Timed_Point(p2.x, p2.y, p2.z, t_courant)
        t_courant += temps_montee
        p7 = geo.Timed_Point(p1.x, p1.y, p1.z, t_courant)
        self.trajet += [p5, p6, p7]
        self.duree = self.calcul_duree_mission()



    def calcul_duree_mission(self):
        '''Calcule le temps que met le drone affilié pour effectuer entièrement la mission'''
        dep = self.trajet[0].t
        drone = self.drone
        distance = calcule_distance(self.client)
        arr = distance / drone.h_speed_max + 2 * self.alti[0] / drone.v_speed_max
        return arr - dep


class Entrepot(geo.Point):

    def __init__(self, x, y, z, models, id):  # models: dico de modèle de drones
        super().__init__(x, y, z)
        self.models = {}
        for mod in models:
            self.models[str(mod)] = 1
        self.id = id

    def __repr__(self):
        return str(self.id) 
        #+ '(' + str(self.x) + ',' + str(self.y) + ',' + str(self.z) + ')' + ' drones : ' + str(self.models)

    def add_drone(self, drone):
        self.models[str(drone.model)] += 1

    def remove_drone(self, drone):
        if self.models[str(drone)] > 0: self.models[str(drone)] -= 1



class Client(geo.Timed_Point):

    def __init__(self, x, y, z, t):
        super().__init__(x, y, z, t)
        self.entrepot = None

    def __repr__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ',' + str(self.z) + ', entrepôt du client : ' + str(self.entrepot) + ')'



def attribuer_entrepot(clients, entrepots):
    '''entrepots est une liste d'entrepôts: attirbue un entrepot à un client'''
    l = len(entrepots)
    for cli in clients:
        if cli.entrepot == None:
            p = random.randint(0, l-1)
            cli.entrepot = entrepots[p]


def ordre_priorite_drones(drones): 
    '''Prend en argument une liste de drones à trier selon leur vitesse maximale'''
    drones.sort(key = lambda drone : drone.h_speed_max, reverse = True) #on trie les drones de l'entrepot le plus proche par ordre décroissant de vitesse maximale en route (tri en place)
    return drones


def calcule_distance(client):
    '''Calcule la distance entre un client et un entrepôt'''
    return math.sqrt((client.x-client.entrepot.x)**2+(client.y-client.entrepot.y)**2)


def capacite_drone(client):
    '''Calcule le drone le plus rapide de l'entrepot capable d'aller livrer le colis jusqu'à chez le client'''
    distance = calcule_distance(client)
    entrepot = client.entrepot
    vit = 1
    drone_correct = None
    for drone in entrepot.models:
        if entrepot.models[drone]>0:
            dro = ldr.Drone(drone, geo.Point(entrepot.x, entrepot.y, entrepot.z))
            if dro.range*1000 >= distance:
                if dro.v_speed_max > vit:
                    drone_correct = dro
                    vit = dro.h_speed_max
    return drone_correct  # drone est un objet de la classe Drone du module lecture_drone
# supprimer le try except

def attribuer_missions(clients, id_mission): #clients est une liste d'objets de la classe Client
    '''renvoie une liste de missions , determinées en fonction des clients et entrepots tirés au sort'''
    file_attente = []
    missions = []
    correctness = 0
    drones_non_traites = 0
    for cli in clients:
        e = cli.entrepot
        drone = capacite_drone(cli)
        m = Mission(cli, id_mission)
        id_mission += 1
        if drone != None:
            correctness += 1 
            m.entrepot = e
            m.drone = drone
            e.models[str(drone.model)] -= 1
            m.decoupe_trajet()

        else :
            #traite le cas où le drone == None
            drones_non_traites += 1
            file_attente.append(cli)
        missions.append(m)
        # print('MISSSIONSSSS : ', missions, '\n\nla mission : ', m)
    return missions, file_attente
    #print('\ndrone correct', correctness, 'drones non traités ', drones_non_traites)


def missions_actives(missions,t):
    '''liste des missions en action à l'instant t'''
    missions_actives = []
    for m in missions:
        if m.heure_dmde + m.duree >= t >= m.heure_dmde :
            missions_actives.append(m)
    return(missions_actives)


def retour(mission, t): #drone est un objet de la classe Drone et mission un objet de la classe Mission
    '''lorsque le drone a fini sa mission il revient dans l'entrepot et peut repartir pour une prochaine mission'''
    print('retour: ', mission)
    print('trajet :', mission.trajet)
    print('\ndernier point', mission.trajet[-1], 'temps : ', mission.trajet[-1].t)
    if t > mission.trajet[-1].t:
        mission.entrepot.models[str(mission.drone.model)] += 1

    else:
        pass

