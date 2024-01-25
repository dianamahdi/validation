from SoupLanguage import SoupConfiguration
from SoupLanguage import SoupSpec
from SoupLanguage import SoupSemantics
from Algorithms import bfs2
from SoupLanguage import Piece
from Semantic2RG import SemanticToRG
from ParentTraceur import ParentTraceur
from random import shuffle

class AliceBobConfig(SoupConfiguration):
    def __init__(self):
        self.state_Alice = 0
        self.state_Bob = 0

    def __hash__(self):
        return hash(self.state_Alice + self.state_Bob)

    def __eq__(self, other):
        return self.state_Alice == other.state_Alice and self.state_Bob == other.state_Bob

    def __str__(self):
        return f"Alice: {self.state_Alice} Bob: {self.state_Bob}"

if __name__ == '__main__':

    def perform_action(x, op):
        if op == 0:
            x.state_Alice = (x.state_Alice + 1) % 3
            return x
        else:
            x.state_Bob = (x.state_Bob + 1) % 3
            return x

    p1 = Piece("Alice veux entrer", lambda x: True, lambda x: perform_action(x, 0))
    p2 = Piece("Alice entre", lambda x: True, lambda x: perform_action(x, 0))
    p3 = Piece("Alice sort", lambda x: True, lambda x: perform_action(x, 0))
    p1 = Piece("Bob veux entrer", lambda x: True, lambda x: perform_action(x, 1))
    p2 = Piece("Bob entre", lambda x: True, lambda x: perform_action(x, 1))
    p3 = Piece("Bob sort", lambda x: True, lambda x: perform_action(x, 1))

    L = [p1, p2, p3, p1, p2, p3]
    shuffle(L)

    initials = [AliceBobConfig()]
    soup = SoupSpec(initials, L)
    soupSem = SoupSemantics(soup)
    s = SemanticToRG(soupSem)
    p = ParentTraceur(s)
    R = bfs2(p, lambda n: n.state_Bob == 4)

    print("Chemin BFS")
    print()
    for i in R[1]:
        print(i)
    print("Trace")
    print()

    p.ParentTraceurAliceBobSoup(R[0])

