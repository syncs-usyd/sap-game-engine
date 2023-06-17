from enum import Enum


class PetConfig:
    def __init__(self,
                 pet_name,
                 tier,
                 base_health,
                 base_defense,
                 base_buy_cost):
        self.PET_NAME = pet_name
        self.TIER = tier
        self.BASE_HEALTH = base_health
        self.BASE_DEFENSE = base_defense
        self.BASE_BUY_COST = base_buy_cost

class Pet(Enum):
    FISH = 1

PET_CONFIG = {
    Pet.FISH: PetConfig(pet_name = "Fish",
                        tier = 1,
                        base_health = 3,
                        base_defense = 3,
                        base_buy_cost = 2)
}

TIER_PETS = [
    [Pet.FISH],
    [],
    [],
    [],
    [],
    []
]