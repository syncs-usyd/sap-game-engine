from typing import TYPE_CHECKING, Tuple

from engine.input.movetype import MoveType
from engine.config.gameconfig import PET_BUY_COST
from engine.config.gameconfig import PET_POSITIONS, REROLL_COST

if TYPE_CHECKING:
    from engine.input.playerinput import PlayerInput
    from engine.state.foodstate import FoodState
    from engine.state.gamestate import GameState
    from engine.state.playerstate import PlayerState


class InputValidator:
    @staticmethod
    def validate_input(input: 'PlayerInput', player: 'PlayerState', state: 'GameState') -> Tuple[bool, str]:
        return_message = ""
        if input.move_type == MoveType.BUY_PET:
            return_message = InputValidator._validate_buy_pet(input, player)
        elif input.move_type == MoveType.BUY_FOOD:
            return_message = InputValidator._validate_buy_food(input, player)
        elif input.move_type == MoveType.UPGRADE_PET_FROM_PETS:
            return_message = InputValidator._validate_upgrade_pet_from_pet(input, player)
        elif input.move_type == MoveType.UPGRADE_PET_FROM_SHOP:
            return_message = InputValidator._validate_upgrade_pet_from_shop(input, player)
        elif input.move_type == MoveType.SELL_PET:
            return_message = InputValidator._validate_sell_pet(input, player)
        elif input.move_type == MoveType.REROLL:
            return_message = InputValidator._validate_reroll(input, player)
        elif input.move_type == MoveType.FREEZE_PET:
            return_message = InputValidator._validate_freeze_pet(input, player)
        elif input.move_type == MoveType.FREEZE_FOOD:
            return_message = InputValidator._validate_freeze_food(input, player)
        elif input.move_type == MoveType.UNFREEZE_PET:
            return_message = InputValidator._validate_unfreeze_pet(input, player)
        elif input.move_type == MoveType.UNFREEZE_FOOD:
            return_message = InputValidator._validate_unfreeze_food(input, player)
        elif input.move_type == MoveType.SWAP_PET:
            return_message = InputValidator._validate_swap_pets(input, player)

        is_valid = return_message == ""
        if not is_valid:
            return_message = f"Invalid {input.move_type}:\n{return_message}"

        return is_valid, return_message

    @staticmethod
    def _validate_buy_pet(input: 'PlayerInput', player: 'PlayerState') -> str:
        return_message = ""

        return_message += InputValidator._check_shop_pets_index_in_range(player, input.index_from)
        return_message += InputValidator._check_target_pet_index(player, input.index_to, should_be_empty = True)
        return_message += InputValidator._check_sufficient_coins_for_pet(player)

        return return_message

    @staticmethod
    def _validate_buy_food(input: 'PlayerInput', player: 'PlayerState') -> str:
        return_message = ""

        return_message = InputValidator._check_shop_foods_index_in_range(player, input.index_from)
        if return_message != "": return return_message

        food = player.shop_foods[input.index_from]
        return_message += InputValidator._check_food_has_target(player, food, input.index_to)
        return_message += InputValidator._check_sufficient_coins_for_food(player, food)

        return return_message

    @staticmethod
    def _validate_upgrade_pet_from_pet(input: 'PlayerInput', player: 'PlayerState') -> str:
        return_message = ""

        return_message += InputValidator._check_from_pet_index(player, input.index_from, should_be_empty = False)
        return_message += InputValidator._check_target_pet_index(player, input.index_to, should_be_empty = False)

        return return_message

    @staticmethod
    def _validate_upgrade_pet_from_shop(input: 'PlayerInput', player: 'PlayerState') -> str:
        return_message = ""

        return_message += InputValidator._check_shop_pets_index_in_range(player, input.index_from)
        return_message += InputValidator._check_target_pet_index(player, input.index_to, should_be_empty = False)
        return_message += InputValidator._check_sufficient_coins_for_pet(player)

        return return_message

    @staticmethod
    def _validate_sell_pet(input: 'PlayerInput', player: 'PlayerState') -> str:
        return InputValidator._check_from_pet_index(player, input.index_from, should_be_empty = False)

    @staticmethod
    def _validate_reroll(input: 'PlayerInput', player: 'PlayerState') -> str:
        if player.coins < REROLL_COST:
            return f"Not enough currency to reroll. You need {REROLL_COST} but only have {player.coins} available\n"
        else:
            return ""

    @staticmethod
    def _validate_freeze_pet(input: 'PlayerInput', player: 'PlayerState') -> str:
        return_message = InputValidator._check_shop_pets_index_in_range(player, input.index_from)
        if return_message != "": return return_message

        if player.shop_pets[input.index_from].is_frozen:
            return f"Shop Pet at index {input.index_from} is already frozen\n"
        else:
            return ""

    @staticmethod
    def _validate_freeze_food(input: 'PlayerInput', player: 'PlayerState') -> str:
        return_message = InputValidator._check_shop_foods_index_in_range(player, input.index_from)
        if return_message != "": return return_message

        if player.shop_foods[input.index_from].is_frozen:
            return f"Shop Food at index {input.index_from} is already frozen\n"
        else:
            return ""

    @staticmethod
    def _validate_unfreeze_pet(input: 'PlayerInput', player: 'PlayerState') -> str:
        return_message = InputValidator._check_shop_pets_index_in_range(player, input.index_from)
        if return_message != "": return return_message

        if not player.shop_pets[input.index_from].is_frozen:
            return f"Shop Pet at index {input.index_from} is already unfrozen\n"
        else:
            return ""

    @staticmethod
    def _validate_unfreeze_food(input: 'PlayerInput', player: 'PlayerState') -> str:
        return_message = InputValidator._check_shop_foods_index_in_range(player, input.index_from)
        if return_message != "": return return_message

        if not player.shop_foods[input.index_from].is_frozen:
            return f"Shop Food at index {input.index_from} is already unfrozen\n"
        else:
            return ""

    @staticmethod
    def _validate_swap_pets(input: 'PlayerInput', player: 'PlayerState') -> str:
        return_message = ""

        if input.index_from not in range(0, PET_POSITIONS):
            return_message += f"Pet A position {input.index_from} is invalid. The index {input.index_from} is not in the range [0, {PET_POSITIONS - 1}]\n"

        if input.index_to not in range(0, PET_POSITIONS):
            return_message += f"Pet B position {input.index_to} is invalid. The index {input.index_to} is not in the range [0, {PET_POSITIONS - 1}]\n"

        return return_message

    @staticmethod
    def _check_shop_pets_index_in_range(player: 'PlayerState', index: int) -> str:
        if index not in range(0, len(player.shop_pets)):
            return f"Shop Pet is invalid. The index {index} is not in the range [0, {len(player.shop_pets) - 1}]\n"
        else:
            return ""

    @staticmethod
    def _check_shop_foods_index_in_range(player: 'PlayerState', index: int) -> str:
        if index not in range(0, len(player.shop_foods)):
            return f"Shop Food is invalid. The index {index} is not in the range [0, {len(player.shop_foods) - 1}]\n"
        else:
            return ""

    @staticmethod
    def _check_target_pet_index(player: 'PlayerState', index: int, should_be_empty: bool) -> str:
        if index not in range(0, PET_POSITIONS):
            return f"Target pet position {index} is not in the range [0, {PET_POSITIONS - 1}]\n"
        elif player.pets[index] is not None and should_be_empty:
            return f"Target pet position {index} is already occupied\n"
        elif player.pets[index] is None and not should_be_empty:
            return f"Target pet position {index} is not occupied\n"
        else:
            return ""

    @staticmethod
    def _check_from_pet_index(player: 'PlayerState', index: int, should_be_empty: bool) -> str:
        if index not in range(0, PET_POSITIONS):
            return f"From pet position {index} is not in the range [0, {PET_POSITIONS - 1}]\n"
        elif player.pets[index] is not None and should_be_empty:
            return f"From pet position {index} is already occupied\n"
        elif player.pets[index] is None and not should_be_empty:
            return f"From pet position {index} is not occupied\n"
        else:
            return ""

    @staticmethod
    def _check_food_has_target(player: 'PlayerState', food: 'FoodState', index: int) -> str:
        if food.food_config.IS_TARGETED:
            return InputValidator._check_target_pet_index(player, index, should_be_empty = False)
        else:
            return ""

    @staticmethod
    def _check_sufficient_coins_for_pet(player: 'PlayerState') -> str:
        if player.coins < PET_BUY_COST:
            return f"Not enough currency to buy pet. You need {PET_BUY_COST} but only have {player.coins} available\n"
        else:
            return ""

    @staticmethod
    def _check_sufficient_coins_for_food(player: 'PlayerState', food: 'FoodState') -> str:
        if player.coins < food.cost:
            return f"Not enough currency to buy food. You need {food.cost} but only have {player.coins} available\n"
        else:
            return ""
