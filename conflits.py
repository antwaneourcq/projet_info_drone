import geometry as geo

SECU = 10 #en metre
Z_ALT = 1500 

def detection(A,B,C,D): # a l'instant t AB et CD
#faire une droite ax+b et ensuite etudier si les deux s'interceptent 

#faire une fonction pour calculer a et b
    a1 = (B.y - A.y) / (B.x - A.x)
    b1 = A.y - a1*A.x
    
    a2 = (D.y - C.y) / (D.x - C.x)
    b2 = C.y - a2*C.x
    
    Ix = (b1 - b2)/(a2 - a1)
    Iy = Ix * a1 + b1
    I = geo.Point(Ix, Iy, Z_ALT)
    
    AI_x = I.x - A. x
    AI_y = I.y - A.y
    IB_x = B.x - I.x
    IB_y = B.y - I.y
    return AI_x * IB_y - AI_y * IB_x < 1e-4 
    

    
def conflit(m1,m2):

    pass
    
    
    
    



def detection1(d1,d2): #class Drone
    return d1.coord.distance(d2.coord) < SECU 
    
def resolution(d1,d2):
    if detection(d1,d2):
        d1.coord.z = Z_ALT + 15
        
    

    
        
    
    
    