class RoundConfig:
    @staticmethod
    def get_round_config(round: int) -> 'RoundConfig':
        return ROUND_CONFIG[round] if round < len(ROUND_CONFIG) else ROUND_CONFIG[-1]

    def __init__(self,
                 round_num: int,
                 max_shop_tier: int,
                 num_shop_pets: int,
                 num_shop_foods: int,
                 health_lost: int):
        self.MAX_SHOP_TIER = max_shop_tier
        self.NUM_SHOP_PETS = num_shop_pets
        self.NUM_SHOP_FOODS = num_shop_foods
        self.HEALTH_LOST = health_lost

ROUND_CONFIG = [
    RoundConfig(round_num = 1,
                max_shop_tier = 1,
                num_shop_pets = 3,
                num_shop_foods = 1,
                health_lost = 1),

    RoundConfig(round_num = 2,
                max_shop_tier = 1,
                num_shop_pets = 3,
                num_shop_foods = 1,
                health_lost = 1),

    RoundConfig(round_num = 3,
                max_shop_tier = 2,
                num_shop_pets = 3,
                num_shop_foods = 1,
                health_lost = 2),

    RoundConfig(round_num = 4,
                max_shop_tier = 2,
                num_shop_pets = 3,
                num_shop_foods = 1,
                health_lost = 2),

    RoundConfig(round_num = 5,
                max_shop_tier = 3,
                num_shop_pets = 4,
                num_shop_foods = 2,
                health_lost = 2),

    RoundConfig(round_num = 6,
                max_shop_tier = 3,
                num_shop_pets = 4,
                num_shop_foods = 2,
                health_lost = 2),

    RoundConfig(round_num = 7,
                max_shop_tier = 4,
                num_shop_pets = 4,
                num_shop_foods = 2,
                health_lost = 3),

    RoundConfig(round_num = 8,
                max_shop_tier = 4,
                num_shop_pets = 4,
                num_shop_foods = 2,
                health_lost = 3),

    RoundConfig(round_num = 9,
                max_shop_tier = 4, # Real game this is 5
                num_shop_pets = 4,
                num_shop_foods = 2,
                health_lost = 3),

    RoundConfig(round_num = 10,
                max_shop_tier = 4, # Real game this is 5
                num_shop_pets = 4,
                num_shop_foods = 2,
                health_lost = 3),

    RoundConfig(round_num = 11,
                max_shop_tier = 4, # Real game this is 6
                num_shop_pets = 5,
                num_shop_foods = 2,
                health_lost = 3),
]
