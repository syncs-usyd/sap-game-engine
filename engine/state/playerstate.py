from copy import deepcopy
from random import choice, randint, shuffle
from typing import List, Optional

from engine.config.foodconfig import FOOD_CONFIG, TIER_FOOD, FoodType
from engine.config.gameconfig import MAX_SHOP_TIER, NUM_PLAYERS, PET_POSITIONS, STARTING_COINS, STARTING_HEALTH
from engine.config.petconfig import PET_CONFIG, TIER_PETS, PetType
from engine.config.roundconfig import RoundConfig
from engine.game.abilitytype import AbilityType
from engine.state.foodstate import FoodState
from engine.state.gamestate import GameState
from engine.state.petstate import PetState


class PlayerState:
    def __init__(self, player_num: int, state: 'GameState'):
        self.player_num = player_num
        self.state = state

        self.health = STARTING_HEALTH
        self.pets: List[Optional['PetState']] = [None] * PET_POSITIONS

        self.shop_pets: List['PetState'] = []
        self.shop_foods: List['FoodState'] = []
        self.shop_perm_health_bonus = 0
        self.shop_perm_attack_bonus = 0

        # Represents who you are currently battling. This can change to multiple different
        # players during a single battle stage
        self.opponent: Optional['PlayerState'] = None

        # Represents a copy of your pets for the purpose of running a battle
        self.battle_pets: List['PetState'] = []

        # Represents who will be challenging you during the battle stage
        # Will only be a single player for an entire battle stage
        self.challenger: Optional['PlayerState'] = None
        self.battle_order = [i for i in range(NUM_PLAYERS) if i != player_num]
        shuffle(self.battle_order)
        self.next_battle_index = 0

        # Contains a reference to the newest summoned pet for use in
        # FRIEND_SUMMON abilities
        self.new_summoned_pet: Optional['PetState'] = None

        # Contains a reference to the pet that just ate food
        # for use in FRIEND_ATE_FOOD abilities
        self.pet_that_ate_food: Optional['PetState'] = None

    def start_new_round(self):
        self.prev_health = self.health
        self.prev_pets = deepcopy(self.pets)

        self.coins = STARTING_COINS
        self.reset_shop_options()
        for pet in self.pets:
            if pet is not None:
                pet.start_new_round()

    def start_battle_stage(self):
        for pet in self.pets:
            pet.proc_ability(AbilityType.BUY_ROUND_END)     
        self._update_challenger()

    # We copy the battle pets so we can make irreversible changes
    # during a battle
    def start_battle(self, opponent: 'PlayerState'):
        self.opponent = opponent
        self.battle_pets = deepcopy(self.pets)
        self.cleanup_battle_pets()
        for pet in self.battle_pets:
            pet.start_next_battle_turn()

    # Remove dead pets and empty slots
    def cleanup_battle_pets(self):
        self.battle_pets = [pet for pet in self.battle_pets if pet is not None and pet.is_alive()]

    def reset_shop_options(self):
        round_config = RoundConfig.get_round_config(self.state.round)

        self.shop_pets = [pet for pet in self.shop_pets if pet.is_frozen]
        pets_to_add = round_config.NUM_SHOP_PETS - len(self.shop_pets)
        for _ in range(pets_to_add):
            shop_pet = self._create_shop_pet(self._get_random_pet_type(round_config.MAX_SHOP_TIER))
            self.shop_pets.append(shop_pet)

        self.shop_foods = [food for food in self.shop_foods if food.is_frozen]
        foods_to_add = round_config.NUM_SHOP_FOODS - len(self.shop_foods)
        for _ in range(foods_to_add):
            food_config = FOOD_CONFIG[self._get_random_food_type(round_config.MAX_SHOP_TIER)]
            self.shop_foods.append(FoodState(food_config))

    def add_level_up_shop_pet(self):
        round_config = RoundConfig.get_round_config(self.state.round)
        tier = min(round_config.MAX_SHOP_TIER + 1, MAX_SHOP_TIER)
        pet_type = choice(TIER_PETS[tier - 1])
        shop_pet = self._create_shop_pet(pet_type)
        self.shop_pets.append(shop_pet)

    def friend_summoned(self, new_pet: 'PetState'):
        pet_list: List[Optional['PetState']] = []
        if self.state.in_battle_stage:
            pet_list = self.battle_pets
        else:
            pet_list = self.pets

        self.new_summoned_pet = new_pet
        for pet in pet_list:
            if pet is not None and pet != new_pet:
                pet.proc_ability(AbilityType.FRIEND_SUMMONED)

        # Clear the reference now its not needed
        self.new_summoned_pet = None

    def friend_ate_food(self, fat_pet: 'PetState'):
        self.pet_that_ate_food = fat_pet
        for pet in self.pets:
            pet.proc_ability(AbilityType.FRIEND_ATE_FOOD)

        # Clear the reference now its not needed
        self.pet_that_ate_food = None

    def is_alive(self) -> bool:
        return self.health > 0

    def get_view_for_self(self) -> dict:
        return {
            "health": self.health,
            "coins": self.coins,
            "pets": [pet.get_view_for_self() if pet is not None else None for pet in self.pets],
            "shop_pets": [pet.get_view_for_shop() for pet in self.shop_pets],
            "shop_foods": [food.get_view_for_shop() for food in self.shop_foods]
        }

    def get_view_for_others(self) -> dict:
        return {
            "health": self.prev_health,
            "pets": [pet.get_view_for_others() if pet is not None else None for pet in self.prev_pets]
        }

    # Round robin through battle order until the next alive player is found
    def _update_challenger(self):
        i = self.next_battle_index
        while True:
            challenger = self.state.players[self.battle_order[i]]
            i = (i + 1) % NUM_PLAYERS

            if challenger.is_alive():
                self.next_battle_index = i
                self.challenger = challenger
                return

    def _create_shop_pet(self, pet_type: 'PetType') -> 'PetState':
        pet_config = PET_CONFIG[pet_type]
        health = pet_config.BASE_HEALTH + self.shop_perm_health_bonus
        attack = pet_config.BASE_ATTACK + self.shop_perm_attack_bonus
        return PetState(health, attack, pet_config)

    def _get_random_pet_type(self, max_shop_tier: int) -> 'PetType':
        return self._get_random_from_config_tiers(TIER_PETS, max_shop_tier)

    def _get_random_food_type(self, max_shop_tier: int) -> 'FoodType':
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
