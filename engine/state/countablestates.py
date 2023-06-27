import itertools

class CountableStates:

    id_iter = itertools.count()

    def __init__(self):
        self.id = next(countable_states.id_iter)
