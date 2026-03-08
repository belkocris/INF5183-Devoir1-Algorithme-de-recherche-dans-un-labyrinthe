from maze import Maze
from dfs import DFS
from bfs import BFS
from astar import AStar

def print_lab(title, maze):
    print("\n" + "="*60)
    print(title)
    print("="*60)
    maze.display()
    print()

def print_path(result):
    print("Chemin :", " -> ".join([f"({x},{y})" for x, y in result["path"]]))
    print("Noeuds explorés :", result["nodes_explored"])
    print("Longueur du chemin :", result["path_length"])
    print(f"Temps (ms) : {result['time_ms']:.3f}")
    print()

def reset_marks(maze):
    for i in range(maze.size):
        for j in range(maze.size):
            if maze.grid[i][j] in ['p', '*']:
                maze.grid[i][j] = '.'
    sx, sy = maze.start
    gx, gy = maze.goal
    maze.grid[sx][sy] = 'S'
    maze.grid[gx][gy] = 'G'

def main():
    # ---------------------------------------------------------
    # Génération du labyrinthe
    # ---------------------------------------------------------
    maze = Maze(seed=42)

    print_lab("Labyrinthe généré", maze)

    results = {}

    # ---------------------------------------------------------
    # BFS
    # ---------------------------------------------------------
    reset_marks(maze)
    bfs = BFS(maze)
    res_bfs = bfs.search()
    results["BFS"] = res_bfs

    maze.mark_explored(res_bfs["explored"])
    maze.mark_path(res_bfs["path"], symbol='*')

    print_lab("Exploration BFS", maze)
    print_path(res_bfs)

    # ---------------------------------------------------------
    # DFS
    # ---------------------------------------------------------
    dfs = DFS(maze)
    res_dfs = dfs.search()
    results["DFS"] = res_dfs

    reset_marks(maze)
    maze.mark_explored(res_dfs["explored"])
    maze.mark_path(res_dfs["path"], symbol='*')

    print_lab("Exploration DFS", maze)
    print_path(res_dfs)

    # ---------------------------------------------------------
    # A*
    # ---------------------------------------------------------
    reset_marks(maze)
    astar = AStar(maze)
    res_astar = astar.search()
    results["A* (Manhattan)"] = res_astar

    maze.mark_explored(res_astar["explored"])
    maze.mark_path(res_astar["path"], symbol='*')

    print_lab("Exploration A*", maze)
    print_path(res_astar)

    # ---------------------------------------------------------
    # Tableau comparatif final
    # ---------------------------------------------------------
    print("\n" + "="*60)
    print("TABLEAU COMPARATIF")
    print("="*60)
    print(f"{'ALGORITHME':<20} {'NOEUDS':<10} {'LONGUEUR':<12} {'TEMPS (ms)':<12}")
    print("-"*60)

    for name, r in results.items():
        print(f"{name:<20} {r['nodes_explored']:<10} {r['path_length']:<12} {r['time_ms']:.3f}")

    print("="*60)

if __name__ == "__main__":
    main()