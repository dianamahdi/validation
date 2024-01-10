from souplang import *
from algorithms import *
from kernel import *
import inspect


class aliceBobConfig:
    def __init__(self):
        self.apc = 0
        self.bpc = 0

    def __hash__(self):
        return int(hash(self.apc + self.bpc))

    def __eq__(self, other):
        return self.apc == other.apc & self.bpc == other.bpc

    def __repr__(self):
        return str(self.apc) + str(self.bpc)


def aliceBob():
    instanceConfCount = aliceBobConfig()
    soup = Behavior_Soup(instanceConfCount)


    def aToSc(c):
        c.apc = 1

    soup.add("aToSc", lambda c: c.apc == 0, aToSc)

    def bToSc(c):
        c.bpc = 1

    soup.add("bToSc", lambda c: c.bpc == 0, bToSc)


    def aToInit(c):
        c.apc = 0

    soup.add("aToInit", lambda c: c.apc == 1, aToInit)

    def bToInit(c):
        c.bpc = 0

    soup.add("bToInit", lambda c: c.bpc == 1, bToInit)


    return soup