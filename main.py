import mappy
import trajet 
import tirage_au_sort as tas
import czmlconverter as czmlc

FILE = "aircraft.json"

def heure_demande(mission) :
    return mission.heure_dmde

def heure_demande2(client) :
    return client.t


def main():
    dico = lect_dr.read(FILE)
    carte = (mappy.A, mappy.C)
    entrepots, clients = tas.points_utiles(carte)  #, carre_ext
    print(entrepots)
    print(clients)

    #mappy.affichage_carte(entrepots , clients)

    tas.drones_utiles(entrepots)
    trajet.attribuer_entrepot(clients, entrepots)
    l1 , l2 = trajet.attribuer_missions(clients)
    missions = sorted(l1 , key = heure_demande , reverse = True)
    file_attente = sorted(l2, key = heure_demande2 , reverse = True)
    for t in range (0, 86400, 1800) :
        missions_actives = trajet.missions_actives(missions,t)
        print(missions_actives)
        for m in missions :
            trajet.retour(m,t)
        l1,l2 = trajet.attribuer_missions(file_attente)
        l1 = sorted(l1, key=heure_demande, reverse=True)
        for m in l1 :
            missions.append(m)
        file_attente = sorted(l2, key=heure_demande2, reverse=True)

    '''AFFICHAGE'''
    missions, file = trajet.attribuer_missions(clients)   #entrepots, 
    print('MISSION')
#    m = missions[0]      #on a choisi la première mission de la liste missions juste pour l'affichage
#    print(missions)
#    client = mission.client
#    entrepot = mission.entrepot
#    print('coordonnées client :')
#    print(client.x, client.y)
#    print('départ mission:')
#    print(client.t)
#    print('coordonnées entrepôt :')
#    print('('+ str(entrepot.x) + ',' + str(entrepot.y) + ',' + str(entrepot.z) + ')') #parfois erreur entrepot n'est pas défini (NoneType)
#    print('modèles présents dans entrepôt :')
#    print(entrepot.models)
#    m.decoupe_trajet()
#    print('découpage spatial du trajet :')
#    print(p1,p2,p3,p4)
#    print('durée de la mission :')
#    print(str(dt)+' secondes')
#    print('Toulouse :')
#    print(mappy.A, mappy.B, mappy.C, mappy.D)
#    dep = mappy.conversion_m_deg(p2)
#    arr = mappy.conversion_m_deg(p3)
#    print('départ :')
#    print(dep)
#    print('arrivée :')
#    print(arr)
    czmlc.conversion(missions)
main()