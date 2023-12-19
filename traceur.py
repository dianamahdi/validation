class Traceur():
    def __init__(self, rg):
        self.operande = rg
        self.parents={}

    def get_roots(self):
        roots = self.operande.get_roots()
        for r in roots :
            self.parents[r] = []
        return roots

    def get_neighbors(self, node):
        neighbors = self.operande.get_neighbors(node)
        for n in neighbors :
            if n not in self.parents :
                self.parents[n] = [node]
        return neighbors

    def get_trace(self, node):
        trace = []
        current = node
        while current is not None:
            trace.append(current)
            current = self.parents.get(current)
        return trace[::-1]






