import geometry as geo
import lecture_drones as lect_dr
import mappy
import tirage_au_sort as tas
import matplotlib.pyplot as plt
import trajet 


FILE = "aircraft.json"


def main():
    dico = lect_dr.read(FILE)
    models = lect_dr.listmodels(dico)
    carte = (mappy.A, mappy.C)
    entrepots, clients, carre_ext = tas.points_utiles(carte)
    x_entrepots,y_entrepots , x_clients, y_clients =[],[] , [],[]
    for i in range(len(entrepots)):
        x_entrepots.append(entrepots[i].x)
        y_entrepots.append(entrepots[i].y)
    for i in range(len(clients)):
        x_clients.append(clients[i].x)
        y_clients.append(clients[i].y)
    plt.plot(x_entrepots,y_entrepots, '.')
    plt.plot(x_clients,y_clients, '.')
    plt.show()
    tas.drones_utiles(dico, entrepots)
    model_prio = trajet.ordre_priorite_drones(models)
    #(model_prio)
    #for model in model_prio:
    #    print(model, model.v_speed_max)
    '''
    entrepot0 = tas.Entrepot(0,0,0, models)
    print(entrepot0)
    entrepot0.addDrone(lect_dr.Drone('Amzn', geo.Point(entrepot0.x, entrepot0.y, entrepot0.z)))
    print(entrepot0, '\n Les drones', entrepot0.drones, '\n Amazon Drone', entrepot0.models['Amzn'])
    for drone in entrepot0.drones:
        print(drone, entrepot0.drones, type(drone))
    print('capacité drone : ',capacite_drone(entrepot0, geo.Point(20,20,20)))
    '''
    
    missions = trajet.attribuer_mission(entrepots, clients)
    print('mission : ')
    mission = missions[0]      #on a choisi une mission
    client = mission[0]
    entrepot = mission[1]
    print('coordonnées client :')
    print(client)
    print('coordonnées entrepôt :')
    print(entrepot.x,entrepot.y)
    print('modèles présents dans entrepôt :')
    print(entrepot.models)
    p1, p2, p3, p4, dt = trajet.decoupe_trajet(mission)
    print('découpage spatial du trajet :')
    print(p1,p2,p3,p4)
    print('durée de la mission :')
    print(str(dt)+' secondes')
    print('Toulouse :')
    print(mappy.A, mappy.B, mappy.C, mappy.D)
    dep = mappy.conversion_m_deg(p2)
    arr = mappy.conversion_m_deg(p3)
    print('départ :')
    print(dep)
    print('arrivée :')
    print(arr)
main()