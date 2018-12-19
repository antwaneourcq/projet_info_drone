#Module permettant de créer les classes Points, Segments
import math
import mappy


Z_ALT = 1500


class Point():
    def __init__(self,x,y,z):
        self.x = x  #coordonnée x en mètres 
        self.y = y  #coordonée y en mètres
        self.z = z
        
    def __repr__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ',' + str(self.z) + ')'  # affichage du point à changer si jamais inutile
        
    
    
class Timed_Point(Point):
    def __init__(self, Point, t):
        super(__init__(self, x, y, z))
        self.t = t
        
    def __repr__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ',' + str(self.z) + ',' + str(self.t) + ')'
        
    def distance(self,other):
        return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
    
#print(Timed_Point(0,2,3,78))

class Real_Point():
    def __init__(self, long,lat,z):
        self.long = long
        self.lat = lat
        self.z = z
        
    def __repr__(self):
        return '(' + str(self.long) + ',' + str(self.lat) + ',' + str(self.z) + ')'
        
    def __sub__(self, other):
        return Real_Point(self.lat - other.lat , self.long - other.long , self.z - other.z) #soustraction 
        
    def __add__(self , other):
        return Real_Point(self.lat + other.lat , self.long + other.long , self.z - other.z)
            

class Line: #ligne reliant 2 points
    def __init__(self,Coords):
        self.Coords = Coords #liste contenant les coordonnées des 2 points A,B de la ligne
        
    def lenght(self):
        a = self.Coords[0][0] - self.Coords[1][0]
        b = self.Coords[0][1] - self.Coords[1][1]
        c = self.Coords[0][2] - self.Coords[1][2]
        return math.sqrt(a**2 + b**2 + c**2) #calcul de la longueur de la ligne entre A et B
        
    
        
    
import matplotlib.pyplot as plt 
P= Point(456,8964,Z_ALT)
T=Point(986,4268,Z_ALT)
PT=Line([[P.x,P.y],[T.x,T.y]])
plt.plot(P.x,P.y, '.')
plt.plot(T.x,T.y,'.')
#############"plt.plot(PT[0],PT[1])


plt.show()
            
        
    
    
    
        
    