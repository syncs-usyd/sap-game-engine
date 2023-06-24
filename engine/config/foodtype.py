from enum import Enum


class FoodType(Enum):
    APPLE = 1
    HONEY = 2
    SLEEPING_PILL = 3
    MEAT_BONE = 4
    CUPCAKE = 5
    SALAD_BOWL = 6
    GARLIC = 7
    CANNED_FOOD = 8
    PEAR = 9

TIER_FOOD = [
    [FoodType.APPLE, FoodType.HONEY],
    [FoodType.SLEEPING_PILL, FoodType.MEAT_BONE, FoodType.CUPCAKE],
    [FoodType.SALAD_BOWL, FoodType.GARLIC],
    [FoodType.CANNED_FOOD, FoodType.PEAR]
]
