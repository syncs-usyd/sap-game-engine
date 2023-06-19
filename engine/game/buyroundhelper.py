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
                self._buy_pet(player, input)
            elif input.move_type == MoveType.BUY_ITEM:
                self._buy_item(player, input)
            elif input.move_type == MoveType.UPGRADE_PET:
                self._upgrade_pet(player, input)
            elif input.move_type == MoveType.SELL_PET:
                self._sell_pet(player, input)
            elif input.move_type == MoveType.REROLL:
                self._reroll(player, input)
            elif input.move_type == MoveType.FREEZE_PET:
                self._freeze_pet(player, input)
            elif input.move_type == MoveType.FREEZE_ITEM:
                self._freeze_item(player, input)
            elif input.move_type == MoveType.SWAP_PET:
                self._swap_pet(player, input)
            elif input.move_type == MoveType.END_TURN:
                return
            else:
                raise Exception(f'Invalid move type: {input.move_type}')

        self.output_handler.terminate_fail(TerminationType.TOO_MANY_MOVES, player, reason = f"Used more than the max number of moves in a single round. Note: the max is {MAX_MOVES_PER_ROUND}")

    def _buy_pet(self, player: 'PlayerState', input: 'PlayerInput'):

        # find the pet specified by the user
        pet_to_buy = player.shop_pets[input.index_from]

        # buy the pet specified by the user
        player.pets.append(pet_to_buy)
        player.pets.insert(input.index_to, pet_to_buy)

        # remove pet from buy options
        player.shop_pets.remove(pet_to_buy)

    def _buy_item(self, player: 'PlayerState', input: 'PlayerInput'):

        # find the item specified by the user
        food_to_buy = player.shop_foods[input.index_from]

        # buy the pet specified by the user
        pet_to_add_food = player.pets[input.index_to]
        pet_to_add_food.add_food(food_to_buy)

        # remove pet from buy options
        player.shop_foods.remove(food_to_buy)

    def _upgrade_pet(self, player: 'PlayerState', input: 'PlayerInput'):

        # find the pet specified by the user
        pet_to_buy = player.shop_pets[input.index_from]
        pet_to_upgrade = player.pets[input.index_to]
        
        # Upgrade pets level
        pet_to_upgrade.sub_level += 1

        # remove pet from buy options
        player.shop_pets.remove(pet_to_buy)


    def _sell_pet(self, player: 'PlayerState', input: 'PlayerInput'):

        # find the pet specified by the user
        pet_to_buy = player.shop_pets[input.index_from]
        
        # Upgrade pets level
        pet_to_upgrade.sub_level += 1

        # remove pet from buy options
        player.shop_pets.remove(pet_to_buy)

    def _reroll(self, player: 'PlayerState', input: 'PlayerInput', round: int):
        player.shop_pets, player.shop_foods = player.get_shop_options(round)

    def _freeze_pet(self, player: 'PlayerState', input: 'PlayerInput'):
        pet_to_freeze = player.shop_pets[input.index_from]
        pet_to_freeze.is_frozen = True

    def _freeze_item(self, player: 'PlayerState', input: 'PlayerInput'):

        # Freeze item specified
        food_to_freeze = player.shop_foods[input.index_from]
        food_to_freeze.is_frozen = True

    def _swap_pet(self, player: 'PlayerState', input: 'PlayerInput'):

        # Swap Pets
        player.pets[input.index_from], player.pets[input.index_to]\
                = player.pets[input.index_to], player.pets[input.index_from]
