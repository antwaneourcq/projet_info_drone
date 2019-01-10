
import lecture_drones as lect_dr
import mappy
import trajet 
import tirage_au_sort as tas
import matplotlib.pyplot as plt
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
    x_entrepots,y_entrepots , x_clients, y_clients =[],[] , [],[]
    for i in range(len(entrepots)):
        x_entrepots.append(entrepots[i].x)
        y_entrepots.append(entrepots[i].y)
    for i in range(len(clients)):
        x_clients.append(clients[i].x)
        y_clients.append(clients[i].y)
    plt.plot(x_entrepots,y_entrepots, '.')
    plt.plot(x_clients,y_clients, '.')
    plt.show()
    tas.drones_utiles(dico, entrepots)
    trajet.attribuer_entrepot(entrepots , clients)
    missions , file_attente = trajet.attribuer_missions(clients)
    sorted(missions , key = heure_demande , reverse = True)
    sorted(file_attente, key = heure_demande2 , reverse = True)
    for t in range (0, 86400, 1800) :
        missions_actives = []
        for m in missions :
            if heure_demande(m)+ m.decoupe_trajet()[4] <= t :
                missions_actives.append(m)
            print(m)





    '''AFFICHAGE'''
    missions = trajet.attribuer_missions(clients)   #entrepots, 
    print('MISSION')
    mission = missions[0]      #on a choisi la première mission de la liste missions juste pour l'affichage
    print(missions)
    client = mission.client
    entrepot = mission.entrepot
#    print('coordonnées client :')
#    print(client.x, client.y)
#    print('départ mission:')
#    print(client.t)
#    print('coordonnées entrepôt :')
#    print('('+ str(entrepot.x) + ',' + str(entrepot.y) + ',' + str(entrepot.z) + ')') #parfois erreur entrepot n'est pas défini (NoneType)
#    print('modèles présents dans entrepôt :')
#    print(entrepot.models)
    p1, p2, p3, p4, dt = trajet.decoupe_trajet(mission)
#    print('découpage spatial du trajet :')
#    print(p1,p2,p3,p4)
#    print('durée de la mission :')
#    print(str(dt)+' secondes')
#    print('Toulouse :')
#    print(mappy.A, mappy.B, mappy.C, mappy.D)
    dep = mappy.conversion_m_deg(p2)
    arr = mappy.conversion_m_deg(p3)
#    print('départ :')
#    print(dep)
#    print('arrivée :')
#    print(arr)
    czmlc.conversion(missions)
main()