from engine.config.foodconfig import FoodConfig
from engine.state.countablestates import CountableStates

class FoodState(CountableStates):
    def __init__(self, food_config: 'FoodConfig'):
        super()
        self.food_config = food_config
        self.is_frozen = False

    def get_view_for_shop(self) -> dict:
        return {
            "id": self.id,
            "type": self.food.FOOD_NAME,
            "is_frozen": self.is_frozen,
            "cost": self.food_config.BUY_COST
        }
