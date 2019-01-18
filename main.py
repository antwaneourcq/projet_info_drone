import mappy
import trajet 
import tirage_au_sort as tas
import czmlconverter as czmlc
import affichage
import conflits
FILE = "aircraft.json"
Missions = 'missions.txt'

def heure_demande(mission):
    return mission.heure_dmde

def heure_demande2(client):
    return client.t

def tri(liste , f):
    return sorted(liste,key=f)




def main():
    carte = (mappy.A, mappy.C)
    entrepots, clients = tas.points_utiles(carte)  #, carre_ext
    print(entrepots)
    print(clients)
    tas.drones_utiles(entrepots)
    trajet.attribuer_entrepot(clients, entrepots)
    id_mission = 0
    l1 , l2 = trajet.attribuer_missions(clients, id_mission)
    missions = tri(l1, heure_demande)
    file_attente = tri(l2 , heure_demande2)
    mission_vide = 0
    mission_traite = 0
    for t in range (0, 86400, 1800):
        '''a chaque pas de temps: actualisation des missions actives + ajout des drones revenus dans l'entrepot qui seront a nouveau disponibles + attribution de missions aux clients qui netait pas servis '''
        missions_actives = trajet.missions_actives(missions,t)
        print(missions_actives)
        for m in missions:
            if m.trajet != []:
                trajet.retour(m,t)
                mission_traite += 1
            else:
                mission_vide += 1
        l1,l2 = trajet.attribuer_missions(file_attente, id_mission)
        missions_ajoutees, file_attente = tri(l1 , heure_demande), tri(l2, heure_demande2)
        for m in missions_ajoutees:
            missions.append(m)

    #missions.sort(key = lambda m: m.trajet[0].t)
    '''AFFICHAGE'''
    #missions, file = trajet.attribuer_missions(clients)   #entrepots, cça ne sert à rien à part détruire le travail précédent...
    print('MISSION')
    print('mission vide :', mission_vide, 'mission traitées :', mission_traite)
    l_conflits = conflits.liste_conflits(missions)
    for m1,m2 in l_conflits :
        conflits.changer_altitude(m1,m2)

    czmlc.writeczml(missions)
    affichage.ecriture_missions(Missions, missions, l_conflits)

    import xmlconverter
    l_conflits = conflits.liste_conflits(missions)

    xmlconverter.ecriture_mission(xmlconverter.Livraison_par_drones, missions, l_conflits,"Missions.xml" )
   


main()

def test():
    import geometry as geo
    x1,x2,x3,x4=0,0,1000,1000
    y1,y2,y3,y4=0,1000,0,1000
    client1 = trajet.Client(x4,y4,0,0)
    m1  = trajet.Mission(client1, 0)
    client2 = trajet.Client(x3,y3,0,0)
    m2  = trajet.Mission(client2, 1)
    entrepot1 , entrepot2 = geo.Point(x1,y1,0) , geo.Point(x2,y2,0)
    client1.entrepot = entrepot1
    client2.entrepot = entrepot2
    m1.entrepot = entrepot1
    m2.entrepot = entrepot2
    m1.alti = [300]
    m2.alti = [300]
    m1.trajet = [geo.Timed_Point(x1,y1,0,0),geo.Timed_Point(x1,y1,300,20), geo.Timed_Point(x4,y4,300,60), geo.Timed_Point(x4,y4,0,80)]
    m2.trajet = [geo.Timed_Point(x2,y2,0,0),geo.Timed_Point(x2,y2,300,20), geo.Timed_Point(x3,y3,300,60), geo.Timed_Point(x3,y3,0,80)]
    print('m2', m2.trajet)
    print('m1', m1.trajet)
    I, t1, t2 = conflits.conflit(m1,m2)
    print('conflit : ',I, t1, t2)
    print('m2', m2.trajet)
    print('m1', m1.trajet)
    mappy.conversion_mission(m1)
    mappy.conversion_mission(m2)
    print('trajet')
    print(m1.trajet)
    print(m2.trajet)
#test()


