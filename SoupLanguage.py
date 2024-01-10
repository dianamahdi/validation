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
        def _init_(self, spec):
            self.spec = spec

        def initial(self):
            return self.spec.initial()




