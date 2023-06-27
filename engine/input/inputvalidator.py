from typing import TYPE_CHECKING, Tuple

from engine.input.movetype import MoveType

if TYPE_CHECKING:
    from engine.input.playerinput import PlayerInput
    from engine.state.gamestate import GameState
    from engine.state.playerstate import PlayerState

from engine.config.roundconfig import ROUND_CONFIG
from engine.config.gameconfig import LEVEL_2_CUTOFF, LEVEL_3_CUTOFF, PET_BUY_COST
from engine.config.gameconfig import PET_POSITIONS, REROLL_COST

class InputValidator:

    @staticmethod
    def validate_input(input: 'PlayerInput', player: 'PlayerState', state: 'GameState') -> Tuple[bool, str]:

        return_message = "" 

        # Get the current round config
        round_conf = ROUND_CONFIG[state.round]

        if input.move_type == MoveType.BUY_PET:
            return_message = _validate_buy_pet(input, player, round_conf)  
        elif input.move_type == MoveType.BUY_FOOD:
            return_message = _validate_buy_food(input, player, round_conf)
        elif input.move_type == MoveType.UPGRADE_PET_FROM_PETS:
            return_message = _validate_upgrade_pet_from_pet(input, player)
        elif input.move_type == MoveType.UPGRADE_PET_FROM_SHOP:
            return_message = _validate_upgrade_pet_from_shop(input, player, round_conf)
        elif input.move_type == MoveType.SELL_PET:
            return_message = _validate_sell_pet(input, player)
        elif input.move_type == MoveType.REROLL:
            return_message = _validate_reroll(input, player)
        elif input.move_type == MoveType.FREEZE_PET:
            return_message = _validate_freeze_pet(input, player, round_conf)
        elif input.move_type == MoveType.FREEZE_FOOD:
            return_message = _validate_freeze_food(input, player, round_conf)
        elif input.move_type == MoveType.UNFREEZE_PET:
            return_message = _validate_unfreeze_pet(input, player, round_conf)
        elif input.move_type == MoveType.UNFREEZE_FOOD:
            return_message = _validate_unfreeze_food(input, player, round_conf)
        elif input.move_type == MoveType.SWAP_PET:
            return_message = _validate_swap_pets(input, player)
        elif input.move_type == MoveType.END_TURN:
            pass

        if return_message == "":
            return_message = None

        return bool(return_message), return_message 

    @staticmethod
    def _validate_buy_pet(input: "PlayerInput", player: "PlayerState", round_conf: "RoundConfig") -> str:
        return_message = ""

        if(input.index_from not in range(0, round_conf.NUM_SHOP_PETS)):
            return_message += f"Shop Pet slot number provided {input.index_from} is not an integer in range(0, {round_conf.NUM_SHOP_PETS}).\n"

        elif(player.shop_pets[input.index_from] == None):
            return_message += f"No pet in shop slot number {input.index_from}. Has already been bought\n"

        if(input.index_to not in range(0, PET_POSITIONS)):
            return_message += f"Pet slot provided {input.index_to}, is not in the available pet slot number [0, {PET_POSITIONS}]\n"

        elif(player.pets[input.index_to] != None):
            return_message += f"Pet slot provided {input.index_to}, is already occupied\n"

        if(player.coins < PET_BUY_COST):
            return_message += f"Not enough currency to buy pet. Required {PET_BUY_COST}, available {player.coins}\n"

        return return_message

    @staticmethod
    def _validate_buy_food(input: "PlayerInput", player: "PlayerState", round_conf: "RoundConfig") -> str:
        if(input.index_from not in range(0, round_conf.NUM_SHOP_FOODS)):
            return_message += f"Shop Food slot number provided {input.index_from} is not an integer in range(0, {round_conf.NUM_SHOP_FOODS}).\n"

        elif(player.shop_foods[input.index_from] == None):
            return_message += f"No food in shop slot number {input.index_from}. Has already been bought\n"

        if(input.index_to not in range(0, PET_POSITIONS)):
            return_message += f"Pet slot provided {input.index_to}, is not in the available pet slot number [0, {PET_POSITIONS}]\n"

        elif(player.pets[input.index_to] == None):
            return_message += f"Pet slot provided {input.index_to}, is not occupied\n"

        if(player.coins < player.shop_foods[input.index_from].food_config.BUY_COST):
            return_message += f"Not enough currency to buy food. Required {player.shop_foods[input.index_from].food_config.BUY_COST}, available {player.coins}\n"

        return return_message

    @staticmethod
    def _validate_upgrade_pet_from_pet(input: "PlayerInput", player: "PlayerState") -> str:
        if(input.index_from not in range(0, PET_POSITIONS)):
            return_message += f"From pet slot provided {input.index_from}, is not in the available pet slot number [0, {PET_POSITIONS}]\n"

        elif(player.pets[input.index_from] == None):
            return_message += f"From pet slot provided {input.index_from}, is not occupied\n"

        if(input.index_to not in range(0, PET_POSITIONS)):
            return_message += f"To pet slot provided {input.index_to}, is not in the available pet slot number [0, {PET_POSITIONS}]\n"

        elif(player.pets[input.index_to] == None):
            return_message += f"From pet slot provided {input.index_to}, is not occupied\n"

        return return_message

    @staticmethod
    def _validate_upgrade_pet_from_shop(input: "PlayerInput", player: "PlayerState", round_conf: "RoundConfig") -> str:
        if(input.index_from not in range(0, round_conf.NUM_SHOP_PETS)):
            return_message += f"Shop Pet slot number provided {input.index_from} is not an integer in range(0, {round_conf.NUM_SHOP_PETS}).\n"

        elif(player.shop_pets[input.index_from] == None):
            return_message += f"No pet in shop slot number {input.index_from}. Has already been bought\n"

        if(input.index_to not in range(0, PET_POSITIONS)):
            return_message += f"To pet slot provided {input.index_to}, is not in the available pet slot number [0, {PET_POSITIONS}]\n"

        elif(player.pets[input.index_to] == None):
            return_message += f"From pet slot provided {input.index_to}, is not occupied\n"

        return return_message

    @staticmethod
    def _validate_sell_pet(input: "PlayerInput", player: "PlayerState") -> str:
        if(input.index_to not in range(0, PET_POSITIONS)):
            return_message += f"To pet slot provided {input.index_to}, is not in the available pet slot number [0, {PET_POSITIONS}]\n"

        elif(player.pets[input.index_to] == None):
            return_message += f"From pet slot provided {input.index_to}, is not occupied\n"

        return return_message

    @staticmethod
    def _validate_reroll(input: "PlayerInput", player: "PlayerState") -> str:
        if(player.coins < REROLL_COST):
            return_message += f"Not enough currency to reroll. Required {REROLL_COST}, available {player.coins}\n"

        return return_message

    @staticmethod
    def _validate_freeze_pet(input: "PlayerInput", player: "PlayerState", round_conf: "RoundConfig") -> str:
        return_message = ""

        if(input.index_from not in range(0, round_conf.NUM_SHOP_PETS)):
            return_message += f"Shop Pet slot number provided {input.index_from} is not an integer in range(0, {round_conf.NUM_SHOP_PETS}).\n"

        elif(player.shop_pets[input.index_from] == None):
            return_message += f"No pet in shop slot number {input.index_from}. Has already been bought\n"

        if(player.shop_pets[input.index_from].is_frozen):
            return_message += f"Pet in shop slot number {input.index_from}, already frozen.\n"

        return return_message

    @staticmethod
    def _validate_freeze_food(input: "PlayerInput", player: "PlayerState", round_conf: "RoundConfig") -> str:
        if(input.index_from not in range(0, round_conf.NUM_SHOP_FOODS)):
            return_message += f"Shop Food slot number provided {input.index_from} is not an integer in range(0, {round_conf.NUM_SHOP_FOODS}).\n"

        elif(player.shop_foods[input.index_from] == None):
            return_message += f"No food item in shop slot number {input.index_from}. Has already been bought\n"

        if(player.shop_foods[input.index_from].is_frozen):
            return_message += f"Food item in shop slot number {input.index_from}, already frozen.\n"

        return return_message

    @staticmethod
    def _validate_unfreeze_pet(input: "PlayerInput", player: "PlayerState", round_conf: "RoundConfig") -> str:
        if(input.index_from not in range(0, round_conf.NUM_SHOP_PETS)):
            return_message += f"Shop Pet slot number provided {input.index_from} is not an integer in range(0, {round_conf.NUM_SHOP_PETS}).\n"

        elif(player.shop_pets[input.index_from] == None):
            return_message += f"No pet in shop slot number {input.index_from}. Has already been bought\n"

        if(not player.shop_pets[input.index_from].is_frozen):
            return_message += f"Pet in shop slot number {input.index_from}, already not frozen.\n"

        return return_message

    @staticmethod
    def _validate_unfreeze_food(input: "PlayerInput", player: "PlayerState", round_conf: "RoundConfig") -> str:
        if(input.index_from not in range(0, round_conf.NUM_SHOP_FOODS)):
            return_message += f"Shop Food slot number provided {input.index_from} is not an integer in range(0, {round_conf.NUM_SHOP_FOODS}).\n"

        elif(player.shop_foods[input.index_from] == None):
            return_message += f"No food item in shop slot number {input.index_from}. Has already been bought\n"

        if(not player.shop_foods[input.index_from].is_frozen):
            return_message += f"Food item in shop slot number {input.index_from}, already not frozen.\n"

        return return_message

    @staticmethod
    def _validate_swap_pets(input: "PlayerInput", player: "PlayerState") -> str:
        if(input.index_from not in range(0, PET_POSITIONS)):
            return_message += f"''From' Pet slot provided {input.index_from}, is not in the available pet slot number [0, {PET_POSITIONS}]\n"

        elif(player.pets[input.index_from] == None):
            return_message += f"''From' Pet slot provided {input.index_from}, is not occupied\n"

        if(input.index_to not in range(0, PET_POSITIONS)):
            return_message += f"''To' Pet slot provided {input.index_to}, is not in the available pet slot number [0, {PET_POSITIONS}]\n"

        elif(player.pets[input.index_to] == None):
            return_message += f"''To' Pet slot provided {input.index_to}, is not occupied\n"

        return return_message

