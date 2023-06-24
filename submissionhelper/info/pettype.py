from enum import Enum


class PetType(Enum):
    @staticmethod
    def get_pet_type(pet_name: str) -> 'PetType':
        upper_snake_case = pet_name.upper().replace(" ", "_")
        return PetType[upper_snake_case]

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
    RAM = 24
    BEE = 25
    ZOMBIE_CRICKET = 26
