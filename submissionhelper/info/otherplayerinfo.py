from typing import Dict, List, Optional

from submissionhelper.info.otherplayerpetinfo import OtherPlayerPetInfo


class OtherPlayerInfo:
    def __init__(self, dict: Dict):
        # Refers to the number of lives the other player has left.
        # Once this reaches 0 THEY ARE ELIMINATED.
        self.health: int = int(dict["health"])

        # Contains the info of the other player's pet lineup
        # from the start of the last battle round
        # Note: the list will contain None. None means there is
        # no pet in that position.
        # Also, the size of pets is always 5 (representing the 5 slots)
        self.pets: List[Optional['OtherPlayerPetInfo']] = [OtherPlayerPetInfo(pet_dict) if pet_dict is not None else None for pet_dict in dict["pets"]]
