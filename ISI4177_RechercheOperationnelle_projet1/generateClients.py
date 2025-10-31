# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 10:10:29 2025

@author: Home
"""


import csv
import random
from itertools import combinations

# --- Paramètres du graphe ---
NB_CLIENTS = 250
TAUX_CONNEXION = 0.5  # 50% des paires seront reliées (modifiable)
FICHIER_SORTIE = "contacts.csv"

# --- Génération des paires (i, j) uniques ---
# combinations(range(NB_CLIENTS), 2) génère (0,1), (0,2), ..., (1,2), etc.
paires_possibles = list(combinations(range(NB_CLIENTS), 2))

# Nombre d'arêtes à générer selon le taux de connexion
nb_aretes = int(len(paires_possibles) * TAUX_CONNEXION)

# Sélection aléatoire d'un sous-ensemble de paires
aretes_selectionnees = random.sample(paires_possibles, nb_aretes)

# --- Écriture dans le fichier CSV ---
with open(FICHIER_SORTIE, mode="w", newline="") as fichier_csv:
    writer = csv.writer(fichier_csv)
    writer.writerow(["client_i", "client_j", "distance_jour_moyen"])  # en-tête

    for i, j in aretes_selectionnees:
        distance = random.randint(1, 6)  # distance entre 1 et 6 jours
        writer.writerow([i, j, distance])

print(f"✅ Fichier '{FICHIER_SORTIE}' généré avec {nb_aretes} arêtes pour {NB_CLIENTS} clients.")
