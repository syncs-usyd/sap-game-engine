from typing import TYPE_CHECKING, Optional

from engine.config.gameconfig import MAX_MOVES_PER_ROUND, PET_BUY_COST, REROLL_COST
from engine.game.abilitytype import AbilityType
from engine.input.inputhelper import InputHelper
from engine.input.movetype import MoveType

if TYPE_CHECKING:
    from engine.input.playerinput import PlayerInput
    from engine.output.gamelog import GameLog
    from engine.output.outputhandler import OutputHandler
    from engine.state.gamestate import GameState
    from engine.state.petstate import PetState
    from engine.state.playerstate import PlayerState


class BuyStageHelper:
    def __init__(self, state: 'GameState', log: 'GameLog', output_handler: 'OutputHandler'):
        self.state = state
        self.log = log
        self.output_handler = output_handler
        self.input_helper = InputHelper(state, output_handler)

    def run(self, player: 'PlayerState'):
        for moves in range(MAX_MOVES_PER_ROUND):
            input = self.input_helper.get_player_input(player, MAX_MOVES_PER_ROUND - moves)

            if input.move_type == MoveType.BUY_PET:
                self._buy_pet(player, input)
            elif input.move_type == MoveType.BUY_FOOD:
                self._buy_food(player, input)
            elif input.move_type == MoveType.UPGRADE_PET_FROM_PETS:
                self._upgrade_pet_from_pets(player, input)
            elif input.move_type == MoveType.UPGRADE_PET_FROM_SHOP:
                self._upgrade_pet_from_shop(player, input)
            elif input.move_type == MoveType.SELL_PET:
                self._sell_pet(player, input)
            elif input.move_type == MoveType.REROLL:
                self._reroll(player, input)
            elif input.move_type == MoveType.FREEZE_PET:
                self._freeze_pet(player, input)
            elif input.move_type == MoveType.FREEZE_FOOD:
                self._freeze_food(player, input)
            elif input.move_type == MoveType.UNFREEZE_PET:
                self._unfreeze_pet(player, input)
            elif input.move_type == MoveType.UNFREEZE_FOOD:
                self._unfreeze_food(player, input)
            elif input.move_type == MoveType.SWAP_PET:
                self._swap_pet(player, input)
            elif input.move_type == MoveType.END_TURN:
                self.log.write_buy_stage_log(player, "End turn")
                return
            else:
                raise Exception(f'Invalid move type: {input.move_type}')

    def _buy_pet(self, player: 'PlayerState', input: 'PlayerInput'):
        new_pet = player.shop_pets[input.index_from]
        player.shop_pets.remove(new_pet)
        player.coins -= PET_BUY_COST

        player.pets[input.index_to] = new_pet
        new_pet.proc_on_demand_ability(AbilityType.BUY)
        player.friend_summoned(new_pet)

        log = f"Bought {new_pet} for position {input.index_to + 1}"
        self.log.write_buy_stage_log(player, log)

    def _buy_food(self, player: 'PlayerState', input: 'PlayerInput'):
        food = player.shop_foods[input.index_from]
        player.shop_foods.remove(food)
        player.coins -= food.cost

        log = f"Bought {food}"

        pet: Optional['PetState'] = None
        if food.food_config.IS_TARGETED:
            pet = player.pets[input.index_to]
            log += f" for {pet}"

        # For carried food, the effects are hard-coded
        if food.food_config.IS_CARRIED:
            assert pet is not None
            pet.carried_food = food.food_config
        else:
            food.food_config.EFFECT_FUNC(pet, player, self.state)

        self.log.write_buy_stage_log(player, log)

    def _upgrade_pet_from_pets(self, player: 'PlayerState', input: 'PlayerInput'):
        from_pet = player.pets[input.index_from]
        player.pets[input.index_from] = None

        to_pet = player.pets[input.index_to]
        to_pet.level_up(from_pet)

        log = f"Leveled up {to_pet} using {from_pet}"
        self.log.write_buy_stage_log(player, log)

    def _upgrade_pet_from_shop(self, player: 'PlayerState', input: 'PlayerInput'):
        shop_pet = player.shop_pets[input.index_from]
        player.shop_pets.remove(shop_pet)
        player.coins -= PET_BUY_COST

        pet = player.pets[input.index_to]
        pet.level_up(shop_pet)
        pet.proc_on_demand_ability(AbilityType.BUY)
        player.friend_summoned(pet)

        log = f"Leveled up {pet} by buying {shop_pet}"
        self.log.write_buy_stage_log(player, log)

    def _sell_pet(self, player: 'PlayerState', input: 'PlayerInput'):
        pet = player.pets[input.index_from]
        player.pets[input.index_from] = None

        pet.proc_on_demand_ability(AbilityType.SELL)
        player.coins += pet.get_level()

        log = f"Sold {pet}"
        self.log.write_buy_stage_log(player, log)

    def _reroll(self, player: 'PlayerState', input: 'PlayerInput'):
        player.reset_shop_options()
        player.coins -= REROLL_COST

        log = f"Rerolled shop"
        self.log.write_buy_stage_log(player, log)

    def _freeze_pet(self, player: 'PlayerState', input: 'PlayerInput'):
        pet = player.shop_pets[input.index_from]
        pet.is_frozen = True

        log = f"Froze {pet}"
        self.log.write_buy_stage_log(player, log)

    def _freeze_food(self, player: 'PlayerState', input: 'PlayerInput'):
        food = player.shop_foods[input.index_from]
        food.is_frozen = True

        log = f"Froze {food}"
        self.log.write_buy_stage_log(player, log)

    def _unfreeze_pet(self, player: 'PlayerState', input: 'PlayerInput'):
        pet = player.shop_pets[input.index_from]
        pet.is_frozen = False

        log = f"Unfroze {pet}"
        self.log.write_buy_stage_log(player, log)

    def _unfreeze_food(self, player: 'PlayerState', input: 'PlayerInput'):
        food = player.shop_foods[input.index_from]
        food.is_frozen = False

        log = f"Unfroze {food}"
        self.log.write_buy_stage_log(player, log)

    def _swap_pet(self, player: 'PlayerState', input: 'PlayerInput'):
        pet_a = player.pets[input.index_from]
        pet_b = player.pets[input.index_to]

        player.pets[input.index_from] = pet_b 
        player.pets[input.index_to] = pet_a

        log = ""
        if pet_a is not None and pet_b is not None:
            log = f"Swapped {pet_a} and {pet_b} positions"
        elif pet_a is not None:
            log = f"Moved {pet_a} to position {input.index_to}"
        else:
            log = f"Moved {pet_b} to position {input.index_from}"
        self.log.write_buy_stage_log(player, log)
