import geometrie as geo
import trajet
import Timer
import math

TCRI = 10 #temps critique de détection de conflit
def a(A,B):
    if A.x == B.x:
        return 0
    return (B.y - A.y) / (B.x - A.x)

def b(A,B) :
    return A.y - a(A,B)*A.x

def point_intersection(A,B,C,D):# a l'instant t AB et CD
#faire une droite ax+b et ensuite etudier si les deux s'interceptent grace au critère de colinearité
    a1 = a(A,B)
    b1 = b(A,B)
    a2 = a(C,D)
    b2 = b(C,D)
    print('1 :', a1 ,'x + ', b1 ,'2 :  ',a2, 'x + ',b2)
    #traiter avant le cas des droites identiques i.e.    a1 == a2 and b1 == b2 (nombre de pts d'intersection infini)
    if a1 != a2:
        Ix = (b1 - b2)/(a2 - a1)
        Iy = Ix * a1 + b1
        I = geo.Point(Ix, Iy, 0)
        return I
    else :
        print('droite parallèle')

def cal_distance(p1,p2): # la meme fonction existe dans le module trajet
    '''Calcule la distance entre p1 et p2'''
    return math.sqrt((p1.x-p2.x)**2+(p1.y-p2.y)**2)

def appartenance_segment(point, A,B): ###s'assurer que A, B et point sont de classe point avec attribut x, y et non long et lat
    if a(A,B)*point.x + b(A,B) == point.y :
        if A.x < B.x :
            if A.y<B.y:
                return A.x<=point.x<=B.x and A.y<=point.y<=B.y
            return A.x<=point.x<=B.x and B.y<=point.y<=A.y
        if A.y<B.y :
            return B.x<=point.x<=A.x and A.y<=point.y<=B.y
        return B.x<=point.x<=A.x and B.y<=point.y<=A.y
    return False

def interception (A,B,C,D, I) :
    #I = point_intersection(A,B,C,D)
    if I:
        return appartenance_segment(I, A, B) and appartenance_segment(I, C, D)

def conflit(m1,m2):
    ''' si les drones arrivent au point d'intersection avec un temps de différence inférieur à 3min , on considère qu'ils sont en conflit'''
    A,B,C,D = m1.entrepot , m1.client , m2.entrepot , m2.client
    if m1.trajet == [] or m2.trajet == []:
        print('mission vide')
    elif m1.trajet != [] and m2.trajet !=[] and m1.trajet[1].z == m2.trajet[1].z:
        I = point_intersection(A, B, C, D)
        if interception(A,B,C,D, I):
            I = point_intersection(A, B, C, D)
            t1, t2, t3, t4 = arrivee_en_I(m1, m2, I)
            if abs(t1-t2) <= TCRI : #sur les 2 allers
                changer_altitude(m1, m2, I, t1, t2, True, True)
                return I, t1,t2
            if abs(t3-t4)<TCRI: #sur les 2 retours
                changer_altitude(m1, m2, I, t3, t4, False, False)
                return I, t3,t4
            if abs(t3-t2)<TCRI: #sur retour m1 aller m2
                changer_altitude(m1, m2, I, t3, t2, False, True)
                return I, t3,t4
            if abs(t1-t4)<TCRI: #sur aller m1 retour m2
                changer_altitude(m1, m2, I, t1, t4, True, False)
                return I, t3,t4
    else:
        print("aucun conflit", m1.trajet, m2.trajet, test)

def arrivee_en_I (m1, m2, I):
    #I = conflit(m1,m2)
    if I :
        d1 = cal_distance(m1.entrepot, I)
        d2 = cal_distance(m2.entrepot, I)
        #aller
        t1 = m1.trajet[1].t + d1/m1.drone.v_speed_max #d1/20 pour les tests sans drone
        t2 = m2.trajet[1].t + d2/m2.drone.v_speed_max
        #retour
        t3 = m1.trajet[-2].t - d1/m1.drone.v_speed_max
        t4 = m2.trajet[-2].t - d1/m1.drone.v_speed_max
    return t1, t2, t3, t4

def changer_altitude(m1,m2, I, t1, t2, aller1, aller2) :
    '''Permet de changer l'altitude du drone (passe 10 mètres au dessus du palier actuel) en cas de conflits au cours de la mission ,
    le drone passera au palier au-dessus 5 secondes avant le conflits et redescendra 5 secondes après'''
    if aller1:
        i=1
        j=2
    elif aller2:
        i,j = changer_altitude(m2, m1, I, t2, t1, aller2, aller1)
    else:
        i=-3
        j=-2
    alti_sup = m1.alti[0] + 10
    m1.alti.append(alti_sup)
    p2_1, p3_1 = m1.trajet[i], m1.trajet[j]
    #dp2I, dp3I = cal_distance(p2_1, I), cal_distance(p3_1, I)
    try :
        t = m1.trajet[i].t
        x, y = abs ((I.x - p2_1.x)/2), abs((I.y - p2_1.y)/2)
        z = alti_sup
        t += cal_distance(I,geo.Point(x,y,z))/m1.drone.h_speed_max
        u, v = abs ((I.x - p3_1.x)/2), abs((I.y - p3_1.y)/2)
        w = alti_sup
        tt = cal_distance(I,geo.Point(u,v,w))/m1.drone.h_speed_max
        z_bas = m1.trajet[i].z
        p4 = geo.Timed_Point(x, y, t)
        t_montee = (z-z_bas)/m1.drone.v_speed_max
        t += t_montee
        p5 = geo.Timed_Point(x, y, z, t)
        t += cal_distance(I, geo.Point(u, v, w)) / m1.drone.h_speed_max
        p6 = geo.Timed_Point(u, v, w, t)
        p7 = geo.Timed_Point(u, v, w, t+t_montee)
        m1.trajet = m1.trajet[:j]+ [p4, p5, p6, p7] + m1.trajet[j:]
        m1.duree += 2*10 / m1.drone.v_speed_max
        for k in range(j, len(m1.trajet)):
            m1.trajet[k].t += m1.duree
    except:
        raise Exception
    finally : return i,j

def thales(A,I,m, dIA):
    '''retourne les coordonnées du point entre A et I pour lequel le drone monte ou descends en utlisant le theoreme de thales et pythagore'''
    v = 10 #modif m.drone.h_speed_max
    xIA = abs(I.x - A.x)
    if I.x != A.x:
        x = abs(xIA - 5*v*xIA/dIA)
        y = math.sqrt(((5*v)**2)*(1-(xIA/dIA)**2))
        return x,y
    
###fonction inutile
def heure_conflit(m1, m2):
    I = conflit(m1, m2)
    t1, t2, t3, t4 = arrivee_en_I(m1, m2)
    maxt_all, mint_all = max(t1, t2), min(t1, t2)
    maxt_re, mint_re = max(t3, t4), min(t3, t4)
    return mint_all, maxt_all, maxt_re, mint_re

def liste_conflits(l_mission):#ancienne version fonctionelle
    '''donne la liste des missions en conflits'''
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
