from enum import Enum


class PetType(Enum):
    FISH = 1
    BEAVER = 2
    PIG = 3
    ANT = 4
    MOSQUITO = 5
    CRICKET = 6
    HORSE = 7
    CRAB = 8
    SWAN = 9
    HEDGEHOG = 10
    PEACOCK = 11
    FLAMINGO = 12
    KANGAROO = 13
    SPIDER = 14
    DODO = 15
    BADGER = 16
    DOLPHIN = 17
    GIRAFFE = 18
    BUNNY = 19 
    DOG = 20
    SHEEP = 21
    ELEPHANT = 22
    CAMEL = 23
    SKUNK = 24
    HIPPO = 25
    BISON = 26
    BLOWFISH = 27
    SQUIRREL = 28
    PENGUIN = 29
    RAM = 30
    BEE = 31
    ZOMBIE_CRICKET = 32

TIER_PETS = [
    [PetType.FISH, PetType.BEAVER, PetType.HORSE, PetType.PIG, PetType.ANT, PetType.MOSQUITO, PetType.CRICKET],
    [PetType.CRAB, PetType.SWAN, PetType.HEDGEHOG, PetType.FLAMINGO, PetType.KANGAROO, PetType.SPIDER, PetType.PEACOCK],
    [PetType.DODO, PetType.BADGER, PetType.DOLPHIN, PetType.GIRAFFE, PetType.ELEPHANT, PetType.CAMEL, PetType.BUNNY, PetType.DOG, PetType.SHEEP],
    [PetType.SKUNK, PetType.HIPPO, PetType.BISON, PetType.BLOWFISH, PetType.SQUIRREL, PetType.PENGUIN]
]
