#import datetime
import json
import random
import geometry as geo
import mappy
from collections import OrderedDict

STEP = 1 #une seconde correspond à un pas de 1 pour les calculs précédents
MULTI = 5

class Document():
    
    def __init__(self, iD, start_time, end_time):
        self.id = iD
        self.name = "CZML Model"
        self.version = "1.0"
        timeS, timeE = conversionTimeCzml(start_time, end_time)
        timeS = timeS[:len(timeS)-1] + '.001Z'
        self.clock = {"interval" : timeS + '/' + timeE , "currentTime" : timeS, "multiplier": MULTI}
    
    def __repr__(self):
        return self.id, self.clock["interval"]
     
    def serialiseur(self, obj):
        if isinstance(obj, Document):
            return OrderedDict({"id":obj.id, "name":obj.name, "version":obj.version, "clock":obj.clock})
        raise TypeError(repr(obj) + "n'est pas sérialisable")
        
def conversionTimeCzml(time_start, time_end):
    if not time_start:
        time_start = 0
        print('time start non défini')
    if not time_end:
        time_end = 0
        print('time_end non défini')
    d0,h,m,s = mappy.convertisseur_temps(time_start)
    d = d0 + 1
    date = '2019-01'
    timeS = '{}-{:02d}T{:02d}:{:02d}:{:02d}Z'.format(date, d, h, m, s)
    d0, h, m, s = mappy.convertisseur_temps(time_end)
    d = d0 + 1
    timeE = '{}-{:02d}T{:02d}:{:02d}:{:02d}Z'.format(date, d, h, m, s)
    return timeS, timeE 

class Aircraft():
        
    def __init__(self, iD, description, name, points_trajet, time_start=0, time_end=0):
        self.id = iD
        self.description = '<h2>' + description + '</h2>'
        self.name = name
        #print(points_trajet[-1], points_trajet[0])
        timeS, timeE = conversionTimeCzml(points_trajet[0].t, points_trajet[-1].t)
        #print('afficaheg des temps :', timeS, timeE)
        self._availability = timeS + '/' + timeE
        self.position = {"epoch" : timeS}
        #modification
        #pts_trajet = [(pt.t, pt.x, pt.y, pt.z) for pt in points_trajet]
        pts_trajet = []
        t0 = points_trajet[0].t
        for pt in points_trajet:
            pts_trajet.append(pt.t - t0)
            pts_trajet.append(pt.long)
            pts_trajet.append(pt.lat)
            pts_trajet.append(pt.z)
        self.position["cartographicDegrees"] = pts_trajet
        self.orientation = {"velocityReference" : "#position"}
        color_1 = color_maker()
        color_2 = [255,255,255,110]
        self.path = {"material":{"polylineOutline":{"color":{"rgba":color_1}}, "outlineColor":{"rgba":color_1}, "outlineWidth":3}, "width":3, "leadTime":0,"trailTime":100000, "resolution":5}
        self.point = {"color" : {"rgba" : color_1}, "outlineColor" : {"rgba" : color_2}}
        self.point["outlineWidth"] = 2
        self.point["pixelSize"] = 12
        self.point["heightReference"] = "NONE"
        
    def __repr__(self):
        return self.id, self.name
    
    def serialiseur(self, obj):
        if isinstance(obj, Aircraft):
            #"__class__": "Aircraft", 
            return OrderedDict({"id":obj.id, "description":obj.description, "_availability":obj._availability, "name":obj.name, "position":obj.position, "orientation":obj.orientation, "path":obj.path, "point":obj.point})
        else :
            print(TypeError(repr(obj), " n'est pas sérialisable !"))
        

def color_maker():
    #[45,245,33,150]
    return [random.randint(45,255) for _ in range(3)] + [150]


def writeczml(missions):
    document = Document("document", 0, 86400) #trouver la derniere mission
    #drone = Aircraft('001', 'mon premier drone', 'Drone model', [0,1.47,43.67,50,20,1.47,43.67,1000,50,1.5,43.65,1000])
    with open('Test1.czml', 'w') as f: #, encoding ='utf-8'
        f.write('[\n')
        json.dump(document, f, indent=4, default = document.serialiseur)
        f.write(',\n')
        j, k = 0, 0
        print('\n MIssion : \n', missions, type(missions), 'type :', type(missions[0]), 'mission 00 : ', missions[0], 'fin de mission')
        n = len(missions)
        print('nombre de mission : ', n)
        s = [missions[0].trajet]

        for i, m in enumerate(missions):
            if m.drone:
                k += 1
                print('mission énumérée : ', i, m.trajet, '\n  entrepot attribué : ', m.drone)
                #if i==2:
                #    s.append(m)
                #e = mappy.conversion_m_deg(geo.Timed_Point(m.entrepot.x, m.entrepot.y, m.entrepot.z, m.heure_dmde))
                #c = mappy.conversion_m_deg(m.client)
                #if i ==2:
                #    s.append(e)
                #    s.append(c)
                mappy.conversion_mission(m)
                print('mission convertie : ', m.trajet)
                #if i==2:
                #    s.append('conversion réalisé')
                #    s.append(m.trajet)
                #print('entrepot :', e, 'client :', c)
                print(str(i), 'name'+str(i), str(m.drone))#, trajectoire[0], trajectoire[-1], trajectoire)
                print('\ntrajet :', m.trajet)
                drone = Aircraft(str(i), 'name'+str(i), str(m.drone), m.trajet) #, trajectoire[0].t, trajectoire[-1].t, 
                json.dump(drone, f, indent=4, default = drone.serialiseur)
                if i <= n-2:
                    f.write(',\n')

            else:
                j += 1
        print('nombre de mission non gérées :', j, 'derniere mission : ', i, 'par rapport à :', n)
        f.write('\n]')
        print('s = ', s)

        
'''        
def conversion(missions):
    for mission in missions:
        trajectoire = [mission.entrepot, mission.client] + mission.deviation
        drone = Aircraft('00XX', 'nameXX', str(mission.drone), trajectoire[0].t, trajectoire[-1].t, trajectoire)
'''
