import geometry as geo
import trajet
import Timer
import math

def a(A,B):
    return (B.y - A.y) / (B.x - A.x)

def b(A,B) :
    return A.y - a(A,B)*A.x
def point_intersection(A,B,C,D):# a l'instant t AB et CD
#faire une droite ax+b et ensuite etudier si les deux s'interceptent grace au critère de colinearité
    a1 = a(A,B)
    b1 = b(A,B)
    a2 = a(C,D)
    b2 = b(C,D)
    #traiter avant le cas des droites identiques i.e.    a1 == a2 and b1 == b2 (nombre de pts d'intersection infini)
    if a1 != a2:
        Ix = (b1 - b2)/(a1 - a2)
        Iy = Ix * a1 + b1
        I = geo.Point(Ix, Iy, 0)
        AI_x = I.x - A. x
        AI_y = I.y - A.y
        IB_x = B.x - I.x
        IB_y = B.y - I.y
        if AI_x * IB_y - AI_y * IB_x < 1e-4 :
            return I


def appartenance_segment(point, A,B): ###s'assurer que A, B et point sont de classe point avec attribut x, y et non long et lat
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
    if I:
        return appartenance_segment(I, A, B) and appartenance_segment(I, C, D)

def conflit(m1,m2):
    ''' si les drones arrivent au point d'intersection avec un temps de différence inférieur à 3min , on considère qu'ils sont en conflit'''
    A,B,C,D = m1.entrepot , m1.client , m2.entrepot , m2.client
    if m1.trajet and m2.trajet and m1.trajet[1].z == m2.trajet[1].z:
        if interception(A,B,C,D):
            t1_dep, t2_dep = m1.trajet[1].t, m2.trajet[1].t
            v1 , v2 = m1.drone.h_speed_max , m2.drone.h_speed_max
            I = point_intersection(A, B, C, D)
            d1 , d2 = trajet.calcule_distance(A,I) , trajet.calcule_distance(B,I)
            t1_I , t2_I = t1_dep + d1/v1 , t2_dep + d2/v2
            if abs(t1_I - t2_I) <= 3 :
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

def cal_distance(p1,p2): # la meme fonction existe dans le module trajet 
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
    
    
def liste_conflits(l_mission):
    '''donnne la liste des missions en conflits'''
    n_missions = len(l_mission)
    conflits = []
    for i in range(n_missions):
        m1 = l_mission[i]
        for j in range(i+1, n_missions):
            m2 = l_mission[j]
            pbl = conflit(m1, m2)
            if pbl:
                conflits.append((m1,m2))
    return conflits
                
                    


def thales(A,I,m, dIA):
    '''retourne les coordonnées du point entre A et I pour lequel le drone monte ou descends en utlisant le theoreme de thales et pythagore'''
    v = m.drone.h_speed_max
    xIA = abs(I.x - A.x)
    x = abs(xIA - 5*v*xIA/dIA)
    y = math.sqrt(((5*v)**2)*(1-(xIA/dIA)**2))
    return x,y


def changer_altitude(m1,m2) :
    '''Permet de changer l'altitude du drone (passe 10 mètres au dessus du palier actuel) en cas de conflits au cours de la mission ,
    le drone passera au palier au-dessus 5 secondes avant le conflits et redescendra 5 secondes après'''
    alti_sup = m1.alti[-1]+10
    m1.alti.append(alti_sup)
    p2_1, p3_1 = m1.trajet[1] , m1.trajet[2]
    I = conflit(m1,m2)
    t1,t2 = arrivee_en_I(m1,m2)
    dp2I, dp3I = cal_distance(p2_1,I) , cal_distance(p3_1, I)
    x,y= thales(p2_1, I , m1, dp2I)
    z,t = alti_sup , t1-5
    u,v = thales(p3_1, I , m1, dp3I)
    w,tt = alti_sup , t1+5
    p5 = geo.Timed_Point(x,y,z,t)
    p6 = geo.Timed_Point(u,v,w,tt)
    m1.trajet = [m1.trajet[:2], p5, p6 , m1.trajet[3:]]
    m1.duree += m1.drone.v_speed_max*2*10


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





    
    

        
    

    
        
    
    
    
