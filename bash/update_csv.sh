#!/bin/bash
# update_csv.sh
# Ce script capture différentes valeurs relatives au fonctionnement du système
# et obtenables grâce aux commandes "ip a" et "ip route".
# Ces valeurs sont ensuite datées et transférées dans un fichier LOG.csv. 
# Paramètres du script: aucun.
# Retourne le code 0.
# Ecrit par Gurvan Mury et Yann Plougonven--Lastennet,
# élèves en BUT réseaux et télécommunications à l'IUT de Lannion.
# Dernière édition de ce fichier le 03/01/2024 par Yann.


### Obtention des valeurs ###

# Obtention de l'heure :
date_epoch=$(date +%s)

# Obtention de l'IP de la route par défaut (potentiellement vide) :
ip_route_defaut=$(ip route | grep default | cut -f 3 -d " ")

# Obtention du nombre total d'interfaces réseau :
nb_int=$(ip a | grep '^[0-9]' | wc -l)

# Obtention du nombre total d'interfaces réseau activées (UP) :
nb_int_up=$(ip a | grep '^[0-9]' | grep 'state UP' |  wc -l)

# Obtention du nombre total d'interfaces réseau désactivées (DOWN) :
nb_int_down=$(ip a | grep '^[0-9]' | grep 'state DOWN' |  wc -l)

# Obtention du nombre total d'interfaces réseau avec le statut UNKNOW :
# Ce nombre est censé rester à 1, car la loopback lo est la seule interface
# censée avoir le statut UNKNOW :
nb_int_unknow=$(ip a | grep '^[0-9]' | grep 'state UNKNOW' |  wc -l)


### Ecriture des valeurs dans le fichier LOG.csv ###
# L'utilisation d'un chemin absolu a l'avantage de nous permettre d'être certain
# de l'emplacement d'enregistrement des données, quel que soit l'emplacement d'exécution de ce script.
echo $date_epoch,$nb_int,$nb_int_up,$nb_int_down,$nb_int_unknow,$ip_route_defaut >> /root/Documents/SAE15/LOG.csv


### Fin de l'éxecution du script ###
echo "$date_epoch : Les informations réseau ont été enregistrées dans root/Documents/SAE15/LOG.csv."
exit 0