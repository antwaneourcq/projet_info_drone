import tirage_au_sort as tas
import trajet
import mappy


Missions = '~\projet_info_drone\missions.txt'

def ecriture_missions( Missions, clients):
    l_mission, file = trajet.attribuer_missions(clients)
    with open(Missions, 'w') as f:
        f.write('{:~^50}'.format('Missions'))
        for m in l_mission :
            f.write('client : ')
            cli_real = mappy.conversion_m_deg(m.client)
            f.write('longitude = {0}, latitude = {1}'.format(cli_real.long, cli_real.lat))
            f.write('entrepot : {0.entrepot}'.format(m))
            f.write('heure de la demande = {0.heure_dmde}'.format(m))
            f.write('drone utilisé : {0.drone}'.format(m))
            for p in m.trajet :
                p_real = mappy.conversion_m_deg(p)
                f.write('points du trajet : long : {0}, lat : {1}'.format(p_real.long, p_real.lat))
                

carte = (mappy.A, mappy.C)
clients,entrepots = tas.points_utiles(carte)
ecriture_missions(Missions,clients)
    

