import tirage_au_sort
import lecture_drones as d
import geometry

ALTI_CROIS = 200 #en mètres


def ordre_priorite_drones(dico, drones): 
	#prend en argument une liste de drones à trier selon leur vitesse maximale
	drones.sort(key = lambda drone : get_h_speeds(dico, drone)[0], reverse = True) #on trie les drones de l'entrepot le plus proche par ordre décroissant de vitesse maximale en route (tri en place)
	return drones



def attribuer_mission(dico, carte):
	#renvoie une liste de listes [[x,y] coordonnées du client, [x,y] coordonnées de l'entrepot le plus proche du client, drone attribué à la mission, liste d'autres drones par ordre de priorité si drone attribué non dispo]
	entrepots,clients=tirage_au_sort.points_utiles(carte)
	drones=tirage_au_sort.drones_utiles(dico,carte)  #j'ai supposé que drones_utiles renvoie une liste de listes de listes de drones correspondants aux entrepots de la liste l_entrepots de la fonction points_utiles
	nb_entrepots=len(entrepots)
	l=[]
	for cli in clients: #j'ai supposé que clients était comme entrepots, une liste de coordonnées (x,y) des clients tirés au sort dans tirage_au_sort
		distance=sqrt((cli.x-entrepots[0].x)**2+(cli.y-entrepots[0].y)**2)
		e=entrepots[0]
		ind=0
		for i in range(nb_entrepots):
			if sqrt((cli.x-entrepots[i].x)**2+(cli.y-entrepots[i].y)**2)<distance: #calcul de l'entrepot le plus proche du client cli
				distance=sqrt((cli[0]-ent[0])**2+(cli[1]-ent[1])**2)
				e=entrepots[i] 
				ind=i
		drone_ord=ordre_priorite_drones(drones[ind][1]) 
		l.append(cli,e,drone_ord[0],drone_ord)
	return l 
	
def calcul_duree_mission(drone,p1,p4): 
	#calcul le temps que met le drone pour faire un aller-retour de p1 à p4
	dico=drones.drones_list(drones.read("aircraft.json"))
	vit_vert=d.get_v_speeds(dico, drone)[0]
	vit_hori=d.get_h_speeds(dico, drone)[0]
	distance=sqrt((p1.x-p4.x)**2+(p1.y-p4.y)**2)
	return 2*(ALTI_CROIS/vit_vert)+2*(distance/vit_hori)


def decoupe_trajet(l):
	#renvoie un tuple de 7 points et une durée 
	p1=geometry.Point(l[1].x,l[1].y,0)  #0 correspond à la coordonnée en altitude que je rajoute aux coordonnées de point p1
	p2=geometry.Point(l[1].x,l[1].y,ALTI_CROIS)
	p3=geometry.Point(l[0].x,l[1].y,ALTI_CROIS)
	p4=geometry.Point(l[0].x,l[1].y,0)
	p5=p3
	p6=p2
	p7=p1
	return p1,p2,p3,p4,p5,p6,p7,calcul_duree_mission(l[i][2],p1,p4)

	


def liste_mission(dico, carte):
	#cumulation de attribuer mission et decoupe trajet
	l=attribuer_mission(dico, carte)
	nb_missions=len(l)
	s=[0]*nb_missions
	for i in range(nb_mission):
		s[i]=decoupe_trajet(l[i])
	return s


	
	

