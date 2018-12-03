'''la ville de Toulouse est la map: donc les points ne peuvent pas sortir de la map'''
#on definit un carré ABCD dans lequel les points évoluent: le coin A est le point en bas à gauche"

import geometry as geo
import math


#coordonées en DD (trouvées sur internet)
A = geo.Real_Point(43.53 , 1.35 , 1500)
B = geo.Real_Point(43.67 , 1.35 , 1500)
C = geo.Real_Point(43.67 , 1.52 , 1500)
D = geo.Real_Point(43.53 , 1.52 , 1500)


def basic_map():
    '''meter'''
    if lat_P <= B.x and lat_P >= A.x and long_P >= A.y and long_P <= C.y:
        return 
    else:
        return "Le point n'est pas dans la zone"
    
    

    


#carte est une liste de 2 tuples, donnant le coin supérieur gauche et le coin inférieur droit

def carre_int(carte):
#je creer l'environnement,
# environnement = liste de deux intervalles représenté par des tuples et correspond à l'intervalle des abcsisses et des ordonnées
    p = 5/100
    l_x,l_y = C.x-A.x, C.y-A.y
    #je definis les limites de l'espace intérieur pour les clients
    return geo.Point(A.x+p*l_x , A.y+p*l_y ,1500) , geo.Point(C.x-p*l_x , C.y-p*l_ , 1500)






def conversion_m_deg(P):  #convertir des coordonées x,y en DD
    '''on passe de x en metres à x en degrés'''
    y_deg = P.y / (1852*60) #on passe x en Nm puis en ° puisqu'il est sur une ortho
    x_deg = P.x/(1852*60*math.cos(A.lat))
    lat_P = round(A.lat + y_deg,2) #arrondi 2 chiffres après la virgule
    long_P = round(A.long + x_deg,2) #idem
    return geo.Real_Point(lat_P , long_P , P.z)
    
def conversion_deg_m(P):
    y_lat = abs(P.lat - A.lat)
    x_long = abs(P.long - A.long)
    y_m = y_lat *1852 *60
    x_m = x_long *1852 *60 *math.cos(A.lat)
    return geo.Point(x_m, y_m, z)
