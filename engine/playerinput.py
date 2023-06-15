from enum import Enum
from engine.gamestate import GameState
from engine.playerstate import PlayerState


class MoveType(Enum):
    BuyPet = 1
    BuyItem = 2
    UpgradePet = 3
    SellPet = 4
    Reroll = 5
    FreezePet = 6
    FreezeItem = 7
    SwapPet = 8
    EndTurn = 9

class PlayerInput:
    @staticmethod
    def get_player_input(player: 'PlayerState', state: 'GameState') -> 'PlayerInput':
      # Read the input_dict for the player
      # Parse move type
      # Create PlayerInput obj
      # Validate PlayerInput obj
      # return PlayerInput obj
      pass

    def __init__(self, move_type: 'MoveType', input_dict: dict) -> 'PlayerInput':
        self.move_type = move_type
        if move_type == MoveType.BuyPet:
            self.parse_buy_pet()
        elif move_type == MoveType.BuyItem:
            self.parse_buy_item()
        elif move_type == MoveType.UpgradePet:
            self.parse_upgrade_pet()
        elif move_type == MoveType.SellPet:
            self.parse_sell_pet()
        elif move_type == MoveType.Reroll:
            self.parse_reroll()
        elif move_type == MoveType.FreezePet:
            self.parse_freeze_pet()
        elif move_type == MoveType.FreezeItem:
            self.parse_freeze_item()
        elif move_type == MoveType.SwapPet:
            self.parse_swap_pet()
        elif move_type == MoveType.EndTurn:
            self.parse_end_turn()
        else:
            raise Exception(f'Invalid move type: {move_type}')

    def parse_buy_pet(self, input_dict):
        pass

    def parse_buy_item(self, input_dict):
        pass

    def parse_upgrade_pet(self, input_dict):
        pass

    def parse_sell_pet(self, input_dict):
        pass

    def parse_reroll(self, input_dict):
        pass

    def parse_freeze_pet(self, input_dict):
        pass

    def parse_freeze_item(self, input_dict):
        pass

    def parse_swap_pet(self, input_dict):
        pass

    def parse_end_turn(self, input_dict):
        pass