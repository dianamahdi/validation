from RootedGraph import RootedGraph


class ParentTraceur(RootedGraph):
    def __init__(self, rg, parents=None):
        self.rg = rg  # operand
        self.parents = {}

    def getRoots(self):
        uroots = self.rg.getRoots()
        for n in uroots:
            self.parents[n] = []
        return uroots

    def getNeighbors(self, n):
        uneighbors = self.rg.getNeighbors(n)
        for node in uneighbors:
            if self.parents.get(node) is None:
                self.parents[node] = [n]
        return uneighbors

    def ParentTraceurHanoi(self, last):  # get_trace
        print("Trace:\n")
        lap = last
        value = self.parents[last]
        while value is not None and len(value) is not 0:
            print(f"{lap.towers}: {value[0].towers}")

            lap = value[0]
            value = self.parents[lap]

    def ParentTraceurAliceBobV1(self, last):
        print("Trace:\n")
        if last is None:
            print("No trace available.")
            return

        lap = last
        value = self.parents.get(last, None)
        while value is not None and len(value) != 0:
            print(f"{lap}: {value}")
            lap = value[0]
            value = self.parents.get(lap, None)

    def ParentTraceurAliceBobSoup(self, last):
        print("Trace:\n")
        if last is None:
            print("No trace available.")
            return

        lap = last
        value = self.parents.get(last, None)
        while value is not None and len(value) != 0:
            print(f"{lap}: {value[0]}")
            lap = value[0]
            value = self.parents.get(lap, None)






