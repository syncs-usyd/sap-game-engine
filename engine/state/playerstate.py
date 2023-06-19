from copy import deepcopy
from random import choice, randint, shuffle
from typing import List, Optional

from engine.config.foodconfig import FOOD_CONFIG, TIER_FOOD, FoodConfig
from engine.config.gameconfig import NUM_PLAYERS, PET_POSITIONS, REROLL_COST, STARTING_COINS, STARTING_HEALTH
from engine.config.petconfig import PET_CONFIG, TIER_PETS
from engine.config.roundconfig import RoundConfig
from engine.state.gamestate import GameState
from engine.state.petstate import PetState


class PlayerState:
    def __init__(self, player_num: int):
        self.player_num = player_num

        self.health = STARTING_HEALTH
        self.pets: List[Optional['PetState']] = [None] * PET_POSITIONS

        self.shop_pets: List['PetState'] = []
        self.shop_foods: List['FoodConfig'] = []
        self.shop_perm_health_bonus = 0
        self.shop_perm_attack_bonus = 0

        self.battle_order = [i for i in range(NUM_PLAYERS) if i != player_num]
        shuffle(self.battle_order)
        self.next_battle_index = 0

    def start_new_round(self, round: int):
        self.prev_health = self.health
        self.prev_pets = deepcopy(self.pets)

        self.coins = STARTING_COINS + self._get_bonus_coins()
        self.reset_shop_options(round)
        for pet in self.pets:
            if pet is not None: pet.start_new_round(round)

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
        self.reset_shop_options(round)
        self.coins -= REROLL_COST

    def reset_shop_options(self, round: int):
        round_config = RoundConfig.get_round_config(round)

        # We do a two-level lottery
        # The first random tells us which tier the pet/food is going to come from
        # The second random tells us which pet/food within that tier we are choosing

        self.shop_pets = []
        for _ in range(round_config.NUM_SHOP_PETS):
            tier = self._get_shop_tier(round_config.MAX_SHOP_TIER)
            pet_config = PET_CONFIG[choice(TIER_PETS[tier])]

            health = pet_config.BASE_HEALTH + self.shop_perm_health_bonus
            attack = pet_config.BASE_ATTACK + self.shop_perm_attack_bonus
            self.shop_pets.append(PetState(health, attack, pet_config))

        self.shop_foods = []
        for _ in range(round_config.NUM_SHOP_FOODS):
            tier = self._get_shop_tier(round_config.MAX_SHOP_TIER)
            food_config = FOOD_CONFIG[choice(TIER_FOOD[tier])]
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

    def _get_bonus_coins(self) -> int:
        return 0

    def _get_shop_tier(self, max_shop_tier: int):
        # Note: we prioritise higher tiers to keep the game interesting
        total_tickets = (max_shop_tier * (max_shop_tier + 1)) / 2
        ticket_num = randint(1, total_tickets)

        tier = 0
        while ticket_num > 0:
            ticket_num -= tier
            tier += 1

        return tier