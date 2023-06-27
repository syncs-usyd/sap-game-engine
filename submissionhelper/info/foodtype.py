from enum import Enum


class FoodType(Enum):
    @staticmethod
    def get_food_type(food_name: str) -> 'FoodType':
        upper_snake_case = food_name.upper().replace(" ", "_")
        return FoodType[upper_snake_case]

    APPLE = 1
    HONEY = 2
    MEAT_BONE = 3
    CUPCAKE = 4
    SALAD_BOWL = 5
    GARLIC = 6
    CANNED_FOOD = 7
    PEAR = 8
