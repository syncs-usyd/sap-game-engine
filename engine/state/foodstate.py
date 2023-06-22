from engine.config.foodconfig import FoodConfig


class FoodState:
    def __init__(self, food_config: 'FoodConfig'):
        self.food_config = food_config
        self.is_frozen = False

    def get_view_for_shop(self) -> dict:
        return {
            "type": self.food.FOOD_NAME,
            "is_frozen": self.is_frozen,
            "cost": self.food_config.BUY_COST
        }
