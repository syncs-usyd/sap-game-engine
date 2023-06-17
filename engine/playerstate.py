from copy import deepcopy
from random import shuffle
from typing import List, Tuple
from engine.config import NUM_PLAYERS, PET_POSITIONS, REROLL_COST, ROUND_CONFIG, STARTING_COINS, STARTING_HEALTH, FoodConfig
from engine.gamestate import GameState
from engine.petstate import PetState


class PlayerState:
    def __init__(self, player_num: int) -> 'PlayerState':
        self.player_num = player_num
        self.health = STARTING_HEALTH
        self.pets: List['PetState'] = [None] * PET_POSITIONS
        self.battle_order = [i for i in range(NUM_PLAYERS) if i != player_num]
        shuffle(self.battle_order)
        self.next_battle_index = 0

    def start_new_round(self, round: int):
        self.prev_health = self.health
        self.prev_pets = deepcopy(self.pets)

        self.coins = STARTING_COINS + self.get_bonus_coins()
        self.shop_pets, self.shop_foods = self.get_shop_options(round)
        for pet in self.pets:
            if pet != None: pet.start_new_round(round)

    # Round robin through battle order until the next alive player is found
    def get_challenger(self, state: 'GameState', increment_index = True) -> 'PlayerState':
        i = self.next_battle_index
        while True:
            challenger = state.players[self.battle_order[i]]
            i = (i + 1) % NUM_PLAYERS

            if challenger.is_alive():
                if increment_index: self.next_battle_index = i
                return challenger

    def reroll(self, round: int):
        self.shop_options = self.get_shop_options(round)
        self.coins -= REROLL_COST

    def get_bonus_coins(self) -> int:
        return 0

    def get_shop_options(self, round: int) -> Tuple[List['PetState'], List['FoodConfig']]:
        round_config = ROUND_CONFIG[round]
        pass

    def is_alive(self) -> bool:
        return self.health > 0

    def get_view_for_self(self) -> dict:
        return {
            "health": self.health,
            "coins": self.coins,
            "pets": [pet.get_view_for_self() if pet != None else None for pet in self.pets],
            "shop_pets": [pet.get_view_for_self() for pet in self.shop_pets],
            "shop_foods": [food.FOOD_NAME for food in self.shop_foods]
        }

    def get_view_for_others(self) -> dict:
        return {
            "health": self.prev_health,
            "pets": [pet.get_view_for_others() if pet != None else None for pet in self.prev_pets]
        }