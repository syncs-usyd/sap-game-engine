from enum import Enum


class MoveType(Enum):
    BUY_PET = 1
    BUY_ITEM = 2
    UPGRADE_PET = 3
    SELL_PET = 4
    REROLL = 5
    FREEZE_PET = 6
    FREEZE_ITEM = 7
    SWAP_PET = 8
    END_TURN = 9
