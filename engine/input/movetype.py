from enum import Enum


class MoveType(Enum):
    BuyPet = 1
    BuyItem = 2
    UpgradePet = 3
    SellPet = 4
    Reroll = 5
    FreezePet = 6
    FreezeItem = 7
    SwapPet = 8
    EndTurn = 9