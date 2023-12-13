from collections import deque
from abc import ABC, abstractmethod

class RootedGraph:
    def __init__(self, graph_dict, roots):
        self.graph = graph_dict
        self.roots = roots

    def get_roots(self):
        return self.roots

    def get_neighbors(self, node):
        return self.graph.get(node, [])

class DRootedGraph(RootedGraph, ABC):
    def __init__(self, graph_dict, roots):
        super().__init__(graph_dict, roots)

    @abstractmethod
    def bfs_search(self, query):
        # La méthode bfs_search doit être implémentée par des sous-classes concrètes
        pass

# Implémentation concrète de DRootedGraph avec la méthode bfs_search
class ConcreteDRootedGraph(DRootedGraph):
    def bfs_search(self, query):
        frontier = deque(self.get_roots())  # File d'attente des nœuds à visiter
        visited = set()  # Ensemble des nœuds déjà visités
        while frontier:
            current = frontier.popleft()
            if query(current):
                return current  # Retourne le nœud si la condition de recherche est remplie
            visited.add(current)
            for neighbor in self.get_neighbors(current):
                if neighbor not in visited and neighbor not in frontier:
                    frontier.append(neighbor)
        return None  # Si aucun nœud ne satisfait la condition, retourne None

# Utilisation de la classe ConcreteDRootedGraph
graph = {1: [2, 3], 2: [3, 4], 3: [], 4: []}
roots = [1]
query = lambda x: x == 3  # Exemple de fonction lambda qui cherche le nœud avec la valeur 5

graph_obj = ConcreteDRootedGraph(graph, roots)
found_node = graph_obj.bfs_search(query)
if found_node:
    print(f"Nœud trouvé : {found_node}")
else:
    print("Aucun nœud ne satisfait la condition de recherche.")
