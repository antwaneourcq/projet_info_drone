import mappy
import trajet 
import tirage_au_sort as tas
import czmlconverter as czmlc
import lecture_drones as lect_dr
FILE = "aircraft.json"

def heure_demande(mission) :
    return mission.heure_dmde

def heure_demande2(client) :
    return client.t

def tri_missions(liste):
    return sorted(liste,key=heure_demande)

def tri_file_attente(liste):
    return sorted(liste,key=heure_demande2)


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
    missions = tri_missions(l1)
    file_attente = tri_file_attente(l2)
    for t in range (0, 86400, 1800) :
        '''a chaque pas de temps: actualisation des missions actives + ajout des drones revenus dans l'entrepot qui seront a nouveau disponibles + attribution de missions aux clients qui netait pas servis '''
        missions_actives = trajet.missions_actives(missions,t)
        print(missions_actives)
        for m in missions :
            trajet.retour(m,t)
        l1,l2 = trajet.attribuer_missions(file_attente)
        missions_ajoutees, file_attente = tri_missions(l1), tri_file_attente(l2)
        for m in missions_ajoutees :
            missions.append(m)


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