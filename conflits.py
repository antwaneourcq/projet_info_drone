import geometry as geo

SECU = 10 #en metre
Z_ALT = 1500 

def detection1(A,B,C,D): # a l'instant t
    
    pass




def detection(d1,d2): #class Drone
    return d1.coord.distance(d2.coord) < SECU 
    
def resolution(d1,d2):
    if detection(d1,d2):
        d1.coord.z = Z_ALT + 15
        
    

    
        
    
    
    