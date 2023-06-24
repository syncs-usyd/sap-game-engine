from enum import Enum


class FoodType(Enum):
    @staticmethod
    def get_food_type(food_name: str) -> 'FoodType':
        upper_snake_case = food_name.upper().replace(" ", "_")
        return FoodType[upper_snake_case]

    APPLE = 1
    HONEY = 2
    SLEEPING_PILL = 3
    MEAT_BONE = 4
    CUPCAKE = 5
    SALAD_BOWL = 6
    GARLIC = 7
    CANNED_FOOD = 8
    PEAR = 9
