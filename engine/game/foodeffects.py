from random import sample
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine.state.gamestate import GameState
    from engine.state.petstate import PetState
    from engine.state.playerstate import PlayerState

class FoodEffects:
    @staticmethod
    def apple_effect(pet: 'PetState', player: 'PlayerState', state: 'GameState'):
        pet.perm_increase_health(1)
        pet.perm_increase_attack(1)
        player.friend_ate_food(pet)

    @staticmethod
    def cupcake_effect(pet: 'PetState', player: 'PlayerState', state: 'GameState'):
        pet.change_health(3)
        pet.change_attack(3)
        player.friend_ate_food(pet)

    @staticmethod
    def salad_bowl_effect(unused: 'PetState', player: 'PlayerState', state: 'GameState'):
        pets = [pet for pet in player.pets if pet is not None]

        num_choose = 2 if len(pets) >= 2 else len(pets)
        pets_to_upgrade = sample(pets, num_choose)
        for pet in pets_to_upgrade:
            pet.perm_increase_health(1)
            pet.perm_increase_attack(1)
            player.friend_ate_food(pet)

    @staticmethod
    def canned_food_effect(unused: 'PetState', player: 'PlayerState', state: 'GameState'):
        player.shop_perm_health_bonus += 1
        player.shop_perm_attack_bonus += 1

    @staticmethod
    def pear_effect(pet: 'PetState', player: 'PlayerState', state: 'GameState'):
        pet.perm_increase_health(2)
        pet.perm_increase_attack(2)
        player.friend_ate_food(pet)
