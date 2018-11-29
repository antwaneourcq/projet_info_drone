import geometry

from random import uniform, randint

#carte est une liste de 2 tuples, donnant le coin supérieur gauche et le coin inférieur droit

def carre_int(carte):
#je creer l'environnement,
# environnement = liste de deux intervalles représenté par des tuples et correspond à l'intervalle des abcsisses et des ordonnées
    p = 5/100
    a,b,c,d = carte[0][0], carte[0][1] , carte[1][0] , carte[1][1]
    #je defint les limites de l'espace intérieur pour les clients
    return = a + p * l_x , c - p  * l_x , d + p*l_y , b - p*l_y




def points_utiles(carte):
    #renvoie la liste des entrepots et des clients
    #uniform genere un nombre réel aléatoire dans l'intervalle donné
    # 50 correspond au nombre maximum de clients ou d'entrepots , choisi arbitrairement
    nbr_entrepots = uniform((5,50))
    nbr_clients = uniform((0,50))
    l_entrepots = []
    l_clients =[]
    x0,x1,y0,y1 = carre_int(carte)
    a, b, c, d = carte[0][0], carte[0][1], carte[1][0], carte[1][1]
    # je decoupe le contour en quatre espace , 1=espace superieur , 2= espace droit , 3= espace inferieur , 4= espace gauche
    # carre_ext renvoie la list de l'intervalle des abcisse et de l'intervalle des ordonnées pour chaque espace 1,2,3,4
    carre_ext = [[(x0, c), (y1, b)], [(x1, c), (d, y1)], [(a, x1), (c, y0)], [(a, x0), (y0, b)]]
    for _ in range(nbr_entrepots) :
        #p est assimilé à l'un de ces espaces aléatoireent
        p= randint(1,4)
        l_entrepots.append(uniform(carrre_ext[p][0]), uniform(carre_est[p][1]))

    for _ in range(nbr_clients):
        l_clients.append((uniform(lim_x,lim_y)))
    return l_entrepots,l_clients


def drones_utiles()













