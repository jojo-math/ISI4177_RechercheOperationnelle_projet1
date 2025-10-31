import networkx as nx
import pandas as pd

def count_touched_after_days(filename='graphe_contacts.csv', days=5):

    #chargement du fichier CSV
    df = pd.read_csv(filename, header=None, names=['i', 'j', 'n'])

    #Construction du graphe
    G = nx.Graph()
    G.add_edges_from(df[['i', 'j']].values)

    #Calcul des proximites
    proximites = {}
    for v in G.nodes():
        lengths = nx.shortest_path_length(G, v)
        proximites[v] = sum(lengths.values())

    #Sommet de proximite le plus bas (plus grande somme, peripherique)
    starting = max(proximites, key=proximites.get)

    #Distances depuis le starting
    dist = nx.shortest_path_length(G, starting)

    #Nombre de sommets a distance <= 5
    touched = sum(1 for d in dist.values() if d <= days)
    print(f"Nombre de sommets touchés après {days} jours :", touched)
    return touched