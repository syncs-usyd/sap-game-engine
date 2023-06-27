from typing import Dict

from submissionhelper.info.foodtype import FoodType


class ShopFoodInfo:
    def __init__(self, dict: Dict):
        self.id: int = int(dict["id"])

        # Says the type of the food
        self.type: 'FoodType' = FoodType.get_food_type(dict["type"])

        # Says whether the shop food is frozen
        # Note: frozen shop foods are kept even when rerolling
        # and stay when a new shop round begins
        self.is_frozen: bool = bool(dict["is_frozen"])

        # The number of coins it costs to buy the food
        self.cost: int = int(dict["cost"])

    def __repr__(self) -> str:
        printable = "Shop Food Info:\n"
        printable += "------------\n"

        printable += f"Id: {self.id}\n"
        printable += f"Type: {self.type}\n"
        printable += f"Is Frozen: {self.is_frozen}\n"
        printable += f"Cost: {self.cost}\n"

        printable += "------------"

        return printable
