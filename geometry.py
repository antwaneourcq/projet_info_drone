#Module permettant de créer les classes Points, Segments

class Point:
    def __init__(self,x,y):
        self.x = x  #coordonnée x en mètres 
        self.y = y  #coordonée y en mètre
        
    def __repr__(self):
        return str(self.x) + ',' + str(self.y)
        
    def __sub__(self, other):
        return Point(self.x - other.x , self.y - other.y) #soustraction 
        
    def __add__(self , other):
        return Point(self.x + other.x , self.y + other.y)
        
    #def __rmul__(self, k):
        #return Point(k * self.x, k * self.y)
    
    def __abs__(self):
        abs=((self.x ** 2) + (self.y ** 2)) ** 0.5
        return abs 
       
    def distance(self, other):
        return abs(self - other)
        


class Vecteur: #segment avec un sens 
    pass 
    
    
    
        
    