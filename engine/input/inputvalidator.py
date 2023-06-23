from typing import Tuple

from engine.input.movetype import MoveType
from engine.input.playerinput import PlayerInput
from engine.state.gamestate import GameState
from engine.state.playerstate import PlayerState

from engine.config.roundconfig import ROUND_CONFIG
from engine.config.gameconfig import LEVEL_2_CUTOFF, LEVEL_3_CUTOFF, PET_BUY_COST

class InputValidator:
    @staticmethod
    def validate_input(input: 'PlayerInput', player: 'PlayerState', state: 'GameState') -> Tuple[bool, str]:

        # TODO Handle completely invalid input
        # Check with Oliver 
        
        return_message = "" 
        error_raised = False

        #ISSUE: just realised we are removing things from shop pets meaning that indexing in not abs

        # Get the current round config
        round_conf = ROUND_CONFIG[state.round]

        if input.move_type == MoveType.BUY_PET:
            
            # Check if it is not in the range of the shop pet items
            # Check if it is not in the range of the number of pet slots that a player has
            # Check if the player has enough currency

            if(input.index_from not in range(0, round_conf.NUM_SHOP_PETS)):
                error_raised = True
                return_message += f"Pet slot number provided {input.index_from} is larger than the shop size.\n"

            elif(player.shop_pets[input.index_from] == None):
                error_raised = True
                return_message += f"No pet in shop slot number {input.index_from}, has already been bought\n"

            if(player.coins < PET_BUY_COST):
                error_raised = True
                return_message += f"Not enough currency to buy pet. Required {PET_BUY_COST}, available {player.coins}\n"

            if error_raised:
                return False, return_message

        elif input.move_type == MoveType.BUY_FOOD:
            
            # Check if it is not in the range of the shop food items
            # Check if it is not in the range of the number of pet slots that a player has
            # Check if the player has enough currency

            if error_raised:
                return False, return_message

        elif input.move_type == MoveType.UPGRADE_PET_FROM_PETS:
            
            # Check if both indexes are in range the pet slots that a player has
            # Check if the pet types match EXCEPTION could be special ability type

            if error_raised:
                return False, return_message

        elif input.move_type == MoveType.UPGRADE_PET_FROM_SHOP:
            
            # Check if it is not in the range of the shop pet items
            # Check if in range the pet slots that a player has
            # Check if the pet types match EXCEPTION could be special ability type

            if error_raised:
                return False, return_message

        elif input.move_type == MoveType.SELL_PET:
            
            # Check if it is not in the range of the shop pet items
            # Check if the pet is occupied in pet slot

            if error_raised:
                return False, return_message

        elif input.move_type == MoveType.REROLL:
            
            # Check if player had enough gold 

            if error_raised:
                return False, return_message

        elif input.move_type == MoveType.FREEZE_PET:

            # Check if index is range of number of shop pets
            # Check if shop pet is occupied 
            # Check if the player has enough currency

            if error_raised:
                return False, return_message

        elif input.move_type == MoveType.FREEZE_FOOD:

            # Check if index is range of number of shop foods
            # Check if shop item is occupied 
            # Check if the player has enough currency

            if error_raised:
                return False, return_message

        elif input.move_type == MoveType.UNFREEZE_PET:

            # Check if index is range of number of shop pets
            # Check if shop item is occupied 
            # Check if shop item is frozen 
            # Check if the player has enough currency

            if error_raised:
                return False, return_message

        elif input.move_type == MoveType.UNFREEZE_FOOD:

            # Check if index is range of number of shop foods 
            # Check if shop item is occupied 
            # Check if shop item is frozen 
            # Check if the player has enough currency

            if error_raised:
                return False, return_message

        elif input.move_type == MoveType.SWAP_PET:

            # Check if both indexes are in range the pet slots that a player has
            # Check if both pets slots are occupied

            if error_raised:
                return False, return_message

        elif input.move_type == MoveType.END_TURN:

            #TODO: check what error can be raised for end turn

            if error_raised:
                return False, return_message

        # Move is valid
        return True, None 
