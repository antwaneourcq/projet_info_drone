import xml.etree.cElementTree as ET
import mappy

Livraison_par_drones = ET.Element('Livraison_par_drones')


def ecriture_xml( Livraison_par_drones , l_mission , l_conflits,file):
    '''ecrit dans un fichier xml, les missions et leurs caractéristiques'''
    for m in l_mission :
        mission = ET.SubElement(Livraison_par_drones, "mission")
        mission.text = '\nid : {0}'.format(m.id)

        client = ET.SubElement(mission , 'client:')
        cli_real = mappy.conversion_m_deg(m.client)
        client.text = '{0.client}\n\n longitude = {1} , latitude = {2}'.format(m, cli_real.long , cli_real.lat)

        entrepot = ET.SubElement(mission, 'entrepot:')
        entrepot.text = '{0.entrepot}\n\n'.format(m)

        drone = ET.SubElement(mission , 'drone:')
        drone.text = 'model : {0.model}\n vitesse_horizontale : {1.h_speed_max}\n\n'.format(m.drone, m.drone, m.drone )

        altitude = ET.SubElement(mission, 'altitude')
        altitude.text = '{0.alti}\n\n'.format(m)

    for c in l_conflits:
        conflit = ET.SubElement(Livraison_par_drones, "conflit")
        conflit.text = 'les missions {} et {} sont en conflit\n le conflit se passera entre {} et {} secondes\n lieu du conflit : {}\n' .format(conflit[0], conflit[1], conflit[3], conflit[4],conflit[2])
    tree = ET.ElementTree(Livraison_par_drones)
    tree.write(file)


def convertisseur_temps(temps):
    '''donne le temps en jour, heure, minute, seconde'''
    min = temps // 60
    s = temps % 60
    heures = min // 60
    m = min % 60
    j = heures // 24
    h = heures % 24
    return j, h, m, s


def ecriture_txt(Missions, l_mission, l_conflits, mission_vide, mission_traite):
    '''écrit dans un fichier Missions les caracteristiques de chaque mission, ainsi que les conflits détectés.'''
    with open(Missions, 'w') as f:
        f.write('{:~^50}\n\n'.format('Missions'))
        f.write('missions vides: {}, missions traités: {}\n'.format(mission_vide, mission_traite))
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
            for p in m.trajet:
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