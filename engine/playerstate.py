from random import shuffle
from typing import List, Tuple
from engine.config import NUM_PLAYERS, PET_POSITIONS, REROLL_COST, ROUND_CONFIG, STARTING_COINS, STARTING_HEALTH, FoodConfig
from engine.gamestate import GameState
from engine.petstate import PetState


class PlayerState:
    def __init__(self, player_num: int) -> 'PlayerState':
        self.health = STARTING_HEALTH
        self.pets = [None] * PET_POSITIONS
        self.battle_order = [i for i in range(NUM_PLAYERS) if i != player_num]
        shuffle(self.battle_order)
        self.next_battle_index = 0

    def start_new_round(self, round: int):
        self.coins = STARTING_COINS + self.get_bonus_coins()
        self.shop_options = self.get_shop_options(round)
        for pet in self.pets:
            if pet != None:
                pet.start_new_round(round)

    def get_challenger(self, state: 'GameState') -> 'PlayerState':
        while True:
            challenger = state.players[self.battle_order[self.next_battle_index]]
            self.next_battle_index = (self.next_battle_index + 1) % NUM_PLAYERS
            if challenger.is_alive():
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

