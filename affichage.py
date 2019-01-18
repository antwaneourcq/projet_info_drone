import mappy

Missions = 'missions.txt'

def convertisseur_temps(temps):
    '''donne le temps en jour, heure, minute, seconde'''
    min = temps // 60
    s = temps % 60
    heures = min // 60
    m = min % 60
    j = heures // 24
    h = heures % 24
    return j, h, m, s
    
def ecriture_missions(Missions, l_mission, l_conflits):
    '''écrit dans un fichier Missions les caracteristiques de chaque mission, ainsi que les conflits détectés.'''
    with open(Missions, 'w') as f:
        f.write('{:~^50}\n\n'.format('Missions'))
        for m in l_mission:
            f.write('\nmission : {}'.format(m.id))
            f.write('\nclient : ')
            cli_real = mappy.conversion_m_deg(m.client)
            f.write('longitude = {0}, latitude = {1}\n'.format(cli_real.long, cli_real.lat))
            f.write('entrepot : {0.entrepot}\n'.format(m))
            j, h, min, s = convertisseur_temps(m.heure_dmde)
            temps = '{}:{}:{}'.format(h, min, s)
            f.write('heure de la demande = {0}\n'.format(temps))
            f.write('drone utilisé : {0.drone}\n'.format(m))
            f.write('points du trajet:\n')
            f.write('{:^20}'.format('longitude: '))
            f.write('{:^20}'.format('latitude: '))
            f.write('{:^20}\n'.format('altitude: '))
            for p in m.trajet :
                # Attention les points de trajet de chaque mission ont déjà été convertis en coordonnées sphériques par CZML
                f.write('{:^20}'.format(p.long))
                f.write('{:^20}'.format(p.lat))
                f.write('{:^20}\n'.format(p.z))
            f.write('\nconflits :')
        for c in l_conflits:
            f.write('\n')
            try:
                f.write('les missions {} et {} sont en conflit\n'.format(c[0], c[1]))
            except:
                f.write('erreur du conflit ' + str(c) + '\n')