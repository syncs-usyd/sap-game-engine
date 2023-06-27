from enum import Enum


class FoodType(Enum):
    APPLE = 1
    HONEY = 2
    MEAT_BONE = 3
    CUPCAKE = 4
    SALAD_BOWL = 5
    GARLIC = 6
    CANNED_FOOD = 7
    PEAR = 8

TIER_FOOD = [
    [FoodType.APPLE, FoodType.HONEY],
    [FoodType.MEAT_BONE, FoodType.CUPCAKE],
    [FoodType.SALAD_BOWL, FoodType.GARLIC],
    [FoodType.CANNED_FOOD, FoodType.PEAR]
]
