from Algorithms import bfs
class HanoiConfig:
    def __init__(self, num_disks):
        self.num_disks = num_disks
        # Utilisation de listes au lieu de tuples pour représenter les tours
        self.start_state = [list(range(num_disks, 0, -1)), [], []]
        self.end_state = [[], [], list(range(num_disks, 0, -1))]

class HanoiRootedGraph(HanoiConfig):
    def __init__(self, num_disks):
        super().__init__(num_disks)

    def get_neighbors(self, config):
        neighbors = []
        for i, start_tower in enumerate(config):
            if start_tower:  # Check if there is at least one disk on the tower
                for j, end_tower in enumerate(config):
                    if i != j and (not end_tower or start_tower[-1] < end_tower[-1]):
                        # Effectuer une copie profonde pour créer un nouvel état
                        new_config = [tower[:] for tower in config]
                        disk = new_config[i].pop()  # Retirer le disque du sommet de la tour de départ
                        new_config[j].append(disk)  # Ajouter le disque au sommet de la tour d'arrivée
                        neighbors.append(new_config)
        return neighbors

class GraphSearcher:
    def __init__(self, hanoi_graph):
        self.hanoi_graph = hanoi_graph
        self.roots = hanoi_graph.start_state

    def bfs(self, query):
        return bfs(self.hanoi_graph, query)

    def get_roots(self):
        return self.roots

    def get_neighbors(self, node):
        return self.graph.get_neighbors(node)

# Utilisation des classes
num_disks = 3
hanoi_graph = HanoiRootedGraph(num_disks)
toto = GraphSearcher(hanoi_graph)

is_solution = lambda state: state == hanoi_graph.end_state
solution = toto.bfs(is_solution)
if solution:
    print(f"Found solution in {len(solution) - 1} moves:")
    for step in solution:
        print(step)
else:
    print("No solution found.")



