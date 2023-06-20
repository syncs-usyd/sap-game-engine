from copy import deepcopy
from random import choice, randint, shuffle
from typing import List, Optional

from engine.config.foodconfig import FOOD_CONFIG, TIER_FOOD, FoodType, FoodConfig
from engine.config.gameconfig import NUM_PLAYERS, PET_POSITIONS, STARTING_COINS, STARTING_HEALTH
from engine.config.petconfig import PET_CONFIG, TIER_PETS, PetType
from engine.config.roundconfig import RoundConfig
from engine.game.abilitytype import AbilityType
from engine.state.gamestate import GameState
from engine.state.petstate import PetState


class PlayerState:
    def __init__(self, player_num: int, state: 'GameState'):
        self.player_num = player_num
        self.state = state

        self.health = STARTING_HEALTH
        self.pets: List[Optional['PetState']] = [None] * PET_POSITIONS

        self.shop_pets: List['PetState'] = []
        self.shop_foods: List['FoodConfig'] = []
        self.shop_perm_health_bonus = 0
        self.shop_perm_attack_bonus = 0

        self.battle_order = [i for i in range(NUM_PLAYERS) if i != player_num]
        shuffle(self.battle_order)
        self.next_battle_index = 0

    def start_new_round(self):
        self.prev_health = self.health
        self.prev_pets = deepcopy(self.pets)

        self.coins = STARTING_COINS
        self.reset_shop_options()
        for pet in self.pets:
            if pet is not None:
                pet.start_new_round()

    # Round robin through battle order until the next alive player is found
    def get_challenger(self, increment_index = True) -> 'PlayerState':
        i = self.next_battle_index
        while True:
            challenger = self.state.players[self.battle_order[i]]
            i = (i + 1) % NUM_PLAYERS

            if challenger.is_alive():
                if increment_index: self.next_battle_index = i
                return challenger

    def reset_shop_options(self):
        round_config = RoundConfig.get_round_config(self.state.round)

        self.shop_pets = []
        for _ in range(round_config.NUM_SHOP_PETS):
            pet_config = PET_CONFIG[self._get_random_pet(round_config.MAX_SHOP_TIER)]
            health = pet_config.BASE_HEALTH + self.shop_perm_health_bonus
            attack = pet_config.BASE_ATTACK + self.shop_perm_attack_bonus
            self.shop_pets.append(PetState(health, attack, pet_config))

        self.shop_foods = []
        for _ in range(round_config.NUM_SHOP_FOODS):
            food_config = FOOD_CONFIG[self._get_random_food(round_config.MAX_SHOP_TIER)]
            self.shop_foods.append(food_config)

    def is_alive(self) -> bool:
        return self.health > 0

    def get_view_for_self(self) -> dict:
        return {
            "health": self.health,
            "coins": self.coins,
            "pets": [pet.get_view_for_self() if pet is not None else None for pet in self.pets],
            "shop_pets": [pet.get_view_for_shop() for pet in self.shop_pets],
            "shop_foods": [food.FOOD_NAME for food in self.shop_foods]
        }

    def get_view_for_others(self) -> dict:
        return {
            "health": self.prev_health,
            "pets": [pet.get_view_for_others() if pet is not None else None for pet in self.prev_pets]
        }

    def _get_random_pet(self, max_shop_tier: int) -> 'PetType':
        return self._get_random_from_config_tiers(TIER_PETS, max_shop_tier)

    def _get_random_food(self, max_shop_tier: int) -> 'FoodType':
        return self._get_random_from_config_tiers(TIER_FOOD, max_shop_tier)

    # Simple probability. Every pet/food has an equal chance among the currently
    # allowed tiers
    def _get_random_from_config_tiers(self, config_tiers, max_shop_tier: int):
        total_num = 0
        for tier in range(max_shop_tier):
            total_num += len(config_tiers[tier])

        global_index = randint(0, total_num - 1)
        for tier in range(max_shop_tier):
            if global_index < len(config_tiers[tier]):
                return config_tiers[tier][global_index]
            else:
                global_index -= len(config_tiers[tier])