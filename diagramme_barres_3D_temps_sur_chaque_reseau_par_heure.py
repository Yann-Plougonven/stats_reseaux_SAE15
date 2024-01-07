######################################################################################################################
# Ligne de substitution à la dépendance aux programmes calcul_statistiques.py et recuperation_donnees.py 
time_in_each_network_by_hour = [{'time_in_dot0': 32, 'time_in_dot1': 17, 'time_in_dot2': 6, 'time_with_no_road': 5, 'hour': '18:00'}, {'time_in_dot0': 27, 'time_in_dot1': 15, 'time_in_dot2': 12, 'time_with_no_road': 6, 'hour': '19:00'}, {'time_in_dot0': 23, 'time_in_dot1': 13, 'time_in_dot2': 14, 'time_with_no_road': 10, 'hour': '20:00'}, {'time_in_dot0': 16, 'time_in_dot1': 13, 'time_in_dot2': 22, 'time_with_no_road': 9, 'hour': '21:00'}, {'time_in_dot0': 38, 'time_in_dot1': 8, 'time_in_dot2': 9, 'time_with_no_road': 5, 'hour': '22:00'}, {'time_in_dot0': 31, 'time_in_dot1': 10, 'time_in_dot2': 11, 'time_with_no_road': 8, 'hour': '23:00'}, {'time_in_dot0': 22, 'time_in_dot1': 12, 'time_in_dot2': 16, 'time_with_no_road': 10, 'hour': '00:00'}, {'time_in_dot0': 28, 'time_in_dot1': 14, 'time_in_dot2': 9, 'time_with_no_road': 9, 'hour': '01:00'}, {'time_in_dot0': 22, 'time_in_dot1': 17, 'time_in_dot2': 12, 'time_with_no_road': 9, 'hour': '02:00'}, {'time_in_dot0': 24, 'time_in_dot1': 17, 'time_in_dot2': 14, 'time_with_no_road': 5, 'hour': '03:00'}, {'time_in_dot0': 21, 'time_in_dot1': 11, 'time_in_dot2': 21, 'time_with_no_road': 7, 'hour': '04:00'}, {'time_in_dot0': 32, 'time_in_dot1': 16, 'time_in_dot2': 7, 'time_with_no_road': 5, 'hour': '05:00'}, {'time_in_dot0': 26, 'time_in_dot1': 9, 'time_in_dot2': 10, 'time_with_no_road': 15, 'hour': '06:00'}, {'time_in_dot0': 26, 'time_in_dot1': 14, 'time_in_dot2': 4, 'time_with_no_road': 8, 'hour': '07:00'}]
######################################################################################################################


# diagramme_barres_3D_temps_sur_chaque_reseau_par_heure.py
# Ce programme permet d'afficher en 3D des barres permettant de visualiser la proportion de temps d'utilisation de chaque réseau par heure, et
# selon leurs localisations, grâce au module Matplotlib.
# Ce programme a besoin des données traitées par les programmes calcul_statistiques.py et recuperation_donnees.py pour fonctionner.
# Écrit par Yann Plougonven--Lastennet et Gurvan Mury,
# élèves en BUT réseaux et télécommunications à l'IUT de Lannion.
# Dernière édition de ce fichier le 05/01/2024 par Yann.

### Importation des modules ###
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib import cm
import numpy as np


def route_par_defaut_live_3D_bars(time_in_each_network_by_hour : list[dict[str:int, str:int, str:int, str:int, str:str]]) -> None:
    """Crée et affiche un graphique 3D en barres représentant la durée de connexion de l'ordinateur à chaque réseau, selon leurs localisation, 
    pendant l'heure choisie par l'utilisateur avec un curseur.

    Args:
        time_in_each_network_by_hour (list[dict[str:int, str:int, str:int, str:int, str:str]]): liste de dictionnaires représentant le temps (le nombre de minutes) que l'ordinateur a passé CHAQUE HEURE dans chaque réseau.
    """
    # /!\ ATTENTION /!\ Pour pouvoir interagir avec le graphique en 3D, il est recommandé d'exécuter le code de cette cellule dans un fichier .py basique, et non dans un notebook.
    print("/!\ ATTENTION /!\ Pour interagir avec le graphique en 3D, il est recommandé d'exécuter le code de cette cellule dans un fichier .py basique, et non dans un notebook.")
    
    ### Typage des variables ###
    hours : list[str] = []
    xpos : list[float]
    ypos : list[float]
    largeur : list[float]
    profondeur : list[float]
    hauteur : list[int]
    bars : list 
    max_height : int
    nb_sousbarres_previsualisation : int 
    i : int
    labels : list[str]

    ### Initialisation de la figure 3D ###
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ### Initialisation du curseur ###
    axtime = plt.axes([0.2, 0.01, 0.7, 0.03]) # positionnement et taille du curseur
    slider_time = Slider(axtime, 'Heure', 0, len(time_in_each_network_by_hour)-1, valinit=0, valstep=1)
    
    for i in range(len(time_in_each_network_by_hour)):
        hours.append(time_in_each_network_by_hour[i]["hour"])

    ### Coordonnées des barres du graphique ###
    xpos = [0.25, 0.75, 1.5] # position en x de la base des trois barres
    ypos = [0.5, 1.5, 0.25] # position en y de la base des trois barres
    largeur = [0.25, 0.25, 0.25] # largeur des barres
    profondeur = [0.25, 0.25, 0.25] # profondeur des barres
    
    # Hauteur des barres :
    hauteur = [time_in_each_network_by_hour[0]['time_in_dot0'], 
               time_in_each_network_by_hour[0]['time_in_dot1'], 
               time_in_each_network_by_hour[0]['time_in_dot2']]
    

    ### Afficher les premières barres dès le début ###
    bars = []
    max_height = max(hauteur) # hauteur maximale des barres pour la normalisation des couleurs du dégradé
    nb_sousbarres_previsualisation : int = 100 # nombre de barres à superposer pour créer le dégradé de couleur (réduire ce nombre sur les ordinateurs peu performants)
    for i in range(len(xpos)): # pour chacune des barres
        color = hauteur[i] / max_height
        for z in np.arange(0, hauteur[i], hauteur[i]/nb_sousbarres_previsualisation):
            bars.append(ax.bar3d(xpos[i], ypos[i], z, largeur[i], profondeur[i], hauteur[i]/nb_sousbarres_previsualisation, color=cm.coolwarm(color * (z/hauteur[i]))))

    ### Mettre à jour chaque barre quand le curseur est utilisé ###
    def update(val) -> None:
        """Méthode appellée pour mettre à jour les barres affichées sur le graphique, lorsque le curseur est bougé par l'utilsateur.

        Args:
            val : valeur quelquonque exigée par matplotlib, ne devant pas figurer dans l'appel de la méthode.
        """
        numero_heure = int(slider_time.val)
        slider_time.valtext.set_text(hours[numero_heure]) # changer la valeur de l'heure à côté du curseur
        
        # Hauteur des barres :
        hauteur = [time_in_each_network_by_hour[numero_heure]['time_in_dot0'], 
                   time_in_each_network_by_hour[numero_heure]['time_in_dot1'], 
                   time_in_each_network_by_hour[numero_heure]['time_in_dot2']]

        ### Supprimer les barres à remplacer ###
        for bar in bars:
            bar.remove()
        bars.clear()

        ### Afficher les nouvelles barres ###
        max_height : int = max(hauteur) # hauteur maximale des barres pour la normalisation des couleurs du dégradé
        nb_sousbarres = 50 # nombre de barres à superposer pour créer le dégradé de couleur (réduire ce nombre sur les ordinateurs peu performants)
        for i in range(len(xpos)): # pour chacune des barres
            color = hauteur[i] / max_height
            for z in np.arange(0, hauteur[i], hauteur[i]/nb_sousbarres):
                bars.append(ax.bar3d(xpos[i], ypos[i], z, largeur[i], profondeur[i], hauteur[i]/nb_sousbarres, color=cm.coolwarm(color * (z/hauteur[i]))))

    slider_time.on_changed(update)

    ### Création des labels ###
    ax.set_title('Durée de connexion par heure à chaque réseau, selon leurs localisations')
    ax.set_zlabel("Durée de connexion au réseau (minutes)")
    ax.set_xticks([0, 1, 2])
    ax.set_yticks([0, 1, 2])
    ax.set_zlim(0, 60) # forcer l'axe z à toujours être à la même hauteur (ici 60, pour 60 minutes dans une heure)
    ax.set_xticklabels([]) # forcer la suppression des labels des ticks l'axe x
    ax.set_yticklabels([]) # forcer la suppression des labels des ticks l'axe y

    labels = ['10.0 - domicile', '10.1 - travail', '10.2 - voisin']
    for i in range(len(xpos)):
        ax.text(xpos[i] - 0.2, ypos[i] - 0.2, 0, labels[i])

    ### Affichage du graphique ###
    plt.show()

route_par_defaut_live_3D_bars(time_in_each_network_by_hour)