import geometry as geo
import trajet
import Timer
import math

def a(A,B):
    return (B.y - A.y) / (B.x - A.x)

def b(A,B) :
    return A.y - a(A,B)*A.x
def point_intersection(A,B,C,D):# a l'instant t AB et CD
#faire une droite ax+b et ensuite etudier si les deux s'interceptent grace au critères de colinearité

#faire une fonction pour calculer a et b ??

    a1 = a(A,B)
    b1 = b(A,B)
    
    a2 = a(C,D)
    b2 = b(C,D)
    
    Ix = (b1 - b2)/(a1 - a2)
    Iy = Ix * a1 + b1

    I = geo.Point(Ix, Iy, 0)
    AI_x = I.x - A. x
    AI_y = I.y - A.y
    IB_x = B.x - I.x
    IB_y = B.y - I.y
    if AI_x * IB_y - AI_y * IB_x < 1e-4 :
        return I
    else :
        return None

def appartenance_segment(point , A,B):
    if a(A,B)*point.x + b(A,B) == point.y :
        if A.x < B.x :
            if A.y<B.y:
                return A.x<=point.x<=B.x and A.y<=point.y<=B.y
            return A.x<=point.x<=B.x and B.y<=point.y<=A.y
        if A.y<B.y :
            return B.x<=point.x<=A.x and A.y<=point.y<=B.y
        return B.x<=point.x<=A.x and A.y<=point.y<=B.y
    return False

def interception (A,B,C,D) :
    I = point_intersection(A,B,C,D)
    if appartenance_segment(I,A,B) and appartenance_segment(I, C,D):
        return True
    return False

def conflit(m1,m2):
    ''' si les drones arrivent au point d'intersection avec un temps de différence inférieur à 3min , on considère qu'ils sont en conflit'''
    A,B,C,D = m1.entrepot , m1.client , m2.entrepot , m2.client
    if interception(A,B,C,D):
        t1_dep, t2_dep = m1.heure_dmde, m2.heure_dmde
        v1 , v2 = m1.drone.v_speed_max , m2.drone.v_speed_max
        I = point_intersection(A, B, C, D)
        d1 , d2 = trajet.calcule_distance(A,I) , trajet.calcule_distance(B,I)
        t1_I , t2_I = t1_dep + d1/v1 , t2_dep + d2/v2
        if abs(t1_I - t2_I) <= 180 :
            print ('!!conflit!!')
            return I


def detect(missions,t):
    missions_actives = Timer.select(missions,t)
    for i, mi in enumerate(missions_actives):
        for j in range(i):
            mj = missions_actives[j]
            if conflit(mi, mj)[0]:
                I = conflit(mi,mj)[1]
                mi.changer_altitude(mi,I)

def cal_distance(p1,p2):
    '''Calcule la distance entre p1 et p2'''
    return math.sqrt((p1.x-p2.x)**2+(p1.y-p2.y)**2)

def arrivee_en_I (m1, m2):
    I = conflit(m1,m2)
    if I :
        d1 = cal_distance(m1.entrepot, I)
        d2 = cal_distance(m2.entrepot, I)
        t1 = m1.heure_dmde + d1 / m1.drone.v_speed_max
        t2 = m2.heure_dmde + d2 / m2.drone.v_speed_max
    return t1, t2



def heure_conflit(m1,m2):
    I=conflit(m1,m2)
    t1,t2 = arrivee_en_I ( m1 , m2)
    maxt , mint = max(t1,t2) , min(t1,t2)
    return mint , maxt

def test():
    client1 = geo.Timed_Point(2,2,0,0)
    m1  = trajet.Mission(client1)
    client2 = geo.Timed_Point(0,2,0,0)
    m2  = trajet.Mission(client2)
    entrepot1 , entrepot2 = geo.Point(0,0,0) , geo.Point(2,0,0)
    m1.entrepot = entrepot1
    m2.entrepot = entrepot2
    print (conflit(m1,m2))

#test()





    
    

        
    

    
        
    
    
    