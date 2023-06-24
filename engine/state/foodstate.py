from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine.config.foodconfig import FoodConfig


class FoodState:
    def __init__(self, food_config: 'FoodConfig'):
        self.food_config = food_config
        self.is_frozen = False

    def get_view_for_shop(self) -> dict:
        return {
            "type": self.food_config.FOOD_NAME,
            "is_frozen": self.is_frozen,
            "cost": self.food_config.BUY_COST
        }

    def __repr__(self) -> str:
        # TODO: add id to this as well
        return self.food_config.FOOD_NAME
