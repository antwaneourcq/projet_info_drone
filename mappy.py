'''la ville de Toulouse est la map: donc les points ne peuvent pas sortir de la map'''
#on definit un carré ABCD dans lequel les points évoluent: le coin A est le point en bas à gauche"

import geometry as geo
import math
import matplotlib.pyplot as plt



#coordonées en degrés décimaux (trouvées sur internet)
A = geo.Real_Point(1.35, 43.53, 0)
B = geo.Real_Point(1.53, 43.67 ,0)
C = geo.Real_Point(1.52, 43.67, 0)
D = geo.Real_Point(1.52, 43.53, 0)

def verif_map(P):
    #pas d'influence du A puisque c'est le point nul
    C_map = conversion_deg_m(C)
    return P.x <= C_map.x and P.y <= C_map.y  and P.x >= 0 and P.y >= 0

#carte est une liste de 2 points, donnant le coin supérieur gauche et le coin inférieur droit A_map , C_map et définit par leur longitude et latitude

def carre_int(carte):
#je crée l'environnement des clients
#environnement = liste de deux points A_int , C_int
    p = 5/100
    '''C_map = conversion_deg_m(C)
    A_origin = geo.Point(0,0,0)
    l_x, l_y = C.x-A.x, C.y-A.y
    #je definis les limites de l'espace intérieur pour les clients
    return geo.Point(A.x+p*l_x , A.y+p*l_y ,0) , geo.Point(C_map.x-p*l_x , C_map.y-p*l_y , 0)'''
    A_map , C_map = conversion_deg_m(carte[0]) , conversion_deg_m(carte[1])
    dx, dy = p * (C_map.x - A_map.x), p * (C_map.y - A_map.y)
    return geo.Point(A_map.x + dx, A_map.y + dy, 0), geo.Point(C_map.x - dx, C_map.y - dy, 0) , A_map , C_map
    
    
    
def affichage_carte(entrepots , clients):
    '''affiche la carte des entrepots et des clients préalablement tirés au sort'''
    x_entrepots,y_entrepots , x_clients, y_clients = [], [], [], []
    for i in range(len(entrepots)):
        x_entrepots.append(entrepots[i].x)
        y_entrepots.append(entrepots[i].y)
    for i in range(len(clients)):
        x_clients.append(clients[i].x)
        y_clients.append(clients[i].y)
    plt.plot(x_entrepots, y_entrepots, '.')
    plt.plot(x_clients, y_clients, '.')
    plt.show()


def conversion_m_deg(P): 
    '''on passe de x en metres à x en degrés décimaux '''
    y_deg = P.y / (1852*60)   #on passe x en Nm puis en ° puisqu'il est sur une ortho
    x_deg = P.x/(1852*60*math.cos(A.lat))
    lat_P = round(A.lat + y_deg, 2)    #arrondi 2 chiffres après la virgule
    long_P = round(A.long + x_deg, 2) 
    try :
        return geo.Real_Point(lat_P, long_P, P.z, P.t)
    except:
        return geo.Real_Point(lat_P, long_P, P.z)
        
        
def conversion_deg_m(P):
    '''on passe de degrés décimaux à m'''
    y_lat = abs(P.lat - A.lat)
    x_long = abs(P.long - A.long)
    y_m = y_lat * 1852 * 60
    x_m = x_long * 1852 *60 * math.cos(A.lat)
    return geo.Point(x_m, y_m, P.z)
