from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine.config.foodconfig import FoodConfig
    from engine.state.gamestate import GameState


class FoodState:
    def __init__(self, food_config: 'FoodConfig', state: 'GameState'):
        self.id = state.get_id()
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
        return f"{self.food_config.FOOD_NAME}:{self.id}"
