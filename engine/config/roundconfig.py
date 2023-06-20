class RoundConfig:
    @staticmethod
    def get_round_config(round: int) -> 'RoundConfig':
        return ROUND_CONFIG[round] if round < len(ROUND_CONFIG) else ROUND_CONFIG[-1]

    def __init__(self,
                 round_num: int,
                 max_pet_tier: int,
                 pet_tier_probabilities: list[int],
                 num_shop_pets: int,
                 num_shop_item: int):
        self.MAX_PET_TIER = max_pet_tier
        self.pet_tier_probabilities = pet_tier_probabilities

ROUND_CONFIG = [
    RoundConfig(round_num = 1,
                max_pet_tier = 1,
                pet_tier_probabilities = [100, 0, 0, 0, 0, 0],
                num_shop_pets = 3,
                num_shop_item = 1),

    RoundConfig(round_num = 2,
                max_pet_tier = 1,
                pet_tier_probabilities = [100, 0, 0, 0, 0, 0],
                num_shop_pets = 3,
                num_shop_item = 1),

    RoundConfig(round_num = 3,
                max_pet_tier = 2,
                pet_tier_probabilities = [0, 100, 0, 0, 0, 0],
                num_shop_pets = 3,
                num_shop_item = 1),


    RoundConfig(round_num = 4,
                max_pet_tier = 2,
                pet_tier_probabilities = [0, 100, 0, 0, 0, 0],
                num_shop_pets = 3,
                num_shop_item = 1),


    RoundConfig(round_num = 5,
                max_pet_tier = 3,
                pet_tier_probabilities = [0, 0, 100, 0, 0, 0],
                num_shop_pets = 4,
                num_shop_item = 2),


    RoundConfig(round_num = 6,
                max_pet_tier = 3,
                pet_tier_probabilities = [0, 0, 100, 0, 0, 0],
                num_shop_pets = 4,
                num_shop_item = 2),


    RoundConfig(round_num = 7,
                max_pet_tier = 4,
                pet_tier_probabilities = [0, 0, 0, 100, 0, 0],
                num_shop_pets = 5,
                num_shop_item = 2),


    RoundConfig(round_num = 8,
                max_pet_tier = 4,
                pet_tier_probabilities = [0, 0, 0, 100, 0, 0],
                num_shop_pets = 5,
                num_shop_item = 2),


    RoundConfig(round_num = 9,
                max_pet_tier = 5,
                pet_tier_probabilities = [0, 0, 0, 0, 100, 0],
                num_shop_pets = 5,
                num_shop_item = 2),


    RoundConfig(round_num = 10,
                max_pet_tier = 5,
                pet_tier_probabilities = [0, 0, 0, 0, 100, 0],
                num_shop_pets = 5,
                num_shop_item = 2),


    RoundConfig(round_num = 11,
                max_pet_tier = 6,
                pet_tier_probabilities = [0, 0, 0, 0, 0, 100],
                num_shop_pets = 5,
                num_shop_item = 2),
]
