from souplang import *
from algorithms import *
from kernel import *
import inspect


class aliceBobConfig:
    def __init__(self):
        self.alice_pc = 0
        self.bob_pc = 0
        self.alice_flag = False
        self.bob_flag = False

    def __hash__(self):
        return int(hash(self.alice_pc + self.bob_pc + self.alice_flag + self.bob_flag))

    def __eq__(self, other):
        return self.alice_pc == other.alice_pc & self.bob_pc == other.bob_pc & self.alice_flag == other.alice_flag & self.bob_flag == other.bob_flag

    def __repr__(self):
        return str(self.alice_pc) + " " + str(self.bob_pc) + " " + str(self.alice_flag) + " " + str(self.bob_flag)


def aliceBob():
    instanceConfCount = aliceBobConfig()
    soup = Behavior_Soup(instanceConfCount)

    def aliceToWait(c):
        c.alice_pc = 1
        c.alice_flag = True

    soup.add("aliceToWait", lambda c: c.alice_pc == 0, aliceToWait)

    def bobToWait(c):
        c.bob_pc = 1
        c.bob_flag = True

    soup.add("bobToWait", lambda c: c.bob_pc == 0, bobToWait)


    def aliceWaitToSc(c):
        c.alice_pc = 2

    soup.add("aliceWaitToSc", lambda c: c.alice_pc == 1 and not c.bob_flag, aliceWaitToSc)

    def bobWaitToSc(c):
        c.bob_pc = 2

    soup.add("bobWaitToSc", lambda c: c.bob_pc == 1 and not c.alice_flag, bobWaitToSc)

    def aliceScToInit(c):
        c.alice_pc = 0
        c.alice_flag = False

    soup.add("aliceScToInit", lambda c: c.alice_pc == 2, aliceScToInit)

    def bobScToInit(c):
        c.bob_pc = 0
        c.bob_flag = False

    soup.add("bobScToInit", lambda c: c.bob_pc == 2, bobScToInit)


    return soup


if __name__ == "__main__":
    semantics = BehSoupSemantics(aliceBob())
    print(semantics.initial())

    # r = bfs(STR2TR(semantics))
    # print("States: ", r)

    predicate_model_checker(semantics, lambda c: c.bob_pc == 0)

    print("Deadlock Test: ", end=" ")
    predicate_model_checker(semantics, lambda c: len(semantics.actions(c)) == 0 )
    print("Critical section Test: ", end=" ")
    predicate_model_checker(semantics, lambda c: c.alice_pc == 2 and c.bob_pc == 2 )