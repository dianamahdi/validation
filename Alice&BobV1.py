from Algorithms import bfs
from Semantic import Semantic
from Semantic2RG import SemanticToRG
from traceur import Traceur


class AliceBobCoordinator(Semantic):
    def __init__(self):
        super().__init__()
        self.aliceFlag = 0
        self.bobFlag = 0

    def initial(self):
        return [("Alice_initial", "Bob_initial")]


    def actions(self, current_state):
        potential_actions = []
        state_of_alice, state_of_bob = current_state

        #Alice actions
        if state_of_alice == "Alice_initial":
            potential_actions.append(lambda state: [("Alice_waiting", state[1])])
        elif state_of_alice == "Alice_waiting" and state_of_bob != "Bob_critical":
            potential_actions.append(lambda state: [("Alice_critical", state[1])])
        elif state_of_alice == "Alice_critical":
            potential_actions.append(lambda state: [("Alice_initial", state[1])])

        #Bob actions
        if state_of_bob == "Bob_initial":
            potential_actions.append(lambda state: [(state[0], "Bob_waiting")])
        elif state_of_bob == "Bob_waiting" and state_of_alice != "Alice_critical":
            potential_actions.append(lambda state: [(state[0], "Bob_critical")])
        elif state_of_bob == "Bob_critical":
            potential_actions.append(lambda state: [(state[0], "Bob_initial")])

        print(f"Current State: {current_state}, Potential Actions: {potential_actions}")
        return potential_actions


    def execute(self, action, current_state):
        # Note that the lambda now takes the state as an argument
        return action(current_state)


if __name__ == '__main__':
    coordinator = AliceBobCoordinator()
    rg = SemanticToRG(coordinator)
    traceur = Traceur(rg)
    # w = witness
    w, k = bfs(traceur, lambda n: n[0] == "Alice_critical" and n[1] == "Bob_critical")
    trace = traceur.get_trace(w)
    print(trace)
