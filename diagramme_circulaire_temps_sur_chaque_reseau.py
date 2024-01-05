######################################################################################################################
# Ligne de substitution à la dépendance aux programmes calcul_statistiques.py et recuperation_donnees.py
time_in_each_network = {'time_in_dot0': 368, 'time_in_dot1': 186, 'time_in_dot2': 167, 'time_with_no_road': 111}
######################################################################################################################


# diagramme_circulaire_temps_sur_chaque_reseau.py
# Ce programme permet d'afficher un diagramme circulaire permettant de visualiser la proportion de temps d'utilisation de chaque réseau, grâce au module Mathplotlib.
# Ce programme a besoin des données traitées par les programmes calcul_statistiques.py et recuperation_donnees.py pour fonctionner.
# Écrit par Yann Plougonven--Lastennet et Gurvan Mury,
# élèves en BUT réseaux et télécommunications à l'IUT de Lannion.
# Dernière édition de ce fichier le 05/01/2024 par Yann.

### Importation des modules ###
import matplotlib.pyplot as plt

def route_par_defaut_pie(donnees : list[int]) -> None:
    """Crée et affiche un diagramme circulaire représentant la proportion temps d'utilisation de chaque réseau.

    Args:
        donnees (list[int]): liste contenant le temps d'utilisation de chaque réseau, en minutes,
        dans l'ordre "10.0 - domicile", "10.1 - travail", "10.2 - voisin" puis "Aucune route par défaut".
    """
    labels : list[str]
    colors : list[str]
    wedgeprops : dict[str:int, str:str]

    labels = ["10.0 - domicile", "10.1 - travail", "10.2 - voisin", "Aucune route par défaut"]
    colors = ["#60a7d2", "#2e7ebc", "#a1cbe2", "#d0e1f2"] # Couleurs utilisé par le schéma
    wedgeprops = {"linewidth": 1, "edgecolor": "white"} # Ligne de séparation entre chaque secteur

    plt.pie(donnees, labels=labels, colors=colors, wedgeprops=wedgeprops, autopct='%1.1f%%')
    plt.title("Pourcentage de temps d'utilisation de chaque réseau")
    plt.show

route_par_defaut_pie(time_in_each_network.values())