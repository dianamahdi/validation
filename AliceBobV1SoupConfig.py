from SoupLanguage import SoupConfiguration
from SoupLanguage import SoupSpec
from SoupLanguage import SoupSemantics
from Algorithms import bfs2
from SoupLanguage import Piece
from Semantic2RG import SemanticToRG
from ParentTraceur import ParentTraceur
from AliceBobSoupConfig import AliceBobConfig
from random import shuffle


class AliceBobConfV2(SoupConfiguration):
    def __init__(self):
        self.state_Alice = 0
        self.state_Bob = 0
        self.flag_Alice = 0
        self.flag_Bob = 0

    def __hash__(self):
        return hash((self.state_Alice, self.state_Bob, self.flag_Alice, self.flag_Bob))

    def __eq__(self, other):
        return (self.state_Alice == other.state_Alice and
                self.state_Bob == other.state_Bob and
                self.flag_Alice == other.flag_Alice and
                self.flag_Bob == other.flag_Bob)

    def __str__(self):
        return f"Alice: {self.state_Alice} flag Alice: {self.flag_Alice} Bob: {self.state_Bob} flag Bob: {self.flag_Bob}"

if __name__ == '__main__':
        def perform_action(x, op):
            if op == 0:
                if x.state_Alice == 0:
                    x.flag_Alice = 1
                x.state_Alice = (x.state_Alice + 1) % 3
                if x.state_Alice == 0:
                    x.flag_Alice = 0
                return x
            else:
                if x.state_Bob == 0:
                    x.flag_Bob = 1
                x.state_Bob = (x.state_Bob + 1) % 3
                if x.state_Bob == 0:
                    x.flag_Bob = 0
                return x

        p1 = Piece("Alice veux entrer", lambda x: x.state_Alice == 0, lambda x: perform_action(x, 0))
        p2 = Piece("Alice entre", lambda x: x.flag_Bob == 0, lambda x: perform_action(x, 0))
        p3 = Piece("Alice sort", lambda x: x.state_Alice == 2, lambda x: perform_action(x, 0))
        p1 = Piece("Bob veux entrer", lambda x: x.state_Bob == 0, lambda x: perform_action(x, 1))
        p2 = Piece("Bob entre", lambda x: x.flag_Alice == 0, lambda x: perform_action(x, 1))
        p3 = Piece("Bob sort", lambda x: x.state_Bob == 2, lambda x: perform_action(x, 1))

        L = [p1, p2, p3, p1, p2, p3]
        shuffle(L)

        initials = [AliceBobConfig()]
        soup = SoupSpec(initials, L)
        soupSem = SoupSemantics(soup)
        s = SemanticToRG(soupSem)
        p = ParentTraceur(s)

        def query_condition(node):
            return not s.getNeighbors(node)
        R = bfs2(p, query_condition)

        print("chemin BFS")
        print()
        for i in R[1]:
            print(i)
        print("Trace")
        print()

        p.ParentTraceurAliceBobSoup(R[0])


