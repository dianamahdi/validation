from copy import deepcopy


class SemanticTransition:
    def __init__(self):
        pass

    def initial(self):
        pass

    def actions(self, conf):
        pass

    def execute(self, conf, action):
        pass


class StepSyncComposition(SemanticTransition):
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def initial(self):
        initial = []
        for lhs_state in self.lhs.initial():
            for rhs_state in self.rhs.initial():
                c = (lhs_state, rhs_state)
                initial.append(c)
        return initial

    def actions(self, source):
        lhs_source,rhs_source = source
        synch_actions = []
        lhs_actions = self.actions(lhs_source)
        lhs_action_count = len(lhs_actions)
        for lhs_action in lhs_actions:
            lhs_targets = self.lhs.execute(lhs_action,lhs_source)
            if len(lhs_targets) == 0:
                lhs_action_count -= 1
                for lhs_target in lhs_targets:
                    lhs_step = (lhs_source,lhs_action,lhs_target)
                    rhs_actions = self.rhs.actions(lhs_step ,rhs_source)
                    actions = map(lambda rA: (lhs_step,rA), rhs_actions)
                    synch_actions.extend(actions)
                    if lhs_action_count == 0 :
                        lhs_step = lhs_source,"deadlock",lhs_source
                        rhs_actions = self.rhs.actions(lhs_step,rhs_source)
                        synch_actions.extend(map(lambda rA: (lhs_step,rA), rhs_actions)) #lhs_target
        return synch_actions

    def execute(self, action, source):
        lhs_step, rhs_action = action
        lhs_source, rhs_source = source
        rhs_targets = self.rhs.execute(rhs_action, (lhs_step, rhs_source))
        return map(lambda rhs_target: (lhs_step[2], rhs_target), rhs_targets)


class DependentSemantics :
    def initial(self):
        pass

    def actions(self, input, configuration):
        pass

    def execute(self, action, input, configuration):
        pass


class DependentSoupSemantics(DependentSemantics):
    def __init__(self, soup):
        self.soup = soup

    def initial(self):
        self.soup.initial()

    def actions(self, input, source):
        return filter(lambda piece : piece.guard(input,source)), self.soup.pieces

    def execute(self, action, input, source):
        src = deepcopy(source)
        inp = deepcopy(input)
        return self.piece.action(inp,src)


if __name__ == '__main__':
    class LHS(SemanticTransition):
        def initial(self):
            return [1, 2]

        def actions(self, conf):
            return ["action1", "action2"]

        def execute(self, conf, action):
            return [(conf[0], "rhs_action1"), (conf[0], "rhs_action2")]

    class RHS(SemanticTransition):
        def initial(self):
            return ["A", "B"]

        def actions(self, conf):
            return ["rhs_action1", "rhs_action2"]

        def execute(self, conf, action):
            return [(conf[0], "C"), (conf[0], "D")]

    lhs_instance = LHS()
    rhs_instance = RHS()

    composition = StepSyncComposition(lhs_instance, rhs_instance)

    initial_states = composition.initial()
    print("Initial States:", initial_states)

    source_configuration = (1, "A")
    actions = composition.actions(source_configuration)
    print("Actions:", actions)

    action = ((1, "rhs_action1"), "A")
    result = composition.execute(action, source_configuration)
    print("Execution Result:", result)

