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
    def __init__(self, initialConfigs: List[SoupConfiguration], pieces: List[Piece]):
            self.configs = initialConfigs
            self.pieces = pieces

    def enabledPieces(self, config: SoupConfiguration) -> List[Piece]:
            return list(filter(lambda p: p.enabled(config), self.pieces))


class SoupSemantics(Semantic):
    def __init__(self, spec):
        super().__init__()
        self.spec = spec

    def initial(self):
        return self.spec.initial()

    def actions(self, config: SoupConfiguration):
        self.spec.enabledPieces(config)

    def execute(self, action, config):
        return action.execute(config)


class OBCConfig(SoupConfiguration):
    def __init__(self, init_clock: int):
        self.clock = init_clock

    def __hash__(self):
        return hash(self.clock)

    def __repr__(self):
        return f"OBCConfig(clock={self.clock})"


if __name__ == "__main__":
    p1 = Piece("p1", lambda x: 1 != 0, lambda x: print("p1"))
    p2 = Piece("p2", lambda x: 1 != 0, lambda x: print("p2"))
    soup = SoupSpec([OBCConfig(0)], [p1, p2])
    soup_sem = SoupSemantics(soup)
    s = SemanticToRG(soup_sem)










