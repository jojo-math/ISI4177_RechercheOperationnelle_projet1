# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 10:42:22 2025

@author: Home
"""

"""
fichier des methodes
"""

import csv
import random
from itertools import combinations

def generer_contacts_csv(nb_clients=250, taux_connexion=0.1, fichier_sortie="contacts.csv"):
    """
    Génère un fichier CSV représentant un graphe non orienté de contacts entre clients.
    Chaque ligne : client_i, client_j, distance_jour_moyen
    """
    paires_possibles = list(combinations(range(nb_clients), 2))
    nb_aretes = int(len(paires_possibles) * taux_connexion)
    aretes_selectionnees = random.sample(paires_possibles, nb_aretes)

    with open(fichier_sortie, mode="w", newline="") as fichier_csv:
        writer = csv.writer(fichier_csv)
        writer.writerow(["client_i", "client_j", "distance_jour_moyen"])
        for i, j in aretes_selectionnees:
            distance = random.randint(1, 6)
            writer.writerow([i, j, distance])

    print(f"✅ Fichier '{fichier_sortie}' généré avec {nb_aretes} arêtes.")


def lire_contacts_csv(fichier_entree="contacts.csv"):
    """
    Lit le fichier CSV des contacts et le convertit en une liste de listes [i, j, n].
    """
    aretes = []
    with open(fichier_entree, mode="r") as fichier_csv:
        reader = csv.reader(fichier_csv)
        next(reader)  # sauter l'en-tête
        for ligne in reader:
            # convertir les valeurs en int
            i, j, n = int(ligne[0]), int(ligne[1]), int(ligne[2])
            aretes.append([i, j, n])
    return aretes
