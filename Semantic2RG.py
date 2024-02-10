from RootedGraph import RootedGraph


class SemanticToRG(RootedGraph):

    def __init__(self, semantics):
        self.operand = semantics

    def roots(self):
        return self.operand.initial()

    def neighbors(self, node):
        neighbors = []  # Initialisation de la liste des voisins
        actions = self.operand.actions(node)
        for a in actions:
            neighbors.extend(self.operand.execute(a, node))
        return neighbors  # Retourne  la liste des voisins












