from random import sample

from engine.game.abilitytype import AbilityType
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
    def sleeping_pill_effect(pet: 'PetState', player: 'PlayerState', state: 'GameState'):
        i = player.pets.index(pet)
        player.pets[i] = None
        player.friend_ate_food(pet)
        pet.proc_ability(AbilityType.FAINTED)

    @staticmethod
    def cupcake_effect(pet: 'PetState', player: 'PlayerState', state: 'GameState'):
        pet.health += 3
        pet.attack += 3
        player.friend_ate_food(pet)

    @staticmethod
    def salad_bowl_effect(unused: 'PetState', player: 'PlayerState', state: 'GameState'):
        num_choose = 2 if len(player.pets) >= 2 else len(player.pets)
        pets_to_upgrade = sample(player.pets, num_choose)
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
