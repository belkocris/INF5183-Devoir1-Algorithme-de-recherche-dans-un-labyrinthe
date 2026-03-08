import time
import heapq

class AStar:
    def __init__(self, maze):
        self.maze = maze
        self.start = maze.start
        self.goal = maze.goal

    # ---------------------------------------------------------
    # Heuristique : distance de Manhattan
    # ---------------------------------------------------------
    def heuristic(self, node):
        x, y = node
        gx, gy = self.goal
        return abs(x - gx) + abs(y - gy)

    # ---------------------------------------------------------
    # A* avec file de priorité
    # ---------------------------------------------------------
    def search(self):
        start_time = time.perf_counter()

        # file de priorité : (f(n), g(n), node)
        open_list = []
        heapq.heappush(open_list, (0, 0, self.start))

        g_cost = {self.start: 0}
        parent = {self.start: None}

        explored_order = []
        visited = set()

        while open_list:
            f, g, current = heapq.heappop(open_list)

            if current in visited:
                continue
            visited.add(current)
            explored_order.append(current)

            if current == self.goal:
                break

            for neighbor in self.maze.get_neighbors(current):
                x, y = neighbor
                if self.maze.grid[x][y] == '#':
                    continue

                tentative_g = g_cost[current] + 1

                if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                    g_cost[neighbor] = tentative_g
                    f_cost = tentative_g + self.heuristic(neighbor)
                    parent[neighbor] = current
                    heapq.heappush(open_list, (f_cost, tentative_g, neighbor))

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
            return []

        while node is not None:
            path.append(node)
            node = parent[node]

        return list(reversed(path))
