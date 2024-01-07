######################################################################################################################
# Ligne de substitution à la dépendance aux programmes calcul_statistiques.py et recuperation_donnees.py
time_in_each_network = {'time_in_dot0': 368, 'time_in_dot1': 186, 'time_in_dot2': 167, 'time_with_no_road': 111}
######################################################################################################################


# diagramme_barres_3D_temps_sur_chaque_reseau.py
# Ce programme permet d'afficher en 3D des barres permettant de visualiser la proportion de temps d'utilisation de chaque réseau
# selon leurs localisations, grâce au module Matplotlib.
# Ce programme a besoin des données traitées par les programmes calcul_statistiques.py et recuperation_donnees.py pour fonctionner.
# Écrit par Yann Plougonven--Lastennet et Gurvan Mury,
# élèves en BUT réseaux et télécommunications à l'IUT de Lannion.
# Dernière édition de ce fichier le 31/12/2023 par Yann.

### Importation des modules ###
import matplotlib.pyplot as plt
from matplotlib import cm

def route_par_defaut_3D_bars(time_in_each_network : dict[str, int]) -> None:
    """Crée et affiche un graphique 3D en barres représentant la durée de connexion de l'ordinateur à chaque réseau, selon leurs localisation.

    Args:
        time_in_each_network (dict[str, int]): liste de dictionnaires représentant le temps (le nombre de minutes) que l'ordinateur a passé dans chaque réseau 
        pendant toute la capture des données.
    """
    # /!\ ATTENTION /!\ Pour pouvoir interagir avec le graphique en 3D, il est recommandé d'exécuter le code de cette cellule dans un fichier .py basique, et non dans un notebook.
    print("/!\ ATTENTION /!\ Pour interagir avec le graphique en 3D, il est recommandé d'exécuter le code de cette cellule dans un fichier .py basique, et non dans un notebook.")

    ### Taille de chaque barre du graphique ###
    total_time_in_dot0 : int = time_in_each_network["time_in_dot0"]
    total_time_in_dot1 : int = time_in_each_network["time_in_dot1"]
    total_time_in_dot2 : int = time_in_each_network["time_in_dot2"]

    ### Initialisation de la figure 3D ###
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ### Coordonnées des barres du graphique ###
    xpos : list[float] = [0.25, 0.75, 1.5] # position en x de la base des trois barres
    ypos : list[float] = [0.5, 1.5, 0.25] # position en y de la base des trois barres
    largeur : list[float] = [0.25, 0.25, 0.25] # largeur des barres
    profondeur : list[float] = [0.25, 0.25, 0.25] # profondeur des barres
    hauteur : list[int] = [total_time_in_dot0, total_time_in_dot1, total_time_in_dot2] # hauteur des barres

    ### Création des barres à partir de sous-barres de couleurs différentes (afin de créer un dégradé) ###
    max_height : int = max(hauteur) # hauteur maximale des barres pour la normalisation des couleurs du dégradé
    nb_sousbarres : int = 100 # nombre de barres à superposer pour créer le dégradé de couleur

    for i in range(len(xpos)): # pour chacune des barres
        color = hauteur[i] / max_height
        for numero_sousbarre in range(nb_sousbarres):
            zpos = numero_sousbarre * hauteur[i] / nb_sousbarres # position en z (hauteur) de la sous-barre
            hauteur_sousbarre = hauteur[i] / nb_sousbarres
            ax.bar3d(xpos[i], ypos[i], zpos, largeur[i], profondeur[i], hauteur_sousbarre, color=cm.coolwarm(color * (numero_sousbarre/nb_sousbarres)))

    ### Création des labels ###
    ax.set_title('Durée de connexion à chaque réseau selon leurs localisations')
    ax.set_zlabel("Durée de connexion au réseau (minutes)")
    ax.set_xticks([0, 1, 2])
    ax.set_yticks([0, 1, 2])
    ax.set_xticklabels([]) # forcer la suppression des labels des ticks l'axe x
    ax.set_yticklabels([]) # forcer la suppression des labels des ticks l'axe y

    labels = ['10.0 - domicile', '10.1 - travail', '10.2 - voisin']
    for i in range(len(xpos)):
        ax.text(xpos[i] - 0.2, ypos[i] - 0.2, 0, labels[i])

    ### Affichage du graphique ###
    plt.show()

route_par_defaut_3D_bars(time_in_each_network)