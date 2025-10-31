# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 10:12:50 2025

@author: Home
"""

from graph_utils import generer_contacts_csv, lire_contacts_csv

def main():
    # Étape 1 : Générer le fichier CSV
    generer_contacts_csv(nb_clients=250, taux_connexion=0.5, fichier_sortie="contacts.csv")

    # Étape 2 : Lire le CSV et le convertir en liste Python
    aretes = lire_contacts_csv("contacts.csv")

    # Étape 3 : Exploiter les données
    print(f"\nNombre total d'arêtes lues : {len(aretes)}")
    print("Aperçu des 5 premières arêtes :")
    for edge in aretes[:5]:
        print(edge)

if __name__ == "__main__":
    main()
