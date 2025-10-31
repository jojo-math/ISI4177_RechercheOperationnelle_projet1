# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 10:12:50 2025

@author: Home
"""

from graph_utils import generer_contacts_csv, lire_contacts_csv, calculer_degres

def main():
    # Étape 1 : Générer le fichier CSV
    generer_contacts_csv(nb_clients=250, taux_connexion=0.5, fichier_sortie="contacts.csv")

    # Étape 2 : Lire le CSV et le convertir en liste Python
    aretes = lire_contacts_csv("contacts.csv")

    # Étape 3 : Calculer les degrés et afficher la distribution
    degClients = calculer_degres(aretes, nb_clients=250)

    # Étape 4 : Exemple d'affichage textuel
    print(f"\nExemple de degrés pour les 10 premiers clients :")
    for i in range(10):
        print(f"Client {i} → degré = {degClients[i]}")

if __name__ == "__main__":
    main()
