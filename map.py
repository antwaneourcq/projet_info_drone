'''la ville de Toulouse est la map: donc les points ne peuvent pas sortir de la map'''
#on definit un carré ABCD dans lequel les points évoluent: le coin A est le point en bas à gauche"

import geometry as geo
import math

#coordonées en DD (trouvées sur internet)
A = geo.Point(43.53 , 1.35 , 1500)
B = geo.Point(43.67 , 1.35 , 1500)
C = geo.Point(43.7 , 1.52 , 1500)
D = geo.Point(43.53 , 1.52 , 1500)

int_lat = A.x -B.x  #intervalles
int_long = A.y - C.x


def conversion_m_deg(P):  #convertir des coordonées x,y en DD
    '''on passe de x en metres à x en degrés'''
    y_deg = P.y / (1852*60) #on passe x en Nm puis en ° puisqu'il est sur une ortho
    x_deg = P.x/(1852*60*math.cos(A.x))
    lat_P = round(A.x + y_deg,2) #arrondi 2 chiffres après la virgule
    long_P = round(A.y + x_deg,2) #idem
    if lat_P <= B.x and lat_P >= A.x and long_P >= A.y and long_P <= C.y:
        return geo.Point(lat_P , long_P , P.z)
    else:
        return "Le point n'est pas dans la zone"
    
    
