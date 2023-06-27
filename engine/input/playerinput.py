from engine.input.movetype import MoveType


class PlayerInput:
    def __init__(self, move_type: 'MoveType', input_dict: dict):
        self.move_type = move_type
        self.index_from: int = input_dict["index_from"] if "index_from" in input_dict else None
        self.index_to: int = input_dict["index_to"] if "index_to" in input_dict else None
