import math

class Point():
    '''point dont les coordonées ( en mètres ) sont exprimées dans un repère (définit dans mappy)'''
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        
    def __repr__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ',' + str(self.z) + ')'
        
    
    
class Timed_Point(Point):
    def __init__(self, x, y, z, t):
        super().__init__(x, y, z)
        self.t = t
        
    def __repr__(self):
        return '(' + str(self.t) + ',' + str(self.x) + ',' + str(self.y) + ',' + str(self.z) + ')'

        
    def distance(self,other):
        return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
    


class Real_Point():
<<<<<<< HEAD
    '''point en coordonnées géographiques'''
    def __init__(self, long,lat,z):
=======
    def __init__(self, long,lat,z, t=None):
>>>>>>> 4c0d1e52bf1f4074246966b325276ae309fa46d9
        self.long = long
        self.lat = lat
        self.z = z
        self.t = t
        
    def __repr__(self):
        if self.t:
            return '(' + str(self.t) + ',' + str(self.long) + ',' + str(self.lat) + ',' + str(self.z) + ')'
        return '(' + str(self.long) + ',' + str(self.lat) + ',' + str(self.z) + ')'
        
    def __sub__(self, other):
        return Real_Point(self.lat - other.lat , self.long - other.long , self.z - other.z) #soustraction 
        
    def __add__(self , other):
        return Real_Point(self.lat + other.lat , self.long + other.long , self.z - other.z)
            

