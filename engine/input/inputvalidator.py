from typing import Tuple

from engine.input.movetype import MoveType
from engine.input.playerinput import PlayerInput
from engine.state.gamestate import GameState
from engine.state.playerstate import PlayerState


class InputValidator:
    @staticmethod
    def validate_input(input: 'PlayerInput', player: 'PlayerState', state: 'GameState') -> Tuple[bool, str]:
        
        return_message = None
        error_raised = False

        if input.move_type == MoveType.BUY_PET:
            
            # Check if it is not in the range of the shop pet items
            # Check if it is not in the range of the number of pet slots that a player has
            # Check if the player has enough currency

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
        return True, return_message 
