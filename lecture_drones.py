import json
import geometry as geo

FILE = "aircraft.json"


def read(file):
    '''reading the file by using json method'''
    with open(file) as f:
        dico = json.load(f)
    del dico["__comment"] ##1er dictionnaire __comment explicatif inutile pour la suite
    return dico


class Drone():
    
    def __init__(self, key, coord, serial_number='serial_number'):
        '''"key" of the main dictionary, "coord" : Point from geometry, "available" if in a warehouse, "serial number" defined as str ex "_00"'''
        self.model =  key
        dico = read(FILE)
        self.h_speed_max = dico[key]['envelop']['v_max']
        self.h_speed_min = dico[key]['envelop']['v_min']
        self.v_speed_max = dico[key]['envelop']['vs_max']
        self.v_speed_min = dico[key]['envelop']['vs_min']
        self.h_max = dico[key]['envelop']['h_max']
        self.range = dico[key]['envelop']['d_range_max'] *1000 # km-> m
        self.current_position = coord
        self.available = True 
        #self.name = key + serial_number
        
    def __repr__(self):
        return str(self.model) #+ ' ; ' + str(self.current_position) + ' ; ' + str(self.available)



    
def listmodels(dico):
    models = []
    for key in dico.keys():
        models.append(Drone(key, geo.Point(float('inf'),float('inf'),0)))
        
    return models

def test():
    dico = read("aircraft.json")
    drones_model = dico.keys()
    print(drones_model) #probleme avec dict_keys([...])
    drones_model0 = []
    for key in dico.keys():
        drones_model0.append(key)
    print(drones_model0)
    first_drone = Drone(drones_model0[0], (5, 2, 0, 0), '_01')
    print(first_drone)
    #for i in range(len(drones_model)):
        
