#Main au-dessous de chaque fichier pour tester chaque fichier seul !
#Ce main etait juste pour le debut!

#Ce code met en œuvre une classe SimpleGraph pour représenter un graphe non orienté.
#Un graphe non orienté est constitué de nœuds (ou sommets) et d'arêtes qui relient ces nœuds.
#La classe offre une méthode de parcours en largeur (bfs pour "Breadth-First Search"),
#qui visite tous les nœuds du graphe à partir d'un nœud de départ donné.


from collections import deque

class SimpleGraph:
    def __init__(self):
        # Initialise un dictionnaire pour représenter le graphe où les clés sont les nœuds et les valeurs sont les listes de voisins.
        self.graph = {}

    def add_edge(self, node1, node2):
        # Ajoute une arête entre deux nœuds en ajoutant les nœuds à la liste des voisins l'un de l'autre.
        self._add_edge(node1, node2)
        self._add_edge(node2, node1)

    def _add_edge(self, node1, node2):
        # Fonction auxiliaire pour ajouter une arête entre deux nœuds.
        # Si le nœud existe déjà, ajoute le nœud voisin à sa liste de voisins, sinon crée une nouvelle entrée.
        if node1 in self.graph:
            self.graph[node1].append(node2)
        else:
            self.graph[node1] = [node2]

    def bfs(self, start):
        # Parcours en largeur du graphe à partir du nœud de départ.
        visited = set()  # Ensemble pour suivre les nœuds déjà visités.
        queue = deque([start])  # Utilise une file pour suivre les nœuds à visiter.
        visited.add(start)

        while queue:
            current_node = queue.popleft()  # Prend le premier nœud de la file.
            print(current_node)  # Affiche le nœud visité. Tu peux adapter cette partie selon tes besoins.

            # Parcourt tous les voisins du nœud actuel.
            for neighbor in self.graph.get(current_node, []):
                if neighbor not in visited:
                    # Ajoute les voisins non visités à la file et les marque comme visités.
                    queue.append(neighbor)
                    visited.add(neighbor)

# Exemple d'utilisation
graph = SimpleGraph()
graph.add_edge('A', 'B')
graph.add_edge('B', 'C')
graph.add_edge('C', 'A')
graph.add_edge('B', 'D')
graph.add_edge('D', 'E')

graph.bfs('A')
