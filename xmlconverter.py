import xml.etree.cElementTree as ET
import mappy
Livraison_par_drones = ET.Element('Livraison_par_drones')



def ecriture_mission( Livraison_par_drones , l_mission , l_conflits,file):
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
