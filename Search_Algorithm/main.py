from aima.search import GraphProblem, breadth_first_graph_search, astar_search, romania_map

# Cari rute kota dari Arad ke Bucharest (Peta Romania)
problem = GraphProblem('Arad', 'Bucharest', romania_map)

print("=== TES SEARCH ALGORITHMS ===")

# 1. Jalankan BFS
bfs_res = breadth_first_graph_search(problem)
print("\n[BFS] Rute   :", " -> ".join([node.state for node in bfs_res.path()]))
print("[BFS] Cost   :", bfs_res.path_cost)

# 2. Jalankan A* Search
astar_res = astar_search(problem)
print("\n[A* ] Rute   :", " -> ".join([node.state for node in astar_res.path()]))
print("[A* ] Cost   :", astar_res.path_cost)
