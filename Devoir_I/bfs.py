import time
from collections import deque

class BFS:
    def __init__(self, maze):
        self.maze = maze
        self.start = maze.start
        self.goal = maze.goal

    # ---------------------------------------------------------
    # BFS avec file FIFO
    # ---------------------------------------------------------
    def search(self):
        start_time = time.perf_counter()

        queue = deque([self.start])       # file FIFO
        visited = set([self.start])       # ensemble des noeuds visités
        parent = {self.start: None}       # pour reconstruire le chemin

        explored_order = []               # pour marquer les 'p'

        while queue:
            current = queue.popleft()
            explored_order.append(current)

            if current == self.goal:
                break

            for neighbor in self.maze.get_neighbors(current):
                x, y = neighbor
                if neighbor not in visited and self.maze.grid[x][y] != '#':
                    visited.add(neighbor)
                    parent[neighbor] = current
                    queue.append(neighbor)

        # Reconstruction du chemin
        path = self._reconstruct_path(parent)

        exec_time = (time.perf_counter() - start_time) * 1000  # ms

        return {
            "path": path,
            "explored": explored_order,
            "nodes_explored": len(explored_order),
            "path_length": len(path),
            "time_ms": exec_time
        }

    # ---------------------------------------------------------
    # Reconstruit le chemin depuis parent[]
    # ---------------------------------------------------------
    def _reconstruct_path(self, parent):
        path = []
        node = self.goal

        if node not in parent:
            return []  # aucun chemin trouvé (ne devrait pas arriver)

        while node is not None:
            path.append(node)
            node = parent[node]

        return list(reversed(path))
