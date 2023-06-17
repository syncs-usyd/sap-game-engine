from engine.config.gameconfig import MAX_MOVES_PER_ROUND
from engine.input.inputhelper import InputHelper
from engine.input.movetype import MoveType
from engine.input.playerinput import PlayerInput
from engine.state.gamestate import GameState
from engine.state.playerstate import PlayerState


class BuyRoundHelper:
    def __init__(self, state: 'GameState'):
        self.state = state
        self.input_helper = InputHelper()

    def run(self, player: 'PlayerState'):
        for moves in range(MAX_MOVES_PER_ROUND):
            input = self.input_helper.get_player_input(player, self.state, MAX_MOVES_PER_ROUND - moves)

            if input.move_type == MoveType.BuyPet:
                self.buy_pet()
            elif input.move_type == MoveType.BuyItem:
                self.buy_item()
            elif input.move_type == MoveType.UpgradePet:
                self.upgrade_pet()
            elif input.move_type == MoveType.SellPet:
                self.sell_pet()
            elif input.move_type == MoveType.Reroll:
                self.reroll()
            elif input.move_type == MoveType.FreezePet:
                self.freeze_pet()
            elif input.move_type == MoveType.FreezeItem:
                self.freeze_item()
            elif input.move_type == MoveType.SwapPet:
                self.swap_pet()
            elif input.move_type == MoveType.EndTurn:
                return
            else:
                raise Exception(f'Invalid move type: {input.move_type}')
            
    def buy_pet(player: 'PlayerState', input: 'PlayerInput'):
        pass

    def buy_item(player: 'PlayerState', input: 'PlayerInput'):
        pass

    def upgrade_pet(player: 'PlayerState', input: 'PlayerInput'):
        pass

    def sell_pet(player: 'PlayerState', input: 'PlayerInput'):
        pass

    def reroll(player: 'PlayerState', input: 'PlayerInput'):
        pass

    def freeze_pet(player: 'PlayerState', input: 'PlayerInput'):
        pass

    def freeze_item(player: 'PlayerState', input: 'PlayerInput'):
        pass

    def swap_pet(player: 'PlayerState', input: 'PlayerInput'):
        pass