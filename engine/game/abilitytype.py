from enum import Enum


class AbilityType(Enum):
    BUY = 1 # Triggers when a pet is bought from the shop
    SELL = 2 # Triggers when a pet is sold
    LEVEL_UP = 3 # Triggers when a pet is leveled up
    HURT = 4 # Triggers when a pet takes damage. Faint counts as hurt
    FRIEND_AHEAD_ATTACK = 5 # Triggers when a friendly pet directly in front attacks
    BUY_ROUND_START = 6 # Triggers when the buy round starts
    BATTLE_ROUND_START = 7 # Triggers when the battle round starts
    FRIEND_SUMMONED = 8 # Triggers when a friendly pet is summoned. Buy counts as summoned
    FRIEND_ATE_FOOD = 9 # Triggers when a friend eats food
    BEFORE_ATTACK = 10 # Triggers before you attack an enemy
    AFTER_ATTACK = 11 # Triggers after you attack an enemy
    KILLED_ENEMY = 12 # Triggers when you kill an enemy pet