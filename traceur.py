from RootedGraph import RootedGraph


class Traceur(RootedGraph):
    def __init__(self, rg):
        self.operande = rg
        self.parents = {}

    def roots(self):
        roots = self.operande.roots()
        for r in roots:
            self.parents[r] = []
        return roots

    def neighbors(self, node):
        neighbors = self.operande.neighbors(node)
        for n in neighbors:
            if n not in self.parents:
                self.parents[n] = [node]
        return neighbors

    def get_trace(self, node):
        trace = []
        current = node
        while current is not None:
            trace.append(current)
            parents = self.parents.get(current)
            if len(parents) > 0:
                current = parents[0]
            else:
                current = None
        return trace[::-1]






