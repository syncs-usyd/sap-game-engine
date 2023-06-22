from typing import Dict, Optional

from submissionhelper.info.foodtype import FoodType
from submissionhelper.info.pettype import PetType


class OtherPlayerPetInfo:
    def __init__(self, dict: Dict):
        # Says the type of the pet
        # Check the game engine for more complex config
        self.type: 'PetType' = PetType.get_pet_type(dict["type"])

        # Represents the amount of health the pet had going
        # into the last battle round.
        # Note: this does contain some temporary buffs (ex: cupcake)
        self.health: int = int(dict["health"])

        # Represents the amount of attack the pet had going
        # into the last battle round.
        # Note: this does contain some temporary buffs (ex: cupcake)
        self.attack: int = int(dict["attack"])

        # Represents the level of the pet going into
        # the last battle round
        self.level: int = int(dict["level"])

        # Represents the pet's carried food going
        # into the last battle round
        # Note: this can be None 
        self.carried_food: Optional['FoodType'] = FoodType.get_food_type(dict["carried_food"]) if dict["carried_food"] is not None else None
