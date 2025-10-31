---

## 📝 **README.md**

```markdown
# 📡 Projet 1 : Simulation de Réseau de Contacts entre Clients

## 👥 Membres du groupe
| Nom complet | Rôle |
|--------------|------|
| MELONG TSAYEM Joan Mathias | ISI-2022-XXX | Chef de projet / Développeur principal |
| BIANGO AFANA G Miguel | ISI-2022-XXX | Développeur Python |
| ZOA EVINA Alexandre Roslyn | ISI-2022-XXX | Analyste & Testeuse |

---

## 🧩 Description du projet

Ce projet consiste à **modéliser un réseau de contacts** entre 250 clients sous forme de graphe non orienté.  
Chaque **arête** représente une relation entre deux clients et contient :
- `i` : identifiant du client 1  
- `j` : identifiant du client 2  
- `n` : nombre moyen de jours avant leur rencontre (1 ≤ n ≤ 6)

À partir de ce graphe, le programme permet de :
1. Générer un fichier `contacts.csv` contenant toutes les arêtes,  
2. Convertir ce fichier en liste Python d’arêtes,  
3. Calculer le **degré** de chaque client et afficher sa distribution,  
4. Simuler une **campagne de diffusion** :
   - en partant du sommet de degré le plus élevé (4 jours),
   - en partant du sommet de plus faible proximité (3 jours).

---

## 📁 Structure du projet

```

📂 projet_reseau_contacts/
│
├── graph_utils.py       # Fonctions principales (génération, lecture, calculs, simulation)
├── main.py              # Point d’entrée principal du projet
├── contacts.csv         # Fichier généré contenant le graphe
└── README.md            # Documentation du projet

````

---

## ⚙️ Prérequis

Avant de lancer le projet, assurez-vous d’avoir :
- **Python 3.8+** installé  
- Les bibliothèques suivantes :
  ```bash
  pip install matplotlib
````

---

## 🧠 Compilation et exécution

### 1️⃣ Cloner le projet (ou copier les fichiers dans un dossier)

```bash
git clone https://github.com/jojo-math/ISI4177_RechercheOperationnelle_projet1
cd projet_reseau_contacts
```

### 2️⃣ Exécuter le projet principal

```bash
python main.py
```

Le programme :

* génère automatiquement le fichier `contacts.csv`,
* calcule les degrés,
* affiche l’histogramme de distribution,
* et exécute les simulations de propagation.

### 3️⃣ Exemple de sortie console

```
✅ Fichier 'contacts.csv' généré avec 3112 arêtes.
🚀 Sommet de départ : 127 (degré = 22)
✅ Sommets atteints après 4 jours : 163 sur 250

📉 Sommet de plus faible proximité : 88 (valeur = 0.00245)
✅ Sommets atteints après 3 jours : 41 sur 250
```

---

## 🧪 Tests

Pour tester chaque fonctionnalité séparément :

### 🔹 Génération du graphe

```python
from graph_utils import generer_contacts_csv
generer_contacts_csv(nb_clients=250, taux_connexion=0.1)
```

### 🔹 Lecture et conversion

```python
from graph_utils import lire_contacts_csv
aretes = lire_contacts_csv("contacts.csv")
print(aretes[:5])
```

### 🔹 Degrés et histogramme

```python
from graph_utils import calculer_degres
calculer_degres(aretes)
```

### 🔹 Simulation de campagne

```python
from graph_utils import sommets_atteints_en_4_jours, sommets_atteints_depuis_proximite_min

sommets_atteints_en_4_jours(aretes, nb_clients=250, nb_jours=4)
sommets_atteints_depuis_proximite_min(aretes, nb_clients=250, nb_jours=3)
```

---

## 📊 Résultats attendus

Le programme produit :

* Un fichier `contacts.csv` (le graphe généré),
* Un histogramme montrant la distribution des degrés,
* Un affichage console du nombre de sommets atteints selon deux stratégies de départ.

---

## 🧩 Auteurs et encadrement

* **Projet académique IUSJC (Institut Universitaire Saint-Jean du Cameroun)**
  Filière : *Informatique & Systèmes d’Information (ISI)*
  Niveau : *4*
  Encadré par : *M. Paulin MELATAGIA YONTA*
  Année académique : 2025–2026

---

## 📜 Licence

Projet à usage académique uniquement.

---

```
