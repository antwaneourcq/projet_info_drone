import tirage_au_sort
import drones as d

ALTI_CROIS = 200 #en mètres


def ordre_priorite_drones(dico, drones): 
	#prend en argument une liste de drones à trier selon leur vitesse maximale
	drones.sort(key = lambda drone : get_h_speeds(dico, drone)[0], reverse = True) #on trie les drones de l'entrepot le plus proche par ordre décroissant de vitesse maximale en route (tri en place)
	return drones


def attribuer_mission(carte):
	#renvoie une liste de listes [[x,y] coordonnées du client, [x,y] coordonnées de l'entrepot le plus proche du client, drone attribué à la mission, liste d'autres drones par ordre de priorité si drone attribué non dispo]
	entrepots,clients=tirage_au_sort.points_utiles(carte)
	drones=tirage_au_sort.drones_utiles()  #j'ai supposé que drones_utiles renvoie une liste de listes de listes de drones correspondants aux entrepots de la liste l_entrepots de la fonction points_utiles
	nb_entrepots=len(entrepots)
	l=[]
	for cli in clients: #j'ai supposé que clients était comme entrepots, une liste de coordonnées (x,y) des clients tirés au sort dans tirage_au_sort
		distance=sqrt((cli[0]-entrepots[0][0])**2+(cli[1]-entrepots[0][1])**2)
		e=entrepots[0]
		ind=0
		for i in range(nb_entrepots):
			if sqrt((cli[0]-entrepots[i][0])**2+(cli[1]-entrepots[i][1])**2)<distance: #calcul de l'entrepot le plus proche du client cli
				distance=sqrt((cli[0]-ent[0])**2+(cli[1]-ent[1])**2)
				e=entrepots[i] 
				ind=i
		d=ordre_priorite_drones(drones[ind]) 
		l.append([cli[0],cli[1]],[e[0],e[1]],d[0],d)
	return l 
	
def calcul_duree_mission(drone,p1,p4): 
	#calcul le temps que met le drone pour faire un aller-retour de p1 à p4
	dico=drones.drones_list(drones.read("aircraft.json"))
	vit_vert=d.get_v_speeds(dico, drone)[0]
	vit_hori=d.get_h_speeds(dico, drone)[0]
	distance=sqrt((p1[0]-p4[0])**2+(p1[1]-p4[1])**2)
	return 2*(ALTI_CROIS/vit_vert)+2*(distance/vit_hori)


def decoupe_trajet(carte):
	#renvoie une liste de tuples de 7 points et une durée dont chaque tuple correspond au trajet découpé de chaque mission de la liste renvoyée par attribuer_mission
	l=attribuer_mission(carte)
	nb_missions=len(l)
	s=[0]*nb_missions
	for i in range(nb_missions):
		p1=l[i][1]+[0]  #+[0] correspon à la cooronnée en altitude que je rajoute aux coordonnées de point p1
		p2=l[i][1]+[ALTI_CROIS]
		p3=l[i][0]+[ALTI_CROIS]
		p4=l[i][0]+[0]
		p5=p3
		p6=p2
		p7=p1
		s[i]=(p1,p2,p3,p4,p5,p6,p7,calcul_duree_mission(l[i][2],p1,p4))
	return s
	


def liste_mission(mission):
	#cumulation de attribuer mission et decoupe trajet
	

