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

    #l_conflits = []
    l_conflits = conflits.liste_conflits(missions)
    czmlc.writeczml(missions)
    affichage.ecriture_missions(Missions, missions, l_conflits, mission_vide, mission_traite)
main()
