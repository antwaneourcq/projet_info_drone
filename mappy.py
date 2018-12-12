'''la ville de Toulouse est la map: donc les points ne peuvent pas sortir de la map'''
#on definit un carré ABCD dans lequel les points évoluent: le coin A est le point en bas à gauche"

import geometry as geo
import math


#coordonées en DD (trouvées sur internet)
A = geo.Real_Point(43.53 , 1.35 , 1500)
B = geo.Real_Point(43.67 , 1.35 , 1500)
C = geo.Real_Point(43.67 , 1.52 , 1500)
D = geo.Real_Point(43.53 , 1.52 , 1500)

Z_ALT = 1500


def verif_map(P):
    #A_origin = geo.Point(0, 0, Z_ALT)    donner inutile ou alors l'utiliser pour la comparaison avec les zeros attende confirmation de suppression
    C_map = conversion_deg_m(C)
    return P.x <= C_map.x and P.y <= C_map.y and P.x >= 0 and P.y >= 0

#carte est une liste de 2 tuples, donnant le coin supérieur gauche et le coin inférieur droit

def carre_int(carte):
#je crée l'environnement,
#environnement = liste de deux intervalles représenté par des tuples et correspond à l'intervalle des abcsisses et des ordonnées
    p = 5/100
    '''C_map = conversion_deg_m(C)
    A_origin = geo.Point(0,0,Z_ALT)
    l_x, l_y = C.x-A.x, C.y-A.y
    #je definis les limites de l'espace intérieur pour les clients
    return geo.Point(A.x+p*l_x , A.y+p*l_y ,Z_ALT) , geo.Point(C_map.x-p*l_x , C_map.y-p*l_y , Z_ALT)'''
    A_map = geo.Point(0, 0, Z_ALT)
    print(carte)
    C_map = carte[1] #geo.Point(C.long, C.lat, C.z)
    #print('hi sir', conversion_deg_m(C))
    dx, dy = p * (C_map.x - A_map.x), p * (C_map.y - A_map.y)
    return geo.Point(A_map.x + dx, A_map.y + dy, Z_ALT), geo.Point(C_map.x - dx, C_map.y - dy, Z_ALT)

def conversion_m_deg(P):  #convertir des coordonées x,y en DD
    '''on passe de x en metres à x en degrés'''
    y_deg = P.y / (1852*60) #on passe x en Nm puis en ° puisqu'il est sur une ortho
    x_deg = P.x/(1852*60*math.cos(A.lat))
    lat_P = round(A.lat + y_deg, 2) #arrondi 2 chiffres après la virgule
    long_P = round(A.long + x_deg, 2) #idem
    return geo.Real_Point(lat_P, long_P, P.z)
    
    
def conversion_deg_m(P):
    y_lat = abs(P.lat - A.lat)
    x_long = abs(P.long - A.long)
    y_m = y_lat * 1852 * 60
    x_m = x_long * 1852 *60 * math.cos(A.lat)
    return geo.Point(x_m, y_m, P.z)