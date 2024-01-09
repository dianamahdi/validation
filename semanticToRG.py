class OneBitClock(semantics):
    def __init__(self):
        return [0]

    def actions(self,c):
        a=[]
        if c==1:
            a.append(lambda c:[0])
        elif c==0:
            a.append(lambda c:[1])

        def execute(self,a,c):
            return a(c)

class AliceBob(rg):
    def __init__(self):
        self.alice={}
        self.bob={}

        self.


class Semantic_to_RG:

    def __init__(self, semantics):
        self.operand = semantics


    def get_roots(self):
        return self.operand.initial()

    def get_neighbors(self, node):
        neighbors = []  # Initialisation de la liste des voisins
        actions = self.operand.actions(node)
        for a in actions:
            neighbors.extend(self.operand.execute(a, node))
        return neighbors  # Retourne  la liste des voisins

# def initia(self):
    #    return self.semantics.initial

    #def actions(self,c):
     #   return self.operand.actions(c)

    #def execute(self,c,a):
     #   target = self.operand.execute(c, a)
      #  return target
