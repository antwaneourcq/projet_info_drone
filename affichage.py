import mappy
import conflits

Missions = 'missions.txt'

def convertisseur_temps(temps):
    min = temps // 60
    s = temps % 60
    heures = min // 60
    m = min % 60
    j = heures // 24
    h = heures % 24
    return j, h, m, s
    
def ecriture_missions(Missions, l_mission):
    with open(Missions, 'w') as f:
        f.write('{:~^50}\n\n'.format('Missions'))
        for m in l_mission:
            f.write('\nclient : ')
            cli_real = mappy.conversion_m_deg(m.client)
            f.write('longitude = {0}, latitude = {1}\n'.format(cli_real.long, cli_real.lat))
            f.write('entrepot : {0.entrepot}\n'.format(m))
            j, h, min, s = convertisseur_temps(m.heure_dmde)
            temps = '{}:{}:{}'.format(h, min, s)
            f.write('heure de la demande = {0}\n'.format(temps))
            f.write('drone utilisé : {0.drone}\n'.format(m))
            for p in m.trajet :
                # attention les points de trajet de chaque mission ont déjà été convertis en coordonnées sphériques par CZML
                p_real = mappy.conversion_m_deg(p)
                f.write('points du trajet : long : {0}, lat : {1}\n'.format(p_real.long, p_real.lat))
            f.write('\nconflits :')
            n_missions = len(l_mission)
            for i in range(n_missions):
                m1 = l_mission[i]
                for j in range(i+1, n_missions):
                    m2 = l_mission[j]
                    I = conflits.conflit(m1, m2)
                    if I :
                        f.write('les missions {} et {} sont en conflit\n'.format(m1, m2))
                        f.write('le conflit se passera entre {} et {} secondes\n'.format(conflits.heure_conflit(m1, m2)))
                        f.write('lieu du conflit : {}'.format(I))


                


