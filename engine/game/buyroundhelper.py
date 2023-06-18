from engine.config.gameconfig import MAX_MOVES_PER_ROUND
from engine.input.inputhelper import InputHelper
from engine.input.movetype import MoveType
from engine.input.playerinput import PlayerInput
from engine.output.outputhandler import OutputHandler
from engine.output.terminationtype import TerminationType
from engine.state.gamestate import GameState
from engine.state.playerstate import PlayerState


class BuyRoundHelper:
    def __init__(self, state: 'GameState', output_handler: 'OutputHandler'):
        self.state = state
        self.output_handler = output_handler
        self.input_helper = InputHelper(state, output_handler)

    def run(self, player: 'PlayerState', round: int):
        for moves in range(MAX_MOVES_PER_ROUND):
            input = self.input_helper.get_player_input(player, MAX_MOVES_PER_ROUND - moves)

            if input.move_type == MoveType.BUY_PET:
                self._buy_pet(player, input, round)
            elif input.move_type == MoveType.BUY_ITEM:
                self._buy_item(player, input, round)
            elif input.move_type == MoveType.UPGRADE_PET:
                self._upgrade_pet(player, input, round)
            elif input.move_type == MoveType.SELL_PET:
                self._sell_pet(player, input, round)
            elif input.move_type == MoveType.REROLL:
                self._reroll(player, input, round)
            elif input.move_type == MoveType.FREEZE_PET:
                self._freeze_pet(player, input, round)
            elif input.move_type == MoveType.FREEZE_ITEM:
                self._freeze_item(player, input, round)
            elif input.move_type == MoveType.SWAP_PET:
                self._swap_pet(player, input, round)
            elif input.move_type == MoveType.END_TURN:
                return
            else:
                raise Exception(f'Invalid move type: {input.move_type}')

        self.output_handler.terminate_fail(TerminationType.TOO_MANY_MOVES, player, reason = f"Used more than the max number of moves in a single round. Note: the max is {MAX_MOVES_PER_ROUND}")

    def _buy_pet(self, player: 'PlayerState', input: 'PlayerInput', round: int):

        # temp values until input handler is better decided
        pet_pos_to_buy = 0
        position = len(player.pets)

        # find the pet specified by the user
        pet_to_buy = get_shop_options()[0][pet_name_to_buy]

        # buy the pet specified by the user
        player.pets.append(pet_to_buy)

        # remove pet from buy options
        player.remove_pet_option(round)

    def _buy_item(self, player: 'PlayerState', input: 'PlayerInput', round: int):

        # temp values until input handler is better decided
        item_pos_to_buy = 0
        position = len(player.)

        # find the pet specified by the user
        pet_to_buy = get_shop_options()[0][pet_name_to_buy]

        # buy the pet specified by the user
        player.pets.append(pet_to_buy)

        # remove pet from buy options
        player.remove_pet_option(round)

    def _upgrade_pet(self, player: 'PlayerState', input: 'PlayerInput', round: int):
        pass

    def _sell_pet(self, player: 'PlayerState', input: 'PlayerInput', round: int):
        pass

    def _reroll(self, player: 'PlayerState', input: 'PlayerInput', round: int):
        pass

    def _freeze_pet(self, player: 'PlayerState', input: 'PlayerInput', round: int):
        pass

    def _freeze_item(self, player: 'PlayerState', input: 'PlayerInput', round: int):
        pass

    def _swap_pet(self, player: 'PlayerState', input: 'PlayerInput', round: int):
        pass
