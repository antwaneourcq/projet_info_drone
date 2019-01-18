import json
import geometrie as geo

FILE = "aircraft.json"


def read(file):
    '''lit le fichier .json en utilisant la méthode json'''
    with open(file) as f:
        dico = json.load(f)
    del dico["__comment"] #1er dictionnaire __comment explicatif inutile pour la suite
    return dico


class Drone():
    
    def __init__(self, key, coord, serial_number='serial_number'):
        '''"key" clé pour le dictionnaire issu de aircraft.json, "coord" : Point du module geometry, "available" si le drone est dans l'entrepot,'''
        self.model = key
        dico = read(FILE)
        self.h_speed_max = dico[key]['envelop']['v_max']
        self.h_speed_min = dico[key]['envelop']['v_min']
        self.v_speed_max = dico[key]['envelop']['vs_max']
        self.v_speed_min = dico[key]['envelop']['vs_min']
        self.h_max = dico[key]['envelop']['h_max']
        self.range = dico[key]['envelop']['d_range_max'] * 1000    #Conversion des kilomètres en mètres
        self.current_position = coord
        self.available = True

    def __repr__(self):
        return str(self.model)



    
def listmodels(dico):
    models = []
    for key in dico.keys():
        models.append(Drone(key, geo.Point(float('inf'),float('inf'),0)))
    return models