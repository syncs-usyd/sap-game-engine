from engine.config.foodtype import FoodType
from engine.game.foodeffects import FoodEffects


class FoodConfig:
    def __init__(self,
                 food_name,
                 tier,
                 buy_cost,
                 is_targeted,
                 is_carried,
                 effect_func,):
        self.FOOD_NAME = food_name
        self.TIER = tier
        self.BUY_COST = buy_cost
        self.IS_TARGETED = is_targeted
        self.IS_CARRIED = is_carried
        self.EFFECT_FUNC = effect_func

FOOD_CONFIG = {
    FoodType.APPLE: FoodConfig(food_name = "Apple",
                            tier = 1,
                            buy_cost = 3,
                            is_targeted = True,
                            is_carried = False,
                            effect_func = FoodEffects.apple_effect),

    FoodType.HONEY: FoodConfig(food_name = "Honey",
                            tier = 1,
                            buy_cost = 3,
                            is_targeted = True,
                            is_carried = True,
                            effect_func = None),

    FoodType.MEAT_BONE: FoodConfig(food_name = "Meat Bone",
                            tier = 2,
                            buy_cost = 3,
                            is_targeted = True,
                            is_carried = True,
                            effect_func = None),

    FoodType.CUPCAKE: FoodConfig(food_name = "Cupcake",
                            tier = 2,
                            buy_cost = 3,
                            is_targeted = True,
                            is_carried = False,
                            effect_func = FoodEffects.cupcake_effect),

    FoodType.SALAD_BOWL: FoodConfig(food_name = "Salad Bowl",
                            tier = 3,
                            buy_cost = 3,
                            is_targeted = False,
                            is_carried = False,
                            effect_func = FoodEffects.salad_bowl_effect),

    FoodType.GARLIC: FoodConfig(food_name = "Garlic",
                            tier = 3,
                            buy_cost = 3,
                            is_targeted = True,
                            is_carried = True,
                            effect_func = None),

    FoodType.CANNED_FOOD: FoodConfig(food_name = "Canned Food",
                            tier = 4,
                            buy_cost = 3,
                            is_targeted = False,
                            is_carried = False,
                            effect_func = FoodEffects.canned_food_effect),

    FoodType.PEAR: FoodConfig(food_name = "Pear",
                            tier = 4,
                            buy_cost = 3,
                            is_targeted = True,
                            is_carried = False,
                            effect_func = FoodEffects.pear_effect),
}
