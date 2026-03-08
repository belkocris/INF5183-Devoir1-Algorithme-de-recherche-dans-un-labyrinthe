# INF5183 – Fondements de l’Intelligence Artificielle  
## Devoir : Algorithmes de recherche dans un labyrinthe

Ce projet implémente trois algorithmes de recherche classiques (DFS, BFS et A*) afin de trouver un chemin dans un labyrinthe généré aléatoirement.  
L’objectif est de comparer leurs performances en termes de nœuds explorés, longueur du chemin et temps d’exécution.

---

## 📌 Structure du projet
### Devoir_I/
#### │
#### ├── maze.py          # Génération et gestion du labyrinthe
#### ├── dfs.py           # Implémentation de DFS (Depth-First Search)
#### ├── bfs.py           # Implémentation de BFS (Breadth-First Search)
#### ├── astar.py         # Implémentation de A* (heuristique Manhattan)
#### ├── main.py          # Point d’entrée principal
#### ├── requirements.txt # Dépendances (si nécessaire)
#### └── README.md        # Documentation

---

## 🧱 Description du problème

Le labyrinthe est une matrice 16×16 contenant :

- `#` : mur  
- `.` : case libre  
- `S` : point de départ (toujours en position (1,1))  
- `G` : point d’arrivée (toujours en position (14,14))  

Les déplacements autorisés sont : haut, bas, gauche, droite.

Le générateur garantit qu’un chemin existe entre S et G.

---

## 🔍 Algorithmes implémentés

### **1. DFS — Depth-First Search**
- Utilise une pile (LIFO)
- Explore en profondeur
- Peut trouver un chemin long
- Ordre des voisins : droite → bas → gauche → haut

### **2. BFS — Breadth-First Search**
- Utilise une file (FIFO)
- Explore par couches
- Trouve toujours le chemin le plus court (en nombre de pas)

### **3. A\* — A-Star**
- Utilise une file de priorité
- Fonction :  
  

\[
  f(n) = g(n) + h(n)
  \]


- Heuristique : distance de Manhattan  
- Optimal si l’heuristique est admissible (ce qui est le cas ici)

---

## ▶️ Exécution

Lancer le programme avec : python main.py


---

## 📊 Résultats affichés

Pour chaque algorithme :

- Labyrinthe exploré (`p`)
- Chemin trouvé (`*`)
- Liste des coordonnées du chemin
- Nombre de nœuds explorés
- Longueur du chemin
- Temps d’exécution (ms)

## Un tableau comparatif final est généré :

## Algorithme           Noeuds     Longueur     Temps (ms)
## -------------------------------------------------------
## DFS                  78         45           0.521
## BFS                  112        27           0.634
## A* (Manhattan)       45         27           0.312


---

## 🔧 Dépendances

Aucune dépendance externe n’est requise.  
Le projet fonctionne avec **Python 3.11**.

---

## 👨‍💻 Auteur
Travail réalisé par :

- **Christian Belibi Kouoh**

Travail réalisé dans le cadre du cours **INF5183 – Fondements de l’IA**.
