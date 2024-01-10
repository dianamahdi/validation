from typing import List
from Semantic import Semantic
from Semantic2RG import SemanticToRG

class SoupConfiguration:
    def __hash__(self) -> int:
        pass

    def __eq__(self, other: object) -> bool:
        pass

    def __repr__(self) -> str:
        pass


class Piece:
    def __init__(self, name, guard, action):
        self.name = name
        self.guard = guard
        self.action = action

    def enabled(self, config):
        return self.guard(config)

    def execute(self, config):
        return [self.action(config)]


class SoupSpec:
    def initial(self) -> List[SoupConfiguration]:
        return []

    def pieces(self) -> List[Piece]:
        return []

    def enabledPieces(self, config: SoupConfiguration) -> List[Piece]:
        return list(filter(lambda p: p.enabled(config), self.pieces()))


class SoupSemantics(Semantic):
    def __init__(self, spec):
        super().__init__()
        self.spec = spec

    def initial(self):
        return self.spec.initial()

    #a continuer










