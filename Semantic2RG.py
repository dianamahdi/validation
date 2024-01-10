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

# def initial(self):
    #    return self.semantics.initial

    #def actions(self,c):
     #   return self.operand.actions(c)

    #def execute(self,c,a):
     #   target = self.operand.execute(c, a)
      #  return target



#from rootedgraph import RootedGraph
#class SemanticToGraph(RootedGraph):
    #def __init__(self, semanticModel):
        #self.semanticModel = semanticModel

    #def find_roots(self):
        # Get the initial state from the semantic model
        #initial_states = self.semanticModel.initial()
        #return initial_states

    #def find_adjacent_nodes(self, node):
        # Retrieve possible actions for the current node
        #possible_actions = self.semanticModel.actions(node)
        #adjacent_nodes = []
        #for action in possible_actions:
            #next_states = self.semanticModel.execute(action, node)
            #adjacent_nodes.extend(next_states)
        #return adjacent_nodes







