#!/bin/bash
# change_values.sh
# Ce script modifie les différentes valeurs relatives au fonctionnement de
# certains services réseaux du système d'exploitation.
# Ces valeurs peuvent être consultées grâce aux commandes "ip a" et "ip route".
# et sont en partie choisies de façon aléatoire.
# Paramètres du script : aucun.
# Retourne le code 0.
# Écrit par Gurvan Mury et Yann Plougonven--Lastennet,
# élèves en BUT réseaux et télécommunications à l'IUT de Lannion.
# Dernière édition de ce fichier le 30/11/2023 par Yann.


### Attendre 2 secondes avant la suite de l'exécution ###

# Cela permet de s'assurer que ce script ne modifie pas les paramètres
# pendant la lecture des données par le script update_csv.sh.
sleep 2


### Générer des entiers aléatoires ###

nb_random_route_defaut=$(shuf -i 0-5 -n1) # Entre 0 et 5 inclus
nb_random_statut_int=$(shuf -i 0-10 -n1) # Entre 0 et 10 inclus
nb_random_supprimer_int=$(shuf -i 0-20 -n1) # Entre 0 et 20 inclus


### Changer la route par défaut ###

# Deux chances sur 5 de définir 10.0.255.254 en route par défaut :
if [ $nb_random_route_defaut = 0 ] || [ $nb_random_route_defaut = 3 ]
then
    ip link set enp0s9 up
    ip addr flush enp0s9
    ip addr add 10.0.0.1/16 dev enp0s9
    ip route add default via 10.0.255.254 
fi

# Une chance sur 5 de définir 10.1.255.254 en route par défaut :
if [ $nb_random_route_defaut = 1 ]
then
    ip link set enp0s9 up
    ip addr flush enp0s9
    ip addr add 10.1.0.1/16 dev enp0s9
    ip route add default via 10.1.255.254 
fi

# Une chance sur 5 de définir 10.2.255.254 en route par défaut :
if [ $nb_random_route_defaut = 2 ]
then
    ip link set enp0s9 up
    ip addr flush enp0s9
    ip addr add 10.2.0.1/16 dev enp0s9
    ip route add default via 10.2.255.254
fi


### Désactiver et activer aléatoirement des interfaces ###

# Une chance sur 5 de désactiver enp0s8 :
if [ $nb_random_statut_int = 1 ] || [ $nb_random_statut_int = 4 ]
then
    ip link set down enp0s8
fi

# Une chance sur 10 d'activer enp0s8 :
if [ $nb_random_statut_int = 5 ]
then
    ip link set up enp0s8
fi

# Une chance sur 10 de désactiver enp0s10 :
if [ $nb_random_statut_int = 2 ]
then
    ip link set down enp0s10
fi

# Une chance sur 10 d'activer enp0s10 :
if [ $nb_random_statut_int = 6 ]
then
    ip link set up enp0s10
fi

# Une chance sur 10 de désactiver enp0s17 : 
if [ $nb_random_statut_int = 3 ]
then
    ip link set down enp0s17
fi

# Une chance sur 10 d'activer enp0s17 : 
if [ $nb_random_statut_int = 7 ]
then
    ip link set up enp0s17
fi


### Supprimer une interface ###

# Sur certaines machines virtuelles, 
# docker0 est la seule interface pouvant être supprimée.
# Il est possible de la réactiver au redémarrage de la machine virtuelle.

# 1 chance sur 20 de supprimer l'interface docker0 :
if [ $nb_random_supprimer_int = 0 ] 
then 
    ip link delete docker0
fi


### Fin de l'execution du script ###

echo "$(date +%s) : Le script de changement des valeurs a bien été exécuté."
exit 0