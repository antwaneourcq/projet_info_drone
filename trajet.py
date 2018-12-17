import tirage_au_sort as tas
import lecture_drones as lect_dr
import geometry as geo
import math

ALTI_CROIS = 200 #en mètres


def ordre_priorite_drones(drones): 
	#prend en argument une liste de drones à trier selon leur vitesse maximale
	drones.sort(key = lambda drone : drone.v_speed_max, reverse = True) #on trie les drones de l'entrepot le plus proche par ordre décroissant de vitesse maximale en route (tri en place)
	return drones

def capacite_drone(entrepot, client):
    #calcule le drone le plus rapide de l'entrepot capable d'aller livrer jusqu'à chez le client
    distance = math.sqrt((client.x-entrepot.x)**2+(client.y-entrepot.y)**2)
    print(distance)
    #drones = entrepot.drones
    vit = 1
    for drone in entrepot.drones:
        dro = lect_dr.Drone(drone, geo.Point(0,0,0))
        print(dro.range)
        if dro.range >= distance:
            if dro.v_speed_max>vit:
                drone_correct = dro
                vit = dro.v_speed_max 
    try : 
        #print('CORRECT ', drone_correct)
        return drone_correct       #drone est un objet de la classe Drone du module lecture_drone
    except UnboundLocalError:
        print('AUCUN drone trouvé')
        return None


def attribuer_mission(carte):
	#renvoie une liste de tuple de la forme (client, entrepot le plus proche, drone choisi pour effectuer la mission)
	entrepots,clients=tas.points_utiles(carte)[0:1]
	nb_entrepots=len(entrepots)
	l = []
	for cli in clients: 
		distance = sqrt((cli.x-entrepots[0].x)**2+(cli.y-entrepots[0].y)**2)
		e = entrepots[0]
		ind = 0
		for i in range(nb_entrepots):
			if sqrt((cli.x-entrepots[i].x)**2+(cli.y-entrepots[i].y)**2)<distance: #calcule l'entrepot le plus proche du client cli
				distance = sqrt((cli.x-entrepots[i].x)**2+(cli.y-entrepots[i].y)**2)
				e = entrepots[i] 
				ind = i
		l.append(cli,e,capacite_drone(e,cli))
	return l 


def attribuer_mission(entrepots, clients):
    #renvoie une liste de tuple de la forme (client, entrepot le plus proche, drone choisi pour effectuer la mission)
    #entrepots,clients=tas.points_utiles(carte)    pas besoin de demander la carte travail du main
    nb_entrepots=len(entrepots)
    missions = []
    for cli in clients: 
        distance = math.sqrt((cli.x-entrepots[0].x)**2+(cli.y-entrepots[0].y)**2)
        e = entrepots[0]
        ind = 0
        for i in range(nb_entrepots):
            if math.sqrt((cli.x-entrepots[i].x)**2+(cli.y-entrepots[i].y)**2) < distance: #calcule l'entrepot le plus proche du client cli
                distance = math.sqrt((cli.x-entrepots[i].x)**2+(cli.y-entrepots[i].y)**2)
                e = entrepots[i] 
                ind = i
        drone_correct = capacite_drone(e, cli)
        if drone_correct != None:
           missions.append((cli, e, drone_correct))
        #missions.append((cli, e, capacite_drone(e, cli)))
    return missions 

	
def calcul_duree_mission(drone, p1, p4): 
	#drone est on objet de la classe Drone du module lecture_drones
	#calcul le temps que met le drone pour faire un aller-retour de p1 à p4
	vit_vert = drone.h_speed_max
	vit_hori = drone.v_speed_max
	distance = math.sqrt((p1.x-p4.x)**2 + (p1.y-p4.y)**2)
	return 2*(ALTI_CROIS/vit_vert) + 2*(distance/vit_hori)


def decoupe_trajet(mission):
    #renvoie un tuple de 4 points et une durée 
    arr, dep, drone = mission[0], mission[1], mission[2]
    p1 = geo.Point(dep.x,dep.y,0)  #0 correspond à la coordonnée en altitude que je rajoute aux coordonnées de point p1
    p2 = geo.Point(dep.x,dep.y,ALTI_CROIS)
    p3 = geo.Point(arr.x,arr.y,ALTI_CROIS)
    p4 = geo.Point(arr.x,arr.y,0)
    return p1,p2,p3,p4,calcul_duree_mission(drone, p1, p4)

	


def liste_mission(dico, carte):
	#cumulation de attribuer mission et decoupe trajet
	l=attribuer_mission(dico, carte)
	nb_missions=len(l)
	s=[0]*nb_missions
	for i in range(nb_mission):
		s[i]=decoupe_trajet(l[i])
	return s
	
	
def test():
    dico = lect_dr.read("aircraft.json")
    models = lect_dr.listmodels(dico)
    print(models)
    print(type(models[0]))
    model_prio = ordre_priorite_drones(models)
    print(model_prio)
    for model in model_prio:
        print(model, model.v_speed_max)
    entrepot0 = tas.Entrepot(0,0,0, models)
    print(entrepot0)
    entrepot0.addDrone(lect_dr.Drone('Amzn', geo.Point(entrepot0.x, entrepot0.y, entrepot0.z)))
    print(entrepot0, '\n Les drones', entrepot0.drones, '\n Amazon Drone', entrepot0.models['Amzn'])
    for drone in entrepot0.drones:
        print(drone, entrepot0.drones, type(drone))
    print('capacité drone : ',capacite_drone(entrepot0, geo.Point(20,20,20)))
    
#test()