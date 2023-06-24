from random import sample, choice
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine.state.petstate import PetState
    from engine.state.gamestate import GameState
    from engine.state.playerstate import PlayerState
from engine.config.petconfig import PET_CONFIG, PetConfig, PetType, TIER_PETS

# Abilities are scaled per level, where L = level
class PetAbilities:
    @staticmethod
    # On level up, Give 2 (random) pets +1L health and +1L attack (consider previous level)
    def fish_ability(fish: 'PetState', player: 'PlayerState', state: 'GameState'):
        other_pets = [pet for pet in player.pets if pet != fish and pet is not None]

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
        other_pets = [pet for pet in player.pets if pet != beaver and pet is not None]

        # If there are no other pets we're done
        if other_pets == 0: return

        num_choose = 2 if len(other_pets) >= 2 else 1
        pets_to_upgrade = sample(other_pets, num_choose)
        for pet in pets_to_upgrade:
            pet.perm_increase_attack(beaver.get_level())

    @staticmethod
   # Ability: On faint, give L attack and helath to a random friend
    def ant_ability(ant: 'PetState', player: 'PlayerState', state: 'GameState'):
        pets = player.battle_pets if state.in_battle_stage else player.pets
        other_pets = [pet for pet in pets if pet != ant and pet is not None]

        # If there are no other pets we're done
        if len(other_pets) == 0: return

        pet_to_upgrade = choice(other_pets)
        #Only temporary in battle state 
        if state.in_battle_stage:
            pet_to_upgrade.attack += ant.get_level()
            pet_to_upgrade.health += ant.get_level()
        else:
            pet_to_upgrade.perm_increase_attack(ant.get_level())
            pet_to_upgrade.perm_increase_health(ant.get_level())

    @staticmethod
    # Ability: At start of battle, deal 1 damage to L enemies
    def mosquito_ability(mosquito: 'PetState', player: 'PlayerState', state: 'GameState'):
        targets = player.opponent.battle_pets

        # If there are no other pets we're done
        if len(targets) == 0: return

        num_choose = mosquito.get_level() if len(targets) >= mosquito.get_level() else len(targets)
        pets_to_snipe = sample(targets, num_choose)
        for pet in pets_to_snipe:
            mosquito.damage_enemy_with_ability(1, pet)

    @staticmethod
    # Ability: On faint, spawn a zombie cricket with L attack and health
    def cricket_ability(cricket: 'PetState', player: 'PlayerState', state: 'GameState'):
        zombie_config = PET_CONFIG[PetType.ZOMBIE_CRICKET]
        zombie = PetState(zombie_config.BASE_ATTACK, zombie_config.BASE_HEALTH, zombie_config, player, state)
        
        player.summon_pets(cricket, [zombie])

    @staticmethod
    # Ability: Friend summoned, give L attack until the end of combat
    def horse_ability(horse: 'PetState', player: 'PlayerState', state: 'GameState'):
        player.new_summoned_pet.attack += horse.get_level()

    @staticmethod
    # Ability: Start of combat, gain 0.5L health from the healthiest friend
    def crab_ability(crab: 'PetState', player: 'PlayerState', state: 'GameState'):
        highest_health = max([pet.health for pet in player.pets if pet != crab and pet is not None])
        crab.health += int(0.5 * highest_health)

    @staticmethod
    # Ability: Start of turn (buy period), gain L gold
    def swan_ability(swan: 'PetState', player: 'PlayerState', state: 'GameState'):
        level = swan.get_level()
        player.coins += level
    
    @staticmethod
    # Ability: On faint, deal 2L damage to all 
    def hedgehog_ability(hedgehog: 'PetState', player: 'PlayerState', state: 'GameState'):
        pets = [pet for pet in player.pets if pet != hedgehog and pet is not None]
        if state.in_battle_stage:
            pets += player.opponent.battle_pets

        for pet in pets: 
            hedgehog.damage_enemy_with_ability(2 * hedgehog.get_level(), pet)

    @staticmethod
    # TODO: Ability: When hurt, gain 4L temporary attach
    def peacock_ability(peacock: 'PetState', player: 'PlayerState', state: 'GameState'):
        
        if state.in_battle_stage:
            peacock.attack += 4 * peacock.get_level()
        else:
            peacock.perm_increase_attack(4*peacock.get_level)           
        

    @staticmethod
    # Ability: Friend ahead attacks, gain L health and damage
    def kangaroo_ability(kangaroo: 'PetState', player: 'PlayerState', state: 'GameState'):
        kangaroo.attack += kangaroo.get_level()
        kangaroo.health += kangaroo.get_level()

    @staticmethod
    # Ability: On faint, give L health and attack to two nearest pets behind
    def flamingo_ability(flamingo: 'PetState', player: 'PlayerState', state: 'GameState'):
        pass

    @staticmethod
    # Ability: On faint, summon a tier 3 pet with L health and attack
    def spider_ability(spider: 'PetState', player: 'PlayerState', state: 'GameState'):
        #Find the config for a random tier 3 pet        
        pet_type = choice(TIER_PETS[3])
        new_pet = PetState(spider.get_level(), spider.get_level(), pet_type, player, state)
        
        player.summon_pets(spider, [new_pet])

    @staticmethod
    # Ability: Start of battle, give 0.5L attack to the nearest friend ahead
    def dodo_ability(dodo: 'PetState', player: 'PlayerState', state: 'GameState'):
        dodo_index = player.battle_pets.index(dodo)
        
        if dodo_index is not 0:
            player.battle_pets[dodo_index - 1].attack += int(dodo.get_level() * 0.5)
        

    @staticmethod
    # Ability: Before faint, deal 0.5L attack damage to the adjacent pets
    # TODO: Find out what an adjacent means 
    def badger_ability(badger: 'PetState', player: 'PlayerState', state: 'GameState'):
        pass

    @staticmethod
    # Ability: Start of battle, deal 3 damage to L random pets on the other team
    def dolphin_ability(dolphin: 'PetState', player: 'PlayerState', state: 'GameState'):
        targets = player.opponent.battle_pets

        # If there are no other pets we're done
        if len(targets) == 0: return

        num_choose = dolphin.get_level() if len(targets) >= dolphin.get_level() else len(targets)
        pets_to_snipe = sample(targets, num_choose)
        for pet in pets_to_snipe:
            dolphin.damage_enemy_with_ability(3, pet)

    @staticmethod
    # Ability: End of turn (buy phase), give 1 health and attack to L friends in front of it
    # TODO: Check if we know the line up and order 
    # Issue
    def giraffe_ability(giraffe: 'PetState', player: 'PlayerState', state: 'GameState'):
        giraffe_index = player.pets.index(giraffe)
        
        # If it is at the front then no buffs can be given
        if giraffe_index == 0: return
        
        # The index will signify how many pets are in front of it (2nd place has index 1 and thus 1 pet infront)
        buffed_pets_amount = min(giraffe_index, giraffe.get_level())
        
        # Will only look literally 
        buffed_pets = player.pets[(giraffe_index - buffed_pets_amount) : giraffe_index()]
        
        for pet in buffed_pets:
            if pet is not None:
                pet.attack += giraffe.get_level()
                pet.health += giraffe.get_level()
        
        

    @staticmethod
    # Ability: When hurt, give nearest friend 2L attack and health; prioritise back
    # TODO: Same problem as but this has some assumptions 
    def camel_ability(camel: 'PetState', player: 'PlayerState', state: 'GameState'):
        # If the camel has something behind it or is not yet the last pet
        if player.battle_pets[-1] is not camel:
            buff_pet = player.battle_pets[player.battle_pets.index(camel) + 1]
            buff_pet.attack += 2 * camel.get_level()
            buff_pet.health += 2 * camel.get_level()
            
        else:
            # Perhaps no case where this would b
            # TODO: Cos case where it is last/only pet 
            if len(player.battle_pets) == 0: return 
            
            buff_pet = player.battle_pets[player.battle_pets.index(camel) - 1]
            buff_pet.attack += 2 * camel.get_level()
            buff_pet.health += 2 * camel.get_level()

    @staticmethod
    # Ability: After attack, deal 1 damage to the friend behind L times
    def elephant_ability(elephant: 'PetState', player: 'PlayerState', state: 'GameState'):
        
        # Nothing will happen if it has no pet behind the elephant
        # ALso covers case where it is just the elephant
        if player.battle_pets[-1] == elephant: return
        
        elephant_index = player.battle_pets.index(elephant)
        target_friend = player.battle_pets[elephant_index + 1] if not None else None
        
        for _ in range(elephant.get_level()):
            elephant.damage_enemy_with_ability(1, target_friend)
        

    @staticmethod
    # Ability: When a friendly eats food, give them +L health (THIS CAN CHANGE)
    def bunny_ability(bunny: 'PetState', player: 'PlayerState', state: 'GameState'):
        target_friend = player.pet_that_ate_food
        
        target_friend.health += bunny.get_level()

    @staticmethod
    # Ability: When a friend is summoned, gain 2L attack and L health until end of battle (stacking and unlimited)
    def dog_ability(dog: 'PetState', player: 'PlayerState', state: 'GameState'):
        dog.health += dog.get_level()
        dog.attack += 2 * dog.get_level()

    @staticmethod
    # Ability: On faint, summon 2 rams with 2L health and attack
    def sheep_ability(sheep: 'PetState', player: 'PlayerState', state: 'GameState'):
        new_pet = PetState(sheep.get_level(), sheep.get_level(), PET_CONFIG[PetType.RAM], player, state)
        
        player.summon_pets(sheep, [new_pet, new_pet])

