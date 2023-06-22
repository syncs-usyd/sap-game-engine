from typing import Dict

from submissionhelper.info.foodtype import FoodType


class ShopFoodInfo:
    def __init__(self, dict: Dict):
        # Says the type of the food
        self.type: 'FoodType' = FoodType.get_food_type(dict["type"])

        # Says whether the shop food is frozen
        # Note: frozen shop foods are kept even when rerolling
        # and stay when a new shop round begins
        self.is_frozen: bool = bool(dict["is_frozen"])

        # The number of coins it costs to buy the food
        self.cost: int = int(dict["cost"])
