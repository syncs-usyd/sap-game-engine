from typing import Tuple

from engine.input.movetype import MoveType
from engine.input.playerinput import PlayerInput
from engine.state.gamestate import GameState
from engine.state.playerstate import PlayerState

from engine.config.roundconfig import ROUND_CONFIG
from engine.config.gameconfig import LEVEL_2_CUTOFF, LEVEL_3_CUTOFF, PET_BUY_COST
from engine.config.gameconfig import PET_POSITIONS, REROLL_COST, FREEZE_COST

class InputValidator:
    @staticmethod
    def validate_input(input: 'PlayerInput', player: 'PlayerState', state: 'GameState') -> Tuple[bool, str]:

        # TODO Handle completely invalid input
        # Check with Oliver 
        
        return_message = "" 
        error_raised = False

        #ISSUE: just realised we are removing things from shop pets meaning that indexing in not abs
        #TODO: Ask Oliver if he wants multiple error messages or?

        # Get the current round config
        round_conf = ROUND_CONFIG[state.round]

        if input.move_type == MoveType.BUY_PET:
            
            # Check if it is not in the range of the shop pet items
            # Check if it is not in the range of the number of pet slots that a player has
            # Check if the player has enough currency

            if(input.index_from not in range(0, round_conf.NUM_SHOP_PETS)):
                error_raised = True
                return_message += f"Shop Pet slot number provided {input.index_from} is larger than the shop size.\n"

            elif(player.shop_pets[input.index_from] == None):
                error_raised = True
                return_message += f"No pet in shop slot number {input.index_from}. Has already been bought\n"

            elif(input.index_to not in range(0, PET_POSITIONS)):
                error_raised = True
                return_message += f"Pet slot provided {input.index_to}, is not in the available pet slot number [0, {PET_POSITIONS}]\n"

            elif(player.pets[input.index_to] != None):
                error_raised = True
                return_message += f"Pet slot provided {input.index_to}, is already occupied\n"

            if(player.coins < PET_BUY_COST):
                error_raised = True
                return_message += f"Not enough currency to buy pet. Required {PET_BUY_COST}, available {player.coins}\n"

            if error_raised:
                return False, return_message

        elif input.move_type == MoveType.BUY_FOOD:
            
            # Check if it is not in the range of the shop food items
            # Check if it is not in the range of the number of pet slots that a player has
            # Check if the player has enough currency

            if(input.index_from not in range(0, round_conf.NUM_SHOP_FOODS)):
                error_raised = True
                return_message += f"Shop Food slot number provided {input.index_from} is larger than the shop size.\n"

            elif(player.shop_foods[input.index_from] == None):
                error_raised = True
                return_message += f"No food in shop slot number {input.index_from}. Has already been bought\n"

            elif(input.index_to not in range(0, PET_POSITIONS)):
                error_raised = True
                return_message += f"Pet slot provided {input.index_to}, is not in the available pet slot number [0, {PET_POSITIONS}]\n"

            elif(player.pets[input.index_to] == None):
                error_raised = True
                return_message += f"Pet slot provided {input.index_to}, is not occupied\n"

            if(player.coins < player.shop_foods[input.index_from].food_config.BUY_COST):
                error_raised = True
                return_message += f"Not enough currency to buy food. Required {player.shop_foods[input.index_from].food_config.BUY_COST}, available {player.coins}\n"

            if error_raised:
                return False, return_message

        elif input.move_type == MoveType.UPGRADE_PET_FROM_PETS:
            
            # Check if both indexes are in range the pet slots that a player has
            # Check if the pet types match EXCEPTION could be special ability type

            if(input.index_from not in range(0, PET_POSITIONS)):
                error_raised = True
                return_message += f"From pet slot provided {input.index_from}, is not in the available pet slot number [0, {PET_POSITIONS}]\n"

            elif(player.pets[input.index_from] == None):
                error_raised = True
                return_message += f"From pet slot provided {input.index_from}, is not occupied\n"

            if(input.index_to not in range(0, PET_POSITIONS)):
                error_raised = True
                return_message += f"To pet slot provided {input.index_to}, is not in the available pet slot number [0, {PET_POSITIONS}]\n"

            elif(player.pets[input.index_to] == None):
                error_raised = True
                return_message += f"From pet slot provided {input.index_to}, is not occupied\n"

            if error_raised:
                return False, return_message

        elif input.move_type == MoveType.UPGRADE_PET_FROM_SHOP:
            
            # Check if it is not in the range of the shop pet items
            # Check if in range the pet slots that a player has
            # Check if the pet types match EXCEPTION could be special ability type

            if(input.index_from not in range(0, round_conf.NUM_SHOP_PETS)):
                error_raised = True
                return_message += f"Shop Pet slot number provided {input.index_from} is larger than the shop size.\n"

            elif(player.shop_pets[input.index_from] == None):
                error_raised = True
                return_message += f"No pet in shop slot number {input.index_from}. Has already been bought\n"

            if(input.index_to not in range(0, PET_POSITIONS)):
                error_raised = True
                return_message += f"To pet slot provided {input.index_to}, is not in the available pet slot number [0, {PET_POSITIONS}]\n"

            elif(player.pets[input.index_to] == None):
                error_raised = True
                return_message += f"From pet slot provided {input.index_to}, is not occupied\n"

            if error_raised:
                return False, return_message

        elif input.move_type == MoveType.SELL_PET:
            
            # Check if it is not in the range of the pet positions 
            # Check if the pet is occupied in pet slot

            if(input.index_to not in range(0, PET_POSITIONS)):
                error_raised = True
                return_message += f"To pet slot provided {input.index_to}, is not in the available pet slot number [0, {PET_POSITIONS}]\n"

            elif(player.pets[input.index_to] == None):
                error_raised = True
                return_message += f"From pet slot provided {input.index_to}, is not occupied\n"

            if error_raised:
                return False, return_message

        elif input.move_type == MoveType.REROLL:
            
            # Check if player had enough gold 

            if(player.coins < REROLL_COST):
                error_raised = True
                return_message += f"Not enough currency to reroll. Required {REROLL_COST}, available {player.coins}\n"

            if error_raised:
                return False, return_message

        elif input.move_type == MoveType.FREEZE_PET:

            # Check if index is range of number of shop pets
            # Check if shop pet is occupied 
            # Check if the player has enough currency

            if(input.index_from not in range(0, round_conf.NUM_SHOP_PETS)):
                error_raised = True
                return_message += f"Shop Pet slot number provided {input.index_from} is larger than the shop size.\n"

            elif(player.shop_pets[input.index_from] == None):
                error_raised = True
                return_message += f"No pet in shop slot number {input.index_from}. Has already been bought\n"

            elif(player.shop_pets[input.index_from].is_frozen):
                error_raised = True
                return_message += f"Pet in shop slot number {input.index_from}, already frozen.\n"

            if(player.coins < FREEZE_COST):
                error_raised = True
                return_message += f"Not enough currency to freeze pet. Required {FREEZE_COST}, available {player.coins}\n"

            if error_raised:
                return False, return_message

        elif input.move_type == MoveType.FREEZE_FOOD:

            # Check if index is range of number of shop foods
            # Check if shop item is occupied 

            if(input.index_from not in range(0, round_conf.NUM_SHOP_FOODS)):
                error_raised = True
                return_message += f"Shop Food slot number provided {input.index_from} is larger than the shop size.\n"

            elif(player.shop_foods[input.index_from] == None):
                error_raised = True
                return_message += f"No food item in shop slot number {input.index_from}. Has already been bought\n"

            elif(player.shop_foods[input.index_from].is_frozen):
                error_raised = True
                return_message += f"Food item in shop slot number {input.index_from}, already frozen.\n"

            if(player.coins < FREEZE_COST):
                error_raised = True
                return_message += f"Not enough currency to freeze pet. Required {FREEZE_COST}, available {player.coins}\n"

            if error_raised:
                return False, return_message

        elif input.move_type == MoveType.UNFREEZE_PET:

            # Check if index is range of number of shop pets
            # Check if shop item is occupied 
            # Check if shop item is frozen 

            if(input.index_from not in range(0, round_conf.NUM_SHOP_PETS)):
                error_raised = True
                return_message += f"Shop Pet slot number provided {input.index_from} is larger than the shop size.\n"

            elif(player.shop_pets[input.index_from] == None):
                error_raised = True
                return_message += f"No pet in shop slot number {input.index_from}. Has already been bought\n"

            elif(not player.shop_pets[input.index_from].is_frozen):
                error_raised = True
                return_message += f"Pet in shop slot number {input.index_from}, already not frozen.\n"

            if error_raised:
                return False, return_message

        elif input.move_type == MoveType.UNFREEZE_FOOD:

            # Check if index is range of number of shop foods 
            # Check if shop item is occupied 
            # Check if shop item is frozen 
            # Check if the player has enough currency

            if(input.index_from not in range(0, round_conf.NUM_SHOP_FOODS)):
                error_raised = True
                return_message += f"Shop Food slot number provided {input.index_from} is larger than the shop size.\n"

            elif(player.shop_foods[input.index_from] == None):
                error_raised = True
                return_message += f"No food item in shop slot number {input.index_from}. Has already been bought\n"

            elif(not player.shop_foods[input.index_from].is_frozen):
                error_raised = True
                return_message += f"Food item in shop slot number {input.index_from}, already not frozen.\n"

            if error_raised:
                return False, return_message

        elif input.move_type == MoveType.SWAP_PET:

            # Check if both indexes are in range the pet slots that a player has
            # Check if both pets slots are occupied

            if(input.index_from not in range(0, PET_POSITIONS)):
                error_raised = True
                return_message += f"''From' Pet slot provided {input.index_from}, is not in the available pet slot number [0, {PET_POSITIONS}]\n"

            elif(player.pets[input.index_from] == None):
                error_raised = True
                return_message += f"''From' Pet slot provided {input.index_from}, is not occupied\n"

            if(input.index_to not in range(0, PET_POSITIONS)):
                error_raised = True
                return_message += f"''To' Pet slot provided {input.index_to}, is not in the available pet slot number [0, {PET_POSITIONS}]\n"

            elif(player.pets[input.index_to] == None):
                error_raised = True
                return_message += f"''To' Pet slot provided {input.index_to}, is not occupied\n"

            if error_raised:
                return False, return_message

        elif input.move_type == MoveType.END_TURN:

            #TODO: check what error can be raised for end turn

            if error_raised:
                return False, return_message

        # Move is valid
        return True, None 
