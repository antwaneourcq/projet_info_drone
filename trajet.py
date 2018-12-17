import tirage_au_sort as tas
from math import sqrt
import lecture_drones as d
import geometry
import math

ALTI_CROIS = 200 #en mètres

dico = d.read("aircraft.json")
drones = d.drones_list(dico)

def ordre_priorite_drones(): 
	#prend en argument une liste de drones à trier selon leur vitesse maximale
	drones.sort(key = lambda drone : drone.h_speed_max, reverse = True) #on trie les drones de l'entrepot le plus proche par ordre décroissant de vitesse maximale en route (tri en place)
	return drones

def capacite_drone(entrepot, client):
	#calcule le drone le plus rapide de l'entrepot capable d'aller livrer jusqu'à chez le client
	distance = math.sqrt((client.x-entrepot.x)**2+(client.y-entrepot.y)**2)
	drones=entrepot.drones
	vit=1
	for dro in drones:
		if dro.range >= distance:
			if dro.v_speed_max>vit:
				drone=dro
				vit=dro.v_speed_max
	return drone       #drone est un objet de la classe Drone du module lecture_drones
	

def attribuer_mission(carte):
	#renvoie une liste de tuple de la forme (client, entrepot le plus proche, drone choisi pour effectuer la mission)
	entrepots,clients=tas.points_utiles(carte)
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
	
def calcul_duree_mission(drone,p1,p4): 
	#drone est on objet de la classe Drone du module lecture_drones
	#calcul le temps que met le drone pour faire un aller-retour de p1 à p4
	vit_vert = drone.h_speed_max
	vit_hori = drone.v_speed.max
	distance = sqrt((p1.x-p4.x)**2 + (p1.y-p4.y)**2)
	return 2*(ALTI_CROIS/vit_vert) + 2*(distance/vit_hori)


def decoupe_trajet(l):
	#renvoie un tuple de 4 points et une durée 
	p1 = geometry.Point(l[1].x,l[1].y,0)  #0 correspond à la coordonnée en altitude que je rajoute aux coordonnées de point p1
	p2 = geometry.Point(l[1].x,l[1].y,ALTI_CROIS)
	p3 = geometry.Point(l[0].x,l[0].y,ALTI_CROIS)
	p4 = geometry.Point(l[0].x,l[0].y,0)
	return p1,p2,p3,p4,calcul_duree_mission(l[i][2],p1,p4)

	


def liste_mission(dico, carte):
	#cumulation de attribuer mission et decoupe trajet
	l=attribuer_mission(dico, carte)
	nb_missions=len(l)
	s=[0]*nb_missions
	for i in range(nb_missions):
		s[i]=decoupe_trajet(l[i])
	return s


	
	

