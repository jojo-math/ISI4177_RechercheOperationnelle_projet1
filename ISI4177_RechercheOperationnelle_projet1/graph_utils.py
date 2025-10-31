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
import matplotlib.pyplot as plt
from collections import defaultdict, deque

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


def calculer_degres(aretes, nb_clients=250):
    """
    Calcule le degré de chaque sommet du graphe à partir de la liste des arêtes.
    Affiche ensuite un histogramme de la distribution des degrés.
    Retourne : dict {client_id: degré}
    """
    # Initialisation du dictionnaire de degrés
    degClients = {i: 0 for i in range(nb_clients)}

    # Comptage des degrés
    for i, j, _ in aretes:
        degClients[i] += 1
        degClients[j] += 1  # graphe non orienté → deux sens comptés

    # --- Affichage de l'histogramme ---
    plt.figure(figsize=(12, 5))
    plt.bar(degClients.keys(), degClients.values(), width=0.8)
    plt.title("Distribution des degrés des sommets (clients)")
    plt.xlabel("Identifiant du client")
    plt.ylabel("Degré (nombre de contacts)")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

    return degClients

def sommets_atteints_en_4_jours(aretes, nb_clients=250, nb_jours=4):
    """
    Calcule le nombre total de sommets atteints après nb_jours jours,
    en partant du sommet de degré maximal.
    
    Paramètres :
        aretes : liste des arêtes [i, j, n]
        nb_clients : nombre total de sommets (par défaut 250)
        nb_jours : durée maximale de la propagation (par défaut 4)
    
    Retourne :
        nombre total de sommets atteints
    """
    # --- 1. Construire le graphe sous forme de dictionnaire d'adjacence ---
    graphe = defaultdict(list)
    for i, j, n in aretes:
        graphe[i].append((j, n))
        graphe[j].append((i, n))  # graphe non orienté

    # --- 2. Calculer le degré de chaque sommet ---
    degres = {i: len(graphe[i]) for i in range(nb_clients)}

    # --- 3. Trouver le sommet de degré maximal ---
    sommet_depart = max(degres, key=degres.get)
    print(f"🚀 Sommet de départ : {sommet_depart} (degré = {degres[sommet_depart]})")

    # --- 4. Parcours en largeur (BFS pondéré par les jours) ---
    visites = set([sommet_depart])
    queue = deque([(sommet_depart, 0)])  # (sommet, jours_courants)

    while queue:
        sommet, jour_courant = queue.popleft()
        for voisin, distance in graphe[sommet]:
            nouveau_jour = jour_courant + distance
            if nouveau_jour <= nb_jours and voisin not in visites:
                visites.add(voisin)
                queue.append((voisin, nouveau_jour))

    # --- 5. Résultat ---
    nb_atteints = len(visites)
    print(f"✅ Sommets atteints après {nb_jours} jours : {nb_atteints} sur {nb_clients}")
    return nb_atteints

