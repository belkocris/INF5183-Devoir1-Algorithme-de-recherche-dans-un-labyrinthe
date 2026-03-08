import random
from collections import deque

class Maze:
    def __init__(self, size=16, seed=None):
        self.size = size
        self.seed = seed
        if seed is not None:
            random.seed(seed)

        self.grid = [['#' for _ in range(size)] for _ in range(size)]
        self.start = (1, 1)
        self.goal = (size - 2, size - 2)

        self.generate()

    # ---------------------------------------------------------
    # Génération du labyrinthe
    # ---------------------------------------------------------
    def generate(self):
        size = self.size

        # 1. Bords = murs (déjà faits dans __init__)
        # 2. Intérieur = murs aléatoires
        for i in range(1, size - 1):
            for j in range(1, size - 1):
                self.grid[i][j] = '.' if random.random() > 0.30 else '#'

        # 3. Placer S et G
        sx, sy = self.start
        gx, gy = self.goal
        self.grid[sx][sy] = 'S'
        self.grid[gx][gy] = 'G'

        # 4. Garantir qu’un chemin existe
        while not self._path_exists():
            self._regenerate_interior()

    # ---------------------------------------------------------
    # Regénère uniquement l’intérieur si aucun chemin n’existe
    # ---------------------------------------------------------
    def _regenerate_interior(self):
        for i in range(1, self.size - 1):
            for j in range(1, self.size - 1):
                if (i, j) not in [self.start, self.goal]:
                    self.grid[i][j] = '.' if random.random() > 0.30 else '#'

    # ---------------------------------------------------------
    # Vérifie l’existence d’un chemin via BFS
    # ---------------------------------------------------------
    def _path_exists(self):
        queue = deque([self.start])
        visited = set([self.start])

        while queue:
            x, y = queue.popleft()
            if (x, y) == self.goal:
                return True

            for nx, ny in self.get_neighbors((x, y)):
                if (nx, ny) not in visited and self.grid[nx][ny] != '#':
                    visited.add((nx, ny))
                    queue.append((nx, ny))

        return False

    # ---------------------------------------------------------
    # Renvoie les voisins valides (haut, bas, gauche, droite)
    # ---------------------------------------------------------
    def get_neighbors(self, pos):
        x, y = pos
        moves = [
            (x, y + 1),  # droite
            (x + 1, y),  # bas
            (x, y - 1),  # gauche
            (x - 1, y)   # haut
        ]

        valid = []
        for nx, ny in moves:
            if 0 <= nx < self.size and 0 <= ny < self.size:
                valid.append((nx, ny))
        return valid

    # ---------------------------------------------------------
    # Affichage du labyrinthe
    # ---------------------------------------------------------
    def display(self):
        for row in self.grid:
            print(" ".join(row))

    # ---------------------------------------------------------
    # Marquer une exploration (p) ou un chemin (*)
    # ---------------------------------------------------------
    def mark_path(self, path, symbol='*'):
        for (x, y) in path:
            if self.grid[x][y] not in ['S', 'G']:
                self.grid[x][y] = symbol

    def mark_explored(self, explored):
        for (x, y) in explored:
            if self.grid[x][y] not in ['S', 'G']:
                self.grid[x][y] = 'p'
