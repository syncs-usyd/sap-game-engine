from typing import Dict, List, Optional

from submissionhelper.info.playerpetinfo import PlayerPetInfo
from submissionhelper.info.shopfoodinfo import ShopFoodInfo
from submissionhelper.info.shoppetinfo import ShopPetInfo


class PlayerInfo:
    def __init__(self, dict: Dict):
        # Refers to the number of lives you have left.
        # Once this reaches 0 YOU ARE ELIMINATED.
        self.health: int = int(dict["health"])

        # Refers to the number of coins you have left in
        # the current buy round. The default is 10 at the
        # start of the round but you can get bonus coins
        # with certain pets. 
        self.coins: int = int(dict["coins"])

        # Contains the info of your current pet lineup
        # Note: the list will contain None. None means there is
        # no pet in that position.
        # Also, the size of pets is always 5 (representing the 5 slots)
        self.pets: List[Optional['PlayerPetInfo']] = [PlayerPetInfo(pet_dict) if pet_dict is not None else None for pet_dict in dict["pets"]]

        # Contains the info of the current pets in the shop
        # Note: if you buy all the pets in the shop, this will be an empty list
        # Also, as the rounds progress, the number of pets in the shop also increases
        self.shop_pets: List['ShopPetInfo'] = [ShopPetInfo(pet_dict) for pet_dict in dict["shop_pets"]]

        # Contains the info of the current foods in the shop
        # Note: if you buy all the foods in the shop, this will be an empty list
        # Also, as the rounds progress, the number of foods in the shop also increases
        self.shop_foods: List['ShopFoodInfo'] = [ShopFoodInfo(food_dict) for food_dict in dict["shop_foods"]]


    def __repr__(self) -> str:
        printable = "Player Info:\n"
        printable += "------------\n"

        printable += f"Health: {self.health}\n"
        printable += f"Coins: {self.coins}\n"

        printable += "Pets: {\n"
        for i, pet in enumerate(self.pets):
            printable += f"    Pet {i}: "
            printable += "{\n"
            for line in repr(pet).splitlines():
                printable += f"        {line}\n"
            printable += "    }\n"
        printable += "}\n"

        printable += "Shop Pets: {\n"
        for i, shop_pet in enumerate(self.shop_pets):
            printable += f"    Pet {i}: "
            printable += "{\n"
            for line in repr(shop_pet).splitlines():
                printable += f"        {line}\n"
            printable += "    }\n"
        printable += "}\n"

        printable += "Shop Foods: {\n"
        for i, shop_food in enumerate(self.shop_foods):
            printable += f"    Pet {i}: "
            printable += "{\n"
            for line in repr(shop_food).splitlines():
                printable += f"        {line}\n"
            printable += "    }\n"
        printable += "}\n"

        printable += "------------"

        return printable
