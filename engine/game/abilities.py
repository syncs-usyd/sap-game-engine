from random import sample
from engine.state.gamestate import GameState
from engine.state.petstate import PetState
from engine.state.playerstate import PlayerState


class Abilities:
    @staticmethod
    # On level up, Give 2 (random) pets +1L health and +1L attack (consider previous level)
    def fish_ability(fish: 'PetState', player: 'PlayerState', state: 'GameState'):
        other_pets = [pet for pet in player.pets if pet != fish]

        # If there are no other pets we're done
        if other_pets == 0: return

        num_choose = 2 if len(other_pets) >= 2 else 1
        pets_to_upgrade = sample(other_pets, num_choose)
        for pet in pets_to_upgrade:
            pet.perm_increase_health(fish.get_level() - 1)
            pet.perm_increase_attack(fish.get_level() - 1)

    @staticmethod
    def pig_ability(pig: 'PetState', player: 'PlayerState', state: 'GameState'):
        level = pig.get_level()
        player.coins += level

    @staticmethod
    def mosquito_ability(mosquito: 'PetState', player: 'PlayerState', state: 'GameState'):
        pass