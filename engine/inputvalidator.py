from typing import Tuple
from engine.gamestate import GameState
from engine.playerinput import MoveType, PlayerInput
from engine.playerstate import PlayerState


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