STEP = 0, 1
import trajet

def select(missions, t):
    drones_actifs = []
    for mission in missions:
        if select_drone(mission,t):
            drones_actifs.append(mission.drone)


def select_drone(mission,t ):
    p1, p4 = trajet.decoupe_trajet(mission)[0],trajet.decoupe_trajet(mission)[3]
    duree = trajet.calcul_duree_mission(mission.drone, p1, p4)
    return mission.heure_dmde - duree <= t <= mission.heure_dmde


class Simulation:
    """The simulation state """

    def __init__(self, missions, start=0):
        self.missions = missions
        self.t = start
        self.drones_actifs = select_drone(missions, self.t)

    def set_time(self, t):
        '''met en place le temps de la simulation'''
        self.t = t
        self.drones_actifs = select(self.missions , t )

    def increment_time(self, dt):
        '''avance le temps'''
        self.set_time(self.t + dt)





def drones_en_points()