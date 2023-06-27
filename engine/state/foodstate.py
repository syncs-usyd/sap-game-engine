from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine.config.foodconfig import FoodConfig
from engine.state.countablestates import CountableStates

class FoodState(CountableStates):
    def __init__(self, food_config: 'FoodConfig'):
        super()
        self.food_config = food_config
        self.cost = food_config.BUY_COST
        self.is_frozen = False

    def get_view_for_shop(self) -> dict:
        return {
            "id": self.id,
            "type": self.food_config.FOOD_NAME,
            "is_frozen": self.is_frozen,
            "cost": self.cost
        }

    def __repr__(self) -> str:
        # TODO: add id to this as well
        return self.food_config.FOOD_NAME
