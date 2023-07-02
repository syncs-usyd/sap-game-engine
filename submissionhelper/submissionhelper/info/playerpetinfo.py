from typing import Dict, Optional

from submissionhelper.info.foodtype import FoodType
from submissionhelper.info.pettype import PetType


class PlayerPetInfo:
    def __init__(self, dict: Dict):
        self.id: int = int(dict["id"])

        # Says the type of the pet
        # Check the game engine for more complex config
        self.type: 'PetType' = PetType.get_pet_type(dict["type"])

        # Represents the amount of health the pet has going
        # into the next battle round.
        # Note: this does contain some temporary buffs (ex: cupcake)
        self.health: int = int(dict["health"])

        # Represents the amount of attack the pet has going
        # into the next battle round.
        # Note: this does contain some temporary buffs (ex: cupcake)
        self.attack: int = int(dict["attack"])

        # Represents the level of the pet
        self.level: int = int(dict["level"])

        # Represents the progress towards the next level
        # To reach level 2, sub level has to reach 2
        # To reach level 3, sub level has to reach 3
        self.sub_level: int = int(dict["sub_level"])

        # Represents the pet's carried food
        # Note: this can be None 
        self.carried_food: Optional['FoodType'] = FoodType.get_food_type(dict["carried_food"]) if dict["carried_food"] is not None else None

    def __repr__(self) -> str:
        printable = "Player Pet Info:\n"
        printable += "------------\n"

        printable += f"Id: {self.id}\n"
        printable += f"Type: {self.type}\n"
        printable += f"Health: {self.health}\n"
        printable += f"Attack: {self.attack}\n"
        printable += f"Level: {self.level}\n"
        printable += f"Sub Level: {self.sub_level}\n"
        printable += f"Carried Food: {self.carried_food}\n"

        printable += "------------"

        return printable
