from enum import Enum


class MoveType(Enum):
    BUY_PET = 1
    BUY_FOOD = 2
    UPGRADE_PET_FROM_SHOP = 3
    UPGRADE_PET_FROM_PETS = 4
    SELL_PET = 5
    REROLL = 6
    FREEZE_PET = 7
    FREEZE_FOOD = 8
    SWAP_PET = 9
    END_TURN = 10
