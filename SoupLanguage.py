from Semantic import *
import copy


class SoupConfiguration:
    def _hash_(self) -> int:
        pass

    def _eq_(self, __value: object) -> bool:
        pass

    def _repr_(self) -> str:
        pass

    class Piece:
        def _init_(self, name, guard, action):
            self.name = name
            self.guard = guard
            self.action = action

        def execute(self, config):
            return [self.action(config)]

    class SoupSemantics(Semantic):
        def __init__(self, program):
            self.spec = program

        def initial(self):
            return [self.spec.initial]

        def actions(self, conf):
            return list(map(lambda b: b.action,
                            filter(lambda b: b.guard(conf),
                                   self.spec.behaviors)))

        def execute(self, c, a):
            target = copy.deepcopy(c)
            r = a(target)
            return target

