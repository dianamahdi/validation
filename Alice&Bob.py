from Algorithms import bfs
from Semantic import Semantic
from Semantic2RG import SemanticToRG
from traceur import Traceur


class GardenDilemma(Semantic):
    def __init__(self):
        super().__init__()
        self.stateAlice = 0
        self.stateBob = 0

    def initial(self):
        return [("Alice_start", "Bob_start")]

    def actions(self, current_config):
        possible_actions = []
        stateAlice, stateBob = current_config

        #Alice
        if stateAlice == "Alice_start":
            possible_actions.append(lambda _: [("Alice_waiting", stateBob)])
        elif stateAlice == "Alice_waiting":
            possible_actions.append(lambda _: [("Alice_inCritical", stateBob)])
        elif stateAlice == "Alice_inCritical":
            possible_actions.append(lambda _: [("Alice_start", stateBob)])

        #Bob
        if stateBob == "Bob_start":
            possible_actions.append(lambda _: [(stateAlice, "Bob_waiting")])
        elif stateBob == "Bob_waiting":
            possible_actions.append(lambda _: [(stateAlice, "Bob_inCritical")])
        elif stateBob == "Bob_inCritical":
            possible_actions.append(lambda _: [(stateAlice, "Bob_start")])

        return possible_actions

    def execute(self, action, current_config):
        return action(current_config)


if __name__ == '__main__':
    dilemma = GardenDilemma()
    rg = SemanticToRG(dilemma)
    traceur = Traceur(rg)
    # w = witness
    w, k = bfs(traceur, lambda n: n[0] == "Alice_inCritical" and n[1] == "Bob_inCritical")
    trace = traceur.get_trace(w)
    print(trace)


