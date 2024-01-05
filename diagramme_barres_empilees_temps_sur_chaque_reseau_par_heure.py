######################################################################################################################
# Ligne de substitution à la dépendance aux programmes calcul_statistiques.py et recuperation_donnees.py
time_in_each_network_by_hour = [{'time_in_dot0': 32, 'time_in_dot1': 17, 'time_in_dot2': 6, 'time_with_no_road': 5, 'hour': '18:00'}, {'time_in_dot0': 27, 'time_in_dot1': 15, 'time_in_dot2': 12, 'time_with_no_road': 6, 'hour': '19:00'}, {'time_in_dot0': 23, 'time_in_dot1': 13, 'time_in_dot2': 14, 'time_with_no_road': 10, 'hour': '20:00'}, {'time_in_dot0': 16, 'time_in_dot1': 13, 'time_in_dot2': 22, 'time_with_no_road': 9, 'hour': '21:00'}, {'time_in_dot0': 38, 'time_in_dot1': 8, 'time_in_dot2': 9, 'time_with_no_road': 5, 'hour': '22:00'}, {'time_in_dot0': 31, 'time_in_dot1': 10, 'time_in_dot2': 11, 'time_with_no_road': 8, 'hour': '23:00'}, {'time_in_dot0': 22, 'time_in_dot1': 12, 'time_in_dot2': 16, 'time_with_no_road': 10, 'hour': '00:00'}, {'time_in_dot0': 28, 'time_in_dot1': 14, 'time_in_dot2': 9, 'time_with_no_road': 9, 'hour': '01:00'}, {'time_in_dot0': 22, 'time_in_dot1': 17, 'time_in_dot2': 12, 'time_with_no_road': 9, 'hour': '02:00'}, {'time_in_dot0': 24, 'time_in_dot1': 17, 'time_in_dot2': 14, 'time_with_no_road': 5, 'hour': '03:00'}, {'time_in_dot0': 21, 'time_in_dot1': 11, 'time_in_dot2': 21, 'time_with_no_road': 7, 'hour': '04:00'}, {'time_in_dot0': 32, 'time_in_dot1': 16, 'time_in_dot2': 7, 'time_with_no_road': 5, 'hour': '05:00'}, {'time_in_dot0': 26, 'time_in_dot1': 9, 'time_in_dot2': 10, 'time_with_no_road': 15, 'hour': '06:00'}, {'time_in_dot0': 26, 'time_in_dot1': 14, 'time_in_dot2': 4, 'time_with_no_road': 8, 'hour': '07:00'}]
######################################################################################################################


# diagramme_barres_empilees_temps_sur_chaque_reseau_par_heure.py
# Ce programme permet d'afficher des barres empilées permettant de visualiser la proportion de temps d'utilisation de chaque réseau par heure, grâce au module Mathplotlib.
# Ce programme a besoin des données traitées par les programmes calcul_statistiques.py et recuperation_donnees.py pour fonctionner.
# Écrit par Yann Plougonven--Lastennet et Gurvan Mury,
# élèves en BUT réseaux et télécommunications à l'IUT de Lannion.
# Dernière édition de ce fichier le 05/01/2024 par Yann.

### Importation des modules ###
import numpy as np
import matplotlib.pyplot as plt

def show_route_par_defaut_in_bars(unit : str, hours : list[str], time_in_dot0 : list[int], time_in_dot1 : list[int], time_in_dot2 : list[int], time_with_no_road : list[int]) -> None:
    """Crée et affiche le graphique en barres empilées illustrant la durée de connexion à chaque réseau par heure,
    une fois les données préprarées par les fonctions route_par_defaut_bars et route_par_defaut_bars_percentage.

    Args:
        unit (str): unité du temps de fonctionnement dans l'heure (minute ou %)
        hours (list[str]): liste contenant l'heure de chaque barre (toutes les 60 minutes) (abscisse)
        time_in_dot0 (list[int]): liste contenant le temps (en minutes ou en pourcentage) passé chaque heure sur la route par défaut 10.0.255.254
        time_in_dot1 (list[int]): liste contenant le temps (en minutes ou en pourcentage) passé chaque heure sur la route par défaut 10.1.255.254
        time_in_dot2 (list[int]): liste contenant le temps (en minutes ou en pourcentage) passé chaque heure sur la route par défaut 10.2.255.254
        time_with_no_road (list[int]): liste contenant le temps (en minutes ou en pourcentage) passé chaque heure sans route par défaut
    """
    ### Définition de la hauteur à partir de laquelle chaque barre doit être représentée ###
    bottom_dot1 : list[int] = time_in_dot0
    bottom_dot2 = np.add(time_in_dot0, time_in_dot1)
    bottom_no_road = np.add(bottom_dot2, time_in_dot2)

    ### Création des barres à afficher ###
    plt.bar(hours, time_in_dot0, label='10.0 - domicile', color="#60a7d2")
    plt.bar(hours, time_in_dot1, bottom=bottom_dot1, label='10.1 - travail', color="#2e7ebc")
    plt.bar(hours, time_in_dot2, bottom=bottom_dot2, label='10.2 - voisin', color = "#a1cbe2")
    plt.bar(hours, time_with_no_road, bottom=bottom_no_road, color="white")

    ### Créations de la légende  ###
    plt.title("Temps de connexion à chaque réseau par heure")
    plt.xlabel('Heure')
    plt.ylabel(f"Temps de fonctionnement dans l'heure ({unit})")
    plt.xticks(rotation = 90)
    plt.legend()

    ### Affichage du graphique ###
    plt.show()


def route_par_defaut_bars(time_in_each_network_by_hour : list[dict[str:int, str:int, str:int, str:int, str:str]]) -> None:
    """Prépare les données pour qu'elles soient utilisable par la fonction show_route_par_defaut_in_bars, puis appelle cette fonction show_route_par_defaut_in_bars.
    Les données permetteront la création d'un graphique en barres empilées tel que décrit dans le docstring de la fonction show_route_par_defaut_in_bars, 
    en utilisant comme unité les MINUTES.
    Comme contrainte, nous nous sommes imposé d'utiliser une liste de dictionnaires en entrée des fonctions, pour les deux graphiques suivants. 
    Ce n'est évidemment pas la manière la plus optimisée, mais c'était un bon exercice pour renforcer notre maitrise des dictionnaires Python tout en répondant à la consigne.

    Args:
        time_in_each_network_by_hour (list[dict[str:int, str:int, str:int, str:int, str:str]]): liste de dictionnaires représentant le temps (le nombre de minutes) que l'ordinateur a passé CHAQUE HEURE dans chaque réseau
    """
    i : int
    hours : list[str] = []
    time_in_dot0 : list[int] = []
    time_in_dot1 : list[int] = []
    time_in_dot2 : list[int] = []
    time_with_no_road : list[int] = []

    for i in range(len(time_in_each_network_by_hour)):
        hours.append(time_in_each_network_by_hour[i]["hour"])
        time_in_dot0.append(time_in_each_network_by_hour[i]["time_in_dot0"])
        time_in_dot1.append(time_in_each_network_by_hour[i]["time_in_dot1"])
        time_in_dot2.append(time_in_each_network_by_hour[i]["time_in_dot2"])
        time_with_no_road.append(time_in_each_network_by_hour[i]["time_with_no_road"])

    show_route_par_defaut_in_bars("minutes", hours, time_in_dot0, time_in_dot1, time_in_dot2, time_with_no_road)


def route_par_defaut_bars_percentage(time_in_each_network_by_hour : list[dict[str:int, str:int, str:int, str:int, str:str]]) -> None:
    """Prépare les données pour qu'elles soient utilisable par la fonction show_route_par_defaut_in_bars, puis appelle cette fonction show_route_par_defaut_in_bars.
    Les données permetteront la création d'un graphique en barres empilées tel que décrit dans le docstring de la fonction show_route_par_defaut_in_bars, 
    en utilisant comme unité le POURCENTAGE.
    Comme contrainte, nous nous sommes imposé d'utiliser une liste de dictionnaires en entrée des fonctions, pour les deux graphiques suivants. 
    Ce n'est évidemment pas la manière la plus optimisée, mais c'était un bon exercice pour renforcer notre maitrise des dictionnaires Python tout en répondant à la consigne.

    Args:
        time_in_each_network_by_hour (list[dict[str:int, str:int, str:int, str:int, str:str]]): liste de dictionnaires représentant le temps (le nombre de minutes) que l'ordinateur a passé CHAQUE HEURE dans chaque réseau
    """
    i : int
    hours : list[str] = []
    time_in_dot0_percent : list[int] = []
    time_in_dot1_percent : list[int] = []
    time_in_dot2_percent : list[int] = []
    time_with_no_road_percent : list[int] = []

    for i in range(len(time_in_each_network_by_hour)):
        hours.append(time_in_each_network_by_hour[i]["hour"])
        time_in_dot0_percent.append(time_in_each_network_by_hour[i]["time_in_dot0"] / 60 * 100)
        time_in_dot1_percent.append(time_in_each_network_by_hour[i]["time_in_dot1"] / 60 * 100)
        time_in_dot2_percent.append(time_in_each_network_by_hour[i]["time_in_dot2"] / 60 * 100)
        time_with_no_road_percent.append(time_in_each_network_by_hour[i]["time_with_no_road"] / 60 * 100)

    show_route_par_defaut_in_bars("%", hours, time_in_dot0_percent, time_in_dot1_percent, time_in_dot2_percent, time_with_no_road_percent)


route_par_defaut_bars(time_in_each_network_by_hour)
route_par_defaut_bars_percentage(time_in_each_network_by_hour)