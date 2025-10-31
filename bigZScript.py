"""
Ici on va faire la question 2,3,4 de la première partie


on modélise le graphe dans un tableau l'ensemble des arêtes.
un arête est un tableau à trois colomnes( sommets de départ, sommets d'arrivée  et le poids de l'arête)
"""
"""
Tab est un tableau contenant la liste des sommets et de leur degre
"""

def ListCinqPlus(Tab):
    T=[]
    for i in range(0, len(Tab)):
        T.append([i,Tab[i]])
    T = sorted(T, key=lambda x: x[1] , reverse=True)
    print("Les cinqs clients ayant les plus grand degré")
    for i in range(0, 5):
        print(f"Client {i} → degré = {T[i]}")
        
"""
    Tab contient l'ensemble des arêtes
"""


def ListSommetDistanceproxi(Tab):
    R={}
    for i in range(0, 255):
        R[i]=0
    for s1, s2, poids in Tab:
       R[s1] += poids
       R[s2] += poids
    return R;


