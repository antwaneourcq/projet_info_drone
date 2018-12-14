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
    l_entrepots, l_clients, carre_ext = tas.points_utiles(carte)
    x_entrepots,y_entrepots , x_clients, y_clients =[],[] , [],[]
    for i in range(len(l_entrepots)):
        x_entrepots.append(l_entrepots[i].x)
        y_entrepots.append(l_entrepots[i].y)
    for i in range(len(l_clients)):
        x_clients.append(l_clients[i].x)
        y_clients.append(l_clients[i].y)
    plt.plot(x_entrepots,y_entrepots, '.')
    plt.plot(x_clients,y_clients, '.')
    plt.show()
    print(tas.drones_utiles(dico, l_entrepots))

main()