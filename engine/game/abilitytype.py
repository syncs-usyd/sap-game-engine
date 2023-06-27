from enum import Enum


# Different abilities have different priority
#   - Battle abilities have a set order of execution that can be seen in the battle stage helper
#   - On-demand abilities are executed as soon as they are valid. If multiple on-demand abilities
#     should be executed for the same event, it is done in pet order
class AbilityType(Enum):
    # On-demand; triggers when a pet is bought from the shop
    BUY = 1 

    # On-demand; triggers when a pet is sold
    SELL = 2

    # On-demand; triggers when a pet is leveled up
    LEVEL_UP = 3 

    # Battle ability; triggers when a pet takes damage. Faint counts as hurt
    HURT = 4 

    # Battle ability; triggers when a friendly pet directly in front attacks
    # Note: ability attacks don't trigger this
    FRIEND_AHEAD_ATTACK = 5 

    # On-demand; triggers when the buy round starts
    BUY_ROUND_START = 6

    # Battle ability; triggers when the battle round starts
    BATTLE_ROUND_START = 7

    # On-demand; triggers when a friendly pet is summoned. Buy counts as summoned
    FRIEND_SUMMONED = 8

    # On-demand; triggers when a friend eats food
    FRIEND_ATE_FOOD = 9

    # Battle-ability; triggers before you attack an enemy
    BEFORE_ATTACK = 10

    # Battle-ability; triggers after you attack an enemy
    AFTER_ATTACK = 11

    # Battle-ability; triggers when you kill an enemy pet
    KNOCKOUT = 12

    # Battle-ability; triggers when the pet dies
    FAINTED = 13

    # On-demand; triggers when the buy round ends
    BUY_ROUND_END = 14
