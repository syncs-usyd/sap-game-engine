from enum import Enum


class FoodConfig:
    def __init__(self,
                 food_name,
                 tier,
                 base_buy_cost):
        self.FOOD_NAME = food_name
        self.TIER = tier
        self.BASE_BUY_COST = base_buy_cost

class FoodType(Enum):
    APPLE = 1

FOOD_CONFIG = {
    FoodType.APPLE: FoodConfig(food_name = "Apple",
                           tier = 1,
                           base_buy_cost = 1)
}

TIER_FOOD = [
    [FoodType.APPLE],
    [],
    [],
    [],
    [],
    []
]