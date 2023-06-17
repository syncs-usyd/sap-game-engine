from typing import Tuple

from engine.input.movetype import MoveType
from engine.input.playerinput import PlayerInput
from engine.state.gamestate import GameState
from engine.state.playerstate import PlayerState


class InputValidator:
    @staticmethod
    def validate_input(input: 'PlayerInput', player: 'PlayerState', state: 'GameState') -> Tuple[bool, str]:
        # TODO
        if input.move_type == MoveType.BuyPet:
            a = 1
            b = 2
            if a == b:
                return False, "Reason for being invalid"

        # Move is valid
        return True, None