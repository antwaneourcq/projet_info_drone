
def basic_map():
    '''meter'''


#carte est une liste de 2 tuples, donnant le coin supérieur gauche et le coin inférieur droit

def carre_int(carte):
#je creer l'environnement,
# environnement = liste de deux intervalles représenté par des tuples et correspond à l'intervalle des abcsisses et des ordonnées
    p = 5/100
    a,b,c,d = carte[0][0], carte[0][1] , carte[1][0] , carte[1][1]
    #je defint les limites de l'espace intérieur pour les clients
    return = a+p*l_x , c-p*l_x , d+p*l_y , b-p*l_y
