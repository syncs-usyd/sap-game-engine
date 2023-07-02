from typing import Dict

from submissionhelper.info.pettype import PetType


class ShopPetInfo:
    def __init__(self, dict: Dict):
        self.id: int = int(dict["id"])

        # Says the type of the pet
        # Check the game engine for more complex config
        self.type: 'PetType' = PetType.get_pet_type(dict["type"])

        # Represents the amount of health the pet has
        self.health: int = int(dict["health"])

        # Represents the amount of attack the pet has
        self.attack: int = int(dict["attack"])

        # Says whether the shop pet is frozen
        # Note: frozen shop pets are kept even when rerolling
        # and stay when a new shop round begins
        self.is_frozen: bool = bool(dict["is_frozen"])

        # The number of coins it costs to buy the pet
        self.cost: int = int(dict["cost"])

    def __repr__(self) -> str:
        printable = "Shop Pet Info:\n"
        printable += "------------\n"

        printable += f"Id: {self.id}\n"
        printable += f"Type: {self.type}\n"
        printable += f"Health: {self.health}\n"
        printable += f"Attack: {self.attack}\n"
        printable += f"Is Frozen: {self.is_frozen}\n"
        printable += f"Cost: {self.cost}\n"

        printable += "------------"

        return printable
