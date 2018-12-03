import geometry

import drones
import map

from random import uniform, randint, choice


NMAX_CL = 50 #nombre maximal de clients autorisés
NMAX_EN = 50 #nombre maximal d'entrepôts autorisés
#carte est une liste de 2 tuples, donnant le coin supérieur gauche et le coin inférieur droit





def points_utiles(carte):
    '''renvoie la liste des entrepots et des clients
    uniform genere un nombre réel aléatoire dans l'intervalle donné
    50 correspond au nombre maximum de clients ou d'entrepots , choisi arbitrairement
    uniform génère un nombre réel aléatoire dans l'intervalle donné

    je decoupe le contour en quatre espace , 1=espace superieur , 2= espace droit , 3= espace inferieur , 4= espace gauche

    carre_ext renvoie la list de l'intervalle des abcisse et de l'intervalle des ordonnées pour chaque espace 1,2,3,4

    p est assimilé à l'un de ces espaces alétoirement'''
    nbr_entrepots = uniform((5, NMAX_EN))
    nbr_clients = uniform((0, NMAX_CL))

    l_entrepots = []
    l_clients =[]
    x0,x1,y0,y1 = map.carre_int(carte)
    a, b, c, d = carte[0][0], carte[0][1], carte[1][0], carte[1][1]

    carre_ext = [[(x0, c), (y1, b)], [(x1, c), (d, y1)], [(a, x1), (c, y0)], [(a, x0), (y0, b)]]
    for _ in range(nbr_entrepots) :

        p = randint(1, 4)
        x,y,z = uniform(carre_ext[p][0]),uniform(carre_ext[p][1]),0
        Point = geometry.Point()
        l_entrepots.append(Point)

    for _ in range(nbr_clients):
        x,y,z = uniform(x0,x1) , uniform(y0,y1) , 0
        Point
        l_client.append(Point)

    return l_entrepots,l_clients


def drones_utiles(dictionnary0,carte):
    '''renvoie un dictionnaire assimilaant entre 1 et 10 drones à un entrepot'''
    l_entrepots = points_utiles(carte)[0]

    for entrepots in points_utiles(carte)[0]:
        drones=[]
        p=randint(1,10)
        for i in range (p) :
            drones.append(random.choice(drones.drones_list(dictionnary0)))
        dico[entrepots] = drones

    return dico












