from enum import Enum


class AbilityType(Enum):
    BUY = 1 # When a pet is bought from the shop
    SELL = 2 # When a pet is sold
    LEVEL_UP = 3 # When a pet is leveled up
    HURT = 4 # When a pet takes damage. Faint counts as hurt
    FRIEND_AHEAD_ATTACK = 5 # When a friendly pet directly in front attacks
    BUY_ROUND_START = 6 # When the buy round starts
    BATTLE_ROUND_START = 7 # When the battle round starts
    FRIEND_SUMMONED = 8 # When a friendly pet is summoned. Buy counts as summoned
    FRIEND_ATE_FOOD = 9