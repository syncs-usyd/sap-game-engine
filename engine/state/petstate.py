from engine.config.foodconfig import FoodConfig
from engine.config.gameconfig import LEVEL_2_CUTOFF, LEVEL_3_CUTOFF
from engine.config.petconfig import PetConfig


class PetState:
    def __init__(self, health: int, defense: int, pet_config: 'PetConfig') -> 'PetState':
        self.perm_health = health
        self.perm_defense = defense
        self.pet_config = pet_config
        self.carried_food: 'FoodConfig' = None 
        self.sub_level = 1

    def start_new_round(self, round: int):
        self.prev_health = self.perm_health
        self.prev_defense = self.perm_defense
        self.prev_carried_food = self.carried_food
        self.prev_level = self.get_level()
        self.health = self.perm_health
        self.defense = self.perm_defense

    def get_level(self):
        if self.sub_level == LEVEL_3_CUTOFF:
            return 3
        elif self.sub_level >= LEVEL_2_CUTOFF:
            return 2
        else:
            return 1

    def get_sub_level_progress(self):
        level = self.get_level()
        if level == 3:
            return 0
        elif level == 2:
            return self.sub_level - LEVEL_2_CUTOFF
        else:
            return self.sub_level

    def add_food(self, food: 'FoodConfig'):
        # Some food have permanent effects (so update both health & perm_health and defense & perm_defense)
        # Some food is more like an item so add it to carried_food
        # Some food is entirely temporary (so update only health/defense)
        pass

    def get_view_for_self(self) -> dict:
        return {
            "type": self.pet_config.PET_NAME,
            "health": self.health,
            "defense": self.defense,
            "level": self.get_level(),
            "sub_level": self.get_sub_level_progress(),
            "carried_food": self.carried_food.FOOD_NAME if self.carried_food != None else None
        }

    def get_view_for_others(self) -> dict:
        return {
            "type": self.pet_config.PET_NAME,
            "health": self.prev_health,
            "defense": self.prev_defense,
            "level": self.prev_level,
            "carried_food": self.prev_carried_food.FOOD_NAME if self.prev_carried_food != None else None
        }