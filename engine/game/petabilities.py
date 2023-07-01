from random import sample, choice
from typing import TYPE_CHECKING

from engine.config.pettype import TIER_PETS, PetType

if TYPE_CHECKING:
    from engine.state.petstate import PetState
    from engine.state.playerstate import PlayerState


# Abilities are scaled per level, where L = level
class PetAbilities:
    @staticmethod
    # On level up, Give 2 (random) pets +1L health and +1L attack
    def fish_ability(fish: 'PetState', player: 'PlayerState'):
        other_pets = [pet for pet in player.pets if pet != fish and pet is not None]

        # If there are no other pets we're done
        if other_pets == 0: return

        num_choose = 2 if len(other_pets) >= 2 else 1
        pets_to_upgrade = sample(other_pets, num_choose)
        for pet in pets_to_upgrade:
            pet.perm_increase_health(fish.get_level() - 1)
            pet.perm_increase_attack(fish.get_level() - 1)

    @staticmethod
    # On sell, give L gold
    def pig_ability(pig: 'PetState', player: 'PlayerState'):
        level = pig.get_level()
        player.coins += level

    @staticmethod
    # On sell, give 2 (random) pets +L attack
    def beaver_ability(beaver: 'PetState', player: 'PlayerState'):
        other_pets = [pet for pet in player.pets if pet != beaver and pet is not None]

        # If there are no other pets we're done
        if other_pets == 0: return

        num_choose = 2 if len(other_pets) >= 2 else 1
        pets_to_upgrade = sample(other_pets, num_choose)
        for pet in pets_to_upgrade:
            pet.perm_increase_attack(beaver.get_level())

    @staticmethod
    # On faint, give L attack and health to a random friend
    def ant_ability(ant: 'PetState', player: 'PlayerState'):
        other_pets = [pet for pet in player.battle_pets if pet != ant and pet is not None]

        # If there are no other pets we're done
        if len(other_pets) == 0: return

        pet_to_upgrade = choice(other_pets)
        pet_to_upgrade.change_attack(ant.get_level())
        pet_to_upgrade.change_health(ant.get_level())

    @staticmethod
    # At start of battle, deal 1 damage to L enemies
    def mosquito_ability(mosquito: 'PetState', player: 'PlayerState'):
        targets = player.opponent.battle_pets

        # If there are no other pets we're done
        if len(targets) == 0: return

        num_choose = mosquito.get_level() if len(targets) >= mosquito.get_level() else len(targets)
        pets_to_snipe = sample(targets, num_choose)
        for pet in pets_to_snipe:
            mosquito.damage_enemy_with_ability(1, pet)

    @staticmethod
    # On faint, spawn a zombie cricket with L attack and health
    def cricket_ability(cricket: 'PetState', player: 'PlayerState'):
        zombie_cricket = player.create_pet_to_summon(PetType.ZOMBIE_CRICKET, cricket.get_level(), cricket.get_level())
        player.summon_pets(cricket, [zombie_cricket])

    @staticmethod
    # Friend summoned, give L attack until the end of combat
    def horse_ability(horse: 'PetState', player: 'PlayerState'):
        player.new_summoned_pet.change_attack(horse.get_level())

    @staticmethod
    # Start of combat, gain 0.5L health from the healthiest friend
    def crab_ability(crab: 'PetState', player: 'PlayerState'):
        highest_health = max([pet.get_health() for pet in player.pets if pet != crab and pet is not None])
        crab.change_health(int(0.5 * highest_health * crab.get_level()))

    @staticmethod
    # Start of turn (buy period), gain L gold
    def swan_ability(swan: 'PetState', player: 'PlayerState'):
        level = swan.get_level()
        player.coins += level
    
    @staticmethod
    # On faint, deal 2L damage to all
    def hedgehog_ability(hedgehog: 'PetState', player: 'PlayerState'):
        for pet in player.battle_pets + player.opponent.battle_pets:
            hedgehog.damage_enemy_with_ability(2 * hedgehog.get_level(), pet)

    @staticmethod
    # When hurt, gain 4L attack
    def peacock_ability(peacock: 'PetState', player: 'PlayerState'):
        peacock.change_attack(4 * peacock.get_level())

    @staticmethod
    # Friend ahead attacks, gain L health and damage
    def kangaroo_ability(kangaroo: 'PetState', player: 'PlayerState'):
        kangaroo.change_attack(kangaroo.get_level())
        kangaroo.change_health(kangaroo.get_level())

    @staticmethod
    # On faint, give L health and attack to two nearest pets behind
    def flamingo_ability(flamingo: 'PetState', player: 'PlayerState'):
        index = player.battle_pets.index(flamingo)

        if len(player.battle_pets) > index + 1:
            player.battle_pets[index + 1].change_attack(flamingo.get_level())
            player.battle_pets[index + 1].change_health(flamingo.get_level())

        if len(player.battle_pets) > index + 2:
            player.battle_pets[index + 2].change_attack(flamingo.get_level())
            player.battle_pets[index + 2].change_health(flamingo.get_level())

    @staticmethod
    # On faint, summon a tier 3 pet with 2L health and attack
    def spider_ability(spider: 'PetState', player: 'PlayerState'):
        pet_type = choice(TIER_PETS[3])
        pet = player.create_pet_to_summon(pet_type, 2 * spider.get_level(), 2 * spider.get_level())
        player.summon_pets(spider, [pet])

    @staticmethod
    # Start of battle, give 0.5L attack to the nearest friend ahead
    def dodo_ability(dodo: 'PetState', player: 'PlayerState'):
        dodo_index = player.battle_pets.index(dodo)
        if dodo_index != 0:
            player.battle_pets[dodo_index - 1].change_attack(int(0.5 * dodo.get_attack() * dodo.get_level()))

    @staticmethod
    # Before faint, deal 0.5L attack damage to the adjacent pets. Includes your own pets
    def badger_ability(badger: 'PetState', player: 'PlayerState'):
        attack = int(0.5 * badger.get_attack() * badger.get_level())
        index = player.battle_pets.index(badger)

        if index == 0:
            if len(player.opponent.battle_pets) > 0:
                badger.damage_enemy_with_ability(attack, player.opponent.battle_pets[0])
        else:
            badger.damage_enemy_with_ability(attack, player.battle_pets[index - 1])

        if len(player.battle_pets) > index + 1:
            badger.damage_enemy_with_ability(attack, player.battle_pets[index + 1])

    @staticmethod
    # Start of battle, deal 3 damage to the lowest health enemy. Triggers L times
    def dolphin_ability(dolphin: 'PetState', player: 'PlayerState'):
        for _ in range(dolphin.get_level()):
            pets = [pet for pet in player.opponent.battle_pets if pet.is_alive()]
            pets.sort(key = lambda pet: pet.get_health())
            if len(pets) > 0:
                dolphin.damage_enemy_with_ability(3, pets[0])

    @staticmethod
    # End of turn (buy phase), give 1 health and attack to L friends in front of it
    def giraffe_ability(giraffe: 'PetState', player: 'PlayerState'):
        pets = [pet for pet in player.pets if pet is not None]
        giraffe_index = pets.index(giraffe)

        # If it is at the front then no buffs can be given
        if giraffe_index == 0: return

        # The index will signify how many pets are in front of it (2nd place has index 1 and thus 1 pet infront)
        num_pets_to_buff = min(giraffe_index, giraffe.get_level())

        pets_to_buff = pets[(giraffe_index - num_pets_to_buff) : giraffe_index]
        for pet in pets_to_buff:
            pet.perm_increase_attack(1)
            pet.perm_increase_health(1)

    @staticmethod
    # When hurt, give nearest friend behind 2L attack and health
    def camel_ability(camel: 'PetState', player: 'PlayerState'):
        # If the camel has something behind it or is not yet the last pet
        if player.battle_pets[-1] != camel:
            buff_pet = player.battle_pets[player.battle_pets.index(camel) + 1]
            buff_pet.change_attack(2 * camel.get_level())
            buff_pet.change_health(2 * camel.get_level())

    @staticmethod
    # After attack, deal 1 damage to the friend behind L times
    def elephant_ability(elephant: 'PetState', player: 'PlayerState'):
        # Nothing will happen if it has no pet behind the elephant
        # Also covers case where it is just the elephant
        if player.battle_pets[-1] == elephant: return

        elephant_index = player.battle_pets.index(elephant)
        target_friend = player.battle_pets[elephant_index + 1]

        # Known bug: this wont retrigger other pets hurt ability multiple times
        for _ in range(elephant.get_level()):
            elephant.damage_enemy_with_ability(1, target_friend)

    @staticmethod
    # When a friendly eats food, give them +L health
    def bunny_ability(bunny: 'PetState', player: 'PlayerState'):
        target_friend = player.pet_that_ate_food
        target_friend.perm_increase_health(bunny.get_level())

    @staticmethod
    # When a friend is summoned, gain 2L attack and L health until end of battle (stacking and unlimited)
    def dog_ability(dog: 'PetState', player: 'PlayerState'):
        dog.change_health(dog.get_level())
        dog.change_attack(2 * dog.get_level())

    @staticmethod
    # On faint, summon 2 rams with 2L health and attack
    def sheep_ability(sheep: 'PetState', player: 'PlayerState'):
        stat = 2 * sheep.get_level()
        ram_a = player.create_pet_to_summon(PetType.RAM, stat, stat)
        ram_b = player.create_pet_to_summon(PetType.RAM, stat, stat)
        player.summon_pets(sheep, [ram_a, ram_b])

    @staticmethod
    # Battle round start -> Reduce the highest health enemy's health by 0.33*L
    def skunk_ability(skunk: 'PetState', player: 'PlayerState'):
        highest_health_pet = max(player.opponent.battle_pets, key = lambda pet: pet.get_health())
        percent = 0.33 * skunk.get_level()
        reduce_amount = int(highest_health_pet.get_health() * percent)
        highest_health_pet.change_health(-reduce_amount)

    @staticmethod
    # Knockout -> Gain 3L health and attack
    def hippo_ability(hippo: 'PetState', player: 'PlayerState'):
        hippo.change_health(3 * hippo.get_level())
        hippo.change_attack(3 * hippo.get_level())

    @staticmethod
    # End buy round -> If this has a level 3 friend, gain L attack and 2L health
    def bison_ability(bison: 'PetState', player: 'PlayerState'):
        level_3_friend = False
        for pet in player.pets:
            if pet.get_level() == 3:
                level_3_friend = True
                break
            
        if level_3_friend:
            bison.perm_increase_health(2 * bison.get_level())
            bison.perm_increase_attack(bison.get_level())

    @staticmethod
    # On hurt -> Deal 3L damage to one random enemy
    def blowfish_ability(blowfish: 'PetState', player: 'PlayerState'):
        if len(player.opponent.battle_pets) == 0: return
        target_pet = choice(player.opponent.battle_pets)
        blowfish.damage_enemy_with_ability(3 * blowfish.get_level(), target_pet)

    @staticmethod
    # Start of buy round -> discount all shop food by 1 coin
    def squirrel_ability(squirrel: 'PetState', player: 'PlayerState'):
        for food in player.shop_foods:
            food.cost -= squirrel.get_level()
            food.cost = max(0, food.cost)

    @staticmethod
    # End buy round -> Give two level 2+ friends L health and attack
    def penguin_ability(penguin: 'PetState', player: 'PlayerState'):
        strong_pets = [pet for pet in player.pets if pet != penguin and pet is not None and pet.get_level() >= 2]

        if len(strong_pets) == 0: return
        
        num_choose = 2 if len(strong_pets) >= 2 else 1
        pets_to_upgrade = sample(strong_pets, num_choose)
        for pet in pets_to_upgrade:
            pet.perm_increase_health(penguin.get_level())
            pet.perm_increase_attack(penguin.get_level())
