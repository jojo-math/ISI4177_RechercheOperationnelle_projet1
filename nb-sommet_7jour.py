import networkx as nx
import pandas as pd

def count_touched_after_7_days(filename='graphe_contacts.csv'):
   
   #chargemet du fichier CSV
    df = pd.read_csv(filename, header=None, names=['i', 'j', 'n'])

    #Construction du graphe
    G = nx.Graph()
    G.add_edges_from(df[['i', 'j']].values)

    #Calcul des proximites
    proximites = {}
    for v in G.nodes():
        lengths = nx.shortest_path_length(G, v)
        proximites[v] = sum(lengths.values())

    #Nombre de sommets ale plus bas (plus grande somme)
    starting = max(proximites, key=proximites.get)

    #Distances depuis le starting
    dist = nx.shortest_path_length(G, starting)

    #Nombre de sommets a distance <= 7
    touched = sum(1 for d in dist.values() if d <= 7)
    print("Nombre de sommets touchés après 7 jours :", touched)
    return touched