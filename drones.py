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


print(drones_list(read("aircraft.json")))