import json

def read(file):
    '''reading the file by using json method'''
    with open(file) as f:
        dictionary0 = json.load(f)
    return dictionary0
    
def drones_list(dictionary0):
    '''create the list of key in the dictionary0 to access to drone caracteristics'''
    drones = []
    for i, key in enumerate(dictionary0):
        if i: drones.append(key) #or key != '__comment'
    return drones

def get_h_speeds(dico, drone):
    '''return the maximum and the minimal horizontal speed of the drone'''
    return dico[str(drone)]['envelop']['v_max'], dico[str(drone)]['envelop']['v_min']

def get_v_speeds(dico, drone):
    '''return the maximum and the minimal vertical speed of the drone'''
    return dico[str(drone)]['envelop']['vs_max'], dico[str(drone)]['envelop']['vs_min'] 


### test
dico = read("aircraft.json")
drones = drones_list(dico)

for drone in drones:
    print(drone, ':', get_h_speeds(dico, drone), get_v_speeds(dico, drone))