'''la ville de Toulouse est la map: donc les points ne peuvent pas sortir de la map'''
#on definit un carré ABCD dans lequel les points évoluent: le coin A est le point en bas à gauche"

import geometry as geo
import math
def basic_map():
    '''meter'''


#carte est une liste de 2 tuples, donnant le coin supérieur gauche et le coin inférieur droit

def carre_int(carte):
#je creer l'environnement,
# environnement = liste de deux intervalles représenté par des tuples et correspond à l'intervalle des abcsisses et des ordonnées
    p = 5/100
    a,b,c,d = carte[0][0], carte[0][1] , carte[1][0] , carte[1][1]
    #je defint les limites de l'espace intérieur pour les clients
    return = a+p*l_x , c-p*l_x , d+p*l_y , b-p*l_y



#coordonées en DD (trouvées sur internet)
A = geo.Point(43.53 , 1.35 , 1500)
B = geo.Point(43.67 , 1.35 , 1500)
C = geo.Point(43.7 , 1.52 , 1500)
D = geo.Point(43.53 , 1.52 , 1500)

int_lat = A.x -B.x  #intervalles
int_long = A.y - C.y


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
    
    

