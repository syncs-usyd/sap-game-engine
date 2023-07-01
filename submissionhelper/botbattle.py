from json import dumps, loads
from typing import Optional

from submissionhelper.info.gameinfo import GameInfo
from submissionhelper.info.playerpetinfo import PlayerPetInfo
from submissionhelper.info.shopfoodinfo import ShopFoodInfo
from submissionhelper.info.shoppetinfo import ShopPetInfo


class BotBattle:
    def __init__(self):
        self._from_engine = open("./io/from_engine.pipe", "r", encoding = "utf-8") 
        self._to_engine = open("./io/to_engine.pipe", "w", encoding = "utf-8")
        self._game_info: Optional['GameInfo'] = None

    def get_game_info(self) -> 'GameInfo':
        dict_game_info = self._read_from_pipe()
        self._game_info = GameInfo(dict_game_info)
        return self._game_info

    # Buy the provided shop pet and place it in your pet lineup at the
    # provided position
    # Note: PlayerInfo.pets[position] must be None 
    def buy_pet(self, shop_pet: 'ShopPetInfo', position: int):
        dict_move = {
            "move_type": "BUY_PET",
            "index_from": self._game_info.player_info.shop_pets.index(shop_pet),
            "index_to": position
        }
        self._write_to_pipe(dict_move)

    # Buy the provided shop food
    # Some foods are targeted (ex: Apple), in this case,
    # you must also provide the pet you are targeting
    def buy_food(self, shop_food: 'ShopFoodInfo', target_pet: Optional['PlayerPetInfo'] = None):
        dict_move = {
            "move_type": "BUY_FOOD",
            "index_from": self._game_info.player_info.shop_foods.index(shop_food),
            "index_to": self._game_info.player_info.pets.index(target_pet) if target_pet is not None else None
        }
        self._write_to_pipe(dict_move)

    # Buy the pet from the shop and use it to level up
    # the target pet
    def level_pet_from_shop(self, shop_pet: 'ShopPetInfo', pet_to_level_up: 'PlayerPetInfo'):
        dict_move = {
            "move_type": "UPGRADE_PET_FROM_SHOP",
            "index_from": self._game_info.player_info.shop_pets.index(shop_pet),
            "index_to": self._game_info.player_info.pets.index(pet_to_level_up)
        }
        self._write_to_pipe(dict_move)

    # Buy the pet from the shop and use it to level up
    # the target pet
    def level_pet_from_pets(self, pet_to_use: 'PlayerPetInfo', pet_to_level_up: 'PlayerPetInfo'):
        dict_move = {
            "move_type": "UPGRADE_PET_FROM_PETS",
            "index_from": self._game_info.player_info.pets.index(pet_to_use),
            "index_to": self._game_info.player_info.pets.index(pet_to_level_up)
        }
        self._write_to_pipe(dict_move)

    # Sell the pet and receive its level in coins
    def sell_pet(self, pet: 'PlayerPetInfo'):
        dict_move = {
            "move_type": "SELL_PET",
            "index_from": self._game_info.player_info.pets.index(pet),
            "index_to": None
        }
        self._write_to_pipe(dict_move)

    # Refresh the shop (costs 1 coin)
    # Note: this doesn't remove frozen pets or food
    def reroll_shop(self):
        dict_move = {
            "move_type": "REROLL",
            "index_from": None,
            "index_to": None
        }
        self._write_to_pipe(dict_move)

    # Freeze the specified pet
    # Note: this means this pet wont be refreshed at the end of the round
    # or when rerolling the shop
    def freeze_pet(self, shop_pet: 'ShopPetInfo'):
        dict_move = {
            "move_type": "FREEZE_PET",
            "index_from": self._game_info.player_info.shop_pets.index(shop_pet),
            "index_to": None
        }
        self._write_to_pipe(dict_move)

    # Freeze the specified food
    # Note: this means this food wont be refreshed at the end of the round
    # or when rerolling the shop
    def freeze_food(self, shop_food: 'ShopFoodInfo'):
        dict_move = {
            "move_type": "FREEZE_FOOD",
            "index_from": self._game_info.player_info.shop_foods.index(shop_food),
            "index_to": None
        }
        self._write_to_pipe(dict_move)

    # Unfreeze the specified pet
    # Note: this means this pet WILL be refreshed at the end of the round
    # and when rerolling the shop
    def unfreeze_pet(self, shop_pet: 'ShopPetInfo'):
        dict_move = {
            "move_type": "UNFREEZE_PET",
            "index_from": self._game_info.player_info.shop_pets.index(shop_pet),
            "index_to": None
        }
        self._write_to_pipe(dict_move)

    # Unfreeze the specified food
    # Note: this means this food WILL be refreshed at the end of the round
    # and when rerolling the shop
    def unfreeze_food(self, shop_food: 'ShopFoodInfo'):
        dict_move = {
            "move_type": "UNFREEZE_FOOD",
            "index_from": self._game_info.player_info.shop_foods.index(shop_food),
            "index_to": None
        }
        self._write_to_pipe(dict_move)

    # Swap the positions of the two pets within your lineup
    # Note: its totally ok for the indices to point to None
    def swap_pets(self, pet_a_index: int, pet_b_index: int):
        dict_move = {
            "move_type": "SWAP_PET",
            "index_from": pet_a_index,
            "index_to": pet_b_index
        }   
        self._write_to_pipe(dict_move)

    # End your turn
    def end_turn(self):
        dict_move = {
            "move_type": "END_TURN",
            "index_from": None,
            "index_to": None
        }   
        self._write_to_pipe(dict_move)

    def _read_from_pipe(self):
        json_game_info = ""
        while not json_game_info or json_game_info[-1] != ";":
            json_game_info += self._from_engine.read(1)

        dict_game_info = loads(json_game_info[:-1])
        return dict_game_info

    def _write_to_pipe(self, dict_move):
        dict_move = dumps(dict_move)
        dict_move += ";"
        self._to_engine.write(dict_move)
        self._to_engine.flush()
