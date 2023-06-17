class RoundConfig:
    @staticmethod
    def get_round_config(round: int) -> 'RoundConfig':
        return ROUND_CONFIG[round] if round < len(ROUND_CONFIG) else ROUND_CONFIG[-1]

    def __init__(self,
                 round_num: int,
                 max_pet_tier: int) -> 'RoundConfig':
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
