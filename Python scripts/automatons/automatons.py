import threading as th


class Automaton:
    def __init__(self, initial_state, state_transitions, final_states):
        self.state: str = initial_state
        self.transitions: dict = state_transitions
        self.final_states: tuple = final_states

    def run(self, input_: str) -> bool:
        for bit in input_:
            self.state = self.transitions.get((self.state, bit))
            if self.state is None:
                return False
        return self.state in self.final_states


TRANSITIONS = {
    ("odd", "0"): "odd",
    ("odd", "1"): "even",
    ("even", "0"): "even",
    ("even", "1"): "odd",
}

ROY = Automaton("even", TRANSITIONS, ("odd",))
print(ROY.run("011001"))
