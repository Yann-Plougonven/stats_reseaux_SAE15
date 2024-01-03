# recuperation_donnees.py
# Ce programme permet de récupérer le contenu d'un fichier csv, puis de les traiter pour les rendre utilisables.
# Écrit par Yann Plougonven--Lastennet et Gurvan Mury,
# élèves en BUT réseaux et télécommunications à l'IUT de Lannion.
# Dernière édition de ce fichier le 03/01/2024 par Yann.

### Importation des modules ###
import csv
import datetime

### Initialisation des variables ###
chemin_fichier : str

### Définition du chemin du fichier csv à traiter ###
chemin_fichier = input('Chemin relatif du fichier csv à traiter (ou "", "1", "2", "3") :')
if chemin_fichier == "":
    chemin_fichier = "logs/LOG.csv"
elif chemin_fichier == "1" or "2" or "3":
    chemin_fichier = f"logs/LOG{chemin_fichier}.csv"

### Fonctions de traitement des fichiers csv ###


def put_csv_in_list(chemin_fichier : str) -> list[list[str]]:
    """Récupère les données contenues dans un fichier au format csv, et les stocke ligne par ligne dans une liste python.

    Args:
        chemin_fichier (str): chemin relatif vers le fichier csv à traiter.

    Returns:
        list[list[str]]: Liste contenant autant de listes que le fichier csv a de ligne. 
        Chaque ligne du csv est stockée dans une sous-liste différente.
    """
    ligne : str
    liste : list[str] = []
    with open(chemin_fichier, newline='') as csvfile :
        datareader = csv.reader(csvfile, delimiter= ',')
        for ligne in datareader:
            liste.append(ligne)
    return liste


def put_csv_in_dict(chemin_fichier : str) -> dict[str, list[str]]:
    """Récupère les données contenues dans un fichier au format csv, et les stocke dans un dictionnaire python.

    Args:
        chemin_fichier (str): chemin relatif vers le fichier csv à traiter.

    Returns:
        dict[str, list[str]]: dictionnaire contenant autant de clés (str) et de valeurs (listes) que le fichier csv a de ligne. 
        Chaque ligne du csv est stockée dans une relation clé:valeur différente.
    """
    i : int
    dico : dict[str] = {}
    liste : list[str] = put_csv_in_list(chemin_fichier)
    for i in range(len(liste)):
        dico[liste[i][0]] = liste[i][1:]
    return dico


def epoch_to_date(epochtimes : list[int]) -> list[str]:
    """Transforme chaque minutes au format epoch de la liste passée en paramètre, en des heures facilement lisibles par l'humain.

    Args:
        epochtimes (list[int]): liste contenant des heures au fomat epoch.

    Returns:
        list[str]: liste contenant des heures dans un format lisible par l'humain.
    """
    epoch : int
    date : str
    resultat : list[str] = []
    for epoch in epochtimes:
        date = datetime.datetime.fromtimestamp(epoch).strftime('%H:%M')
        resultat.append(date)
    return resultat


def transposer(chemin_fichier : str) -> list:
    """Transpose les données contenues dans un fichier au format csv, et les stocke dans une liste python contenant autant de sous-listes que le fichier csv a de valeur par ligne.
    Converti les données du format str au format int, si possible.
    Ajoute une sous-liste list[str], à la fin de la liste de retour, contenant les temps convertis du format epoch au format lisible par l'humain.

    Args:
        chemin_fichier (str): chemin relatif vers le fichier csv à traiter.

    Returns:
        list: contient autant de sous-listes que le fichier csv a de valeur par ligne, plus une liste (list[str]) contenant les temps de la première sous-liste (list[int]),
        convertis du format epoch au format lisible par l'humain (str).
        Une sous-liste correspond à une métrique contenu dans le fichier csv.
    """
    i : int
    j : int
    liste : list[str] = put_csv_in_list(chemin_fichier)
    une_valeur : str
    resultat : list[list[str]] = [[] for i in range(len(liste[0]) + 1)]
    #resultat : list[list[str]] = [[]]*len(liste[0]) # Avec cette méthode, les x listes seraient liées entre elles, ce qui pose des problèmes.

    for i in range(len(liste[0])):
        for j in range(len(liste)):
            une_valeur = liste[j][i]

            if une_valeur.isdigit(): # Si la valeur peut être représentée par un entier, la stocker sous forme d'entier
                resultat[i].append(int(une_valeur))

            else: # Si la valeur ne peut pas être représentée par un entier, la stocker sous forme de chaine de caractère
                resultat[i].append(une_valeur)

    resultat[-1] = epoch_to_date(resultat[0]) # Ajouter une liste contenant l'heure dans un format lisible

    return resultat


### Enregistrement des résultats des 3 premières fonctions de traitement des données ###
liste_donnees : list[list[str]]
liste_donnees = put_csv_in_list(chemin_fichier)

dictionnaire_donnees : dict[str, list[str]]
dictionnaire_donnees = put_csv_in_dict(chemin_fichier)

transposee : list
transposee = transposer(chemin_fichier)


print(f"liste_donnees : {liste_donnees}")
print(f"dictionnaire_donnees : {dictionnaire_donnees}")
print(f"transposee : {transposee}")