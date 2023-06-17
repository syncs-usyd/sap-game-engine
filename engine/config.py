from enum import Enum


# Input helper config
CORE_DIRECTORY = "./"
OPEN_PIPE_TIMEOUT_SECONDS = 5
WRITE_PIPE_TIMEOUT_SECONDS = 5
READ_PIPE_TIMEOUT_SECONDS = 5

# Game config
NUM_PLAYERS = 5
STARTING_HEALTH = 10
STARTING_COINS = 10
PET_POSITIONS = 5
MAX_MOVES_PER_ROUND = 20
REROLL_COST = 1
LEVEL_2_CUTOFF = 2
LEVEL_3_CUTOFF = 5

# Round specific config
class RoundConfig:
    def __init__(self, round_num: int,
                 max_pet_tier: int,
                 ) -> 'RoundConfig':
        self.ROUND_NUM = round_num
        self.MAX_PET_TIER = max_pet_tier

ROUND_CONFIG = [
    RoundConfig(round_num = 1,
                max_pet_tier = 1),

    RoundConfig(round_num = 2,
                max_pet_tier = 1),

    RoundConfig(round_num = 3,
                max_pet_tier = 2),

    RoundConfig(round_num = 4,
                max_pet_tier = 2),

    RoundConfig(round_num = 5,
                max_pet_tier = 3),

    RoundConfig(round_num = 6,
                max_pet_tier = 3),

    RoundConfig(round_num = 7,
                max_pet_tier = 4),

    RoundConfig(round_num = 8,
                max_pet_tier = 4),

    RoundConfig(round_num = 9,
                max_pet_tier = 5),

    RoundConfig(round_num = 10,
                max_pet_tier = 5),

    RoundConfig(round_num = 11,
                max_pet_tier = 6),
]

# Pets config
class PetConfig:
    def __init__(self, pet_name, tier, base_health, base_defense, base_buy_cost) -> 'PetConfig':
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

# Food config
class FoodConfig:
    def __init__(self, food_name, tier, base_buy_cost) -> 'FoodConfig':
        self.FOOD_NAME = food_name
        self.TIER = tier
        self.BASE_BUY_COST = base_buy_cost

class Food(Enum):
    APPLE = 1

FOOD_CONFIG = {
    Food.APPLE: FoodConfig(food_name = "Apple",
                           tier = 1,
                           base_buy_cost = 1)
}

TIER_FOOD = [
    [Food.APPLE],
    [],
    [],
    [],
    [],
    []
]