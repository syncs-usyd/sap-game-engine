from random import sample, choice
from engine.state.gamestate import GameState
from engine.state.petstate import PetState
from engine.state.playerstate import PlayerState


class PetAbilities:
    # Abilities are scaled per level, where L = level
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
    # Ability: On sell, give L gold
    def pig_ability(pig: 'PetState', player: 'PlayerState', state: 'GameState'):
        level = pig.get_level()
        player.coins += level

    @staticmethod
    # Ability: On sell, give 2 (random) pets +L attack
    def beaver_ability(beaver: 'PetState', player: 'PlayerState', state: 'GameState'):
        other_pets = [pet for pet in player.pets if pet != beaver]

        # If there are no other pets we're done
        if other_pets == 0: return

        num_choose = 2 if len(other_pets) >= 2 else 1
        pets_to_upgrade = sample(other_pets, num_choose)
        for pet in pets_to_upgrade:
            pet.perm_increase_attack(beaver.get_level())
            
            
    @staticmethod
   # Ability: On faint, give L attack and helath to a random friend
    def ant_ability(ant: 'PetState', player: 'PlayerState', state: 'GameState'):
        other_pets = [pet for pet in player.pets if pet != ant]

        # If there are no other pets we're done
        if other_pets == 0: return

        pet_to_upgrade = choice(other_pets)
        pet_to_upgrade.perm_increase_attack(ant.get_level())
        pet_to_upgrade.perm_increase_health(ant.get_level())

    
    @staticmethod
    # Ability: At start of battle, deal 1 damage to L enemies
    # TODO: Check if the interaction is correct
    def mosquito_ability(mosquito: 'PetState', player: 'PlayerState', state: 'GameState'):
        targets = player.challenger.pets

        # If there are no other pets we're done
        if len(targets) == 0: return

        num_choose = mosquito.get_level() if len(targets) >= mosquito.get_level() else len(targets)
        pets_to_snipe = sample(targets, num_choose)
        for pet in pets_to_snipe:
            mosquito.damage_enemy_with_ability(1, pet)
            
    @staticmethod
    # TODO: Actually implement this lol
    # Ability: On faint, spawn a zombie cricket with L attack and health
    def cricket_ability(cricket: 'PetState', player: 'PlayerState', state: 'GameState'):
        pass
    
    @staticmethod
    # Ability: Friend summoned, give L temporary attack
    def horse_ability(horse: 'PetState', player: 'PlayerState'):
        player.new_summoned_pet.attack += horse.get_level()
    
    @staticmethod
    # Ability: Start of combat, gain 0.5L health from the healthiest friend
    # TODO: check if this is the right way to check health
    def crab_ability(crab: 'PetState', player: 'PlayerState', state: 'GameState'):
        highest_health = 0
        for pet in player.pets:
            if pet.health > highest_health:
                highest_health = pet.health
                
                
        crab.health = crab.health + 0.5 * highest_health
    
    @staticmethod
    # Ability: Start of turn (buy period), gain L gold
    def swan_ability(swan: 'PetState', player: 'PlayerState', state: 'GameState'):
        level = swan.get_level()
        player.coins += level
    
    @staticmethod
    # TODO: Ability: On faint, deal 2L damage to all 
    def hedgehog_ability(hedgehog: 'PetState', player: 'PlayerState', state: 'GameState'):
        pass
    
    @staticmethod
    # Ability: When hurt, gain 4L attack permanently 
    def peacock_ability(peacock: 'PetState', player: 'PlayerState', state: 'GameState'):
        pass
    
    @staticmethod
    # Ability: Friend ahead attacks, gain L helath and damage
    def kangaroo_ability(kangaroo: 'PetState', player: 'PlayerState', state: 'GameState'):
        pass
    
    @staticmethod
    
    # Ability: On faint, give L health and attack to two nearest pets behind
    def flamingo_ability(flamingo: 'PetState', player: 'PlayerState', state: 'GameState'):
        pass
    
    @staticmethod
    # Ability: On faint, summon a tier 3 pet with L health and attack
    def spider_ability(spider: 'PetState', player: 'PlayerState', state: 'GameState'):
        pass
    
    @staticmethod
    def dodo_ability(dodo: 'PetState', player: 'PlayerState', state: 'GameState'):
        pass
    
    @staticmethod
    def badger_ability(badger: 'PetState', player: 'PlayerState', state: 'GameState'):
        pass
    
    @staticmethod
    def dolphin_ability(dolphin: 'PetState', player: 'PlayerState', state: 'GameState'):
        pass
    
    @staticmethod
    def giraffe_ability(giraffe: 'PetState', player: 'PlayerState', state: 'GameState'):
        pass
    
    @staticmethod
    def camel_ability(camel: 'PetState', player: 'PlayerState', state: 'GameState'):
        pass
    
    @staticmethod
    def elephant_ability(elephant: 'PetState', player: 'PlayerState', state: 'GameState'):
        pass
    
    @staticmethod
    def bunny_ability(bunny: 'PetState', player: 'PlayerState', state: 'GameState'):
        pass
    
    @staticmethod
    def dog_ability(dog: 'PetState', player: 'PlayerState', state: 'GameState'):
        pass
    
    @staticmethod
    def sheep_ability(sheep: 'PetState', player: 'PlayerState', state: 'GameState'):
        pass
    
