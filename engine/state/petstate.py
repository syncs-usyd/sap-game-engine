from typing import Optional

from engine.config.foodconfig import FOOD_CONFIG, FoodConfig, FoodType
from engine.config.gameconfig import LEVEL_2_CUTOFF, LEVEL_3_CUTOFF
from engine.config.petconfig import PetConfig
from engine.game.abilitytype import AbilityType
from engine.state.gamestate import GameState
from engine.state.playerstate import PlayerState


class PetState:
    def __init__(self, health: int, attack: int, pet_config: 'PetConfig', player: 'PlayerState', state: 'GameState'):
        self.player = player
        self.state = state

        self.pet_config = pet_config
        self.perm_health = health
        self.perm_attack = attack

        self.carried_food: Optional['FoodConfig'] = None 
        self.sub_level = 0

        # If the pet is in the shop, represents whether it is frozen or not
        self.is_frozen = False

        # Represents whether the pet has already been hurt in the current battle turn
        self.hurt_already = False

    def start_new_round(self):
        self.prev_health = self.perm_health
        self.prev_attack = self.perm_attack
        self.prev_carried_food = self.carried_food
        self.prev_level = self.get_level()

        self.health = self.perm_health
        self.attack = self.perm_attack

        self.proc_ability(AbilityType.BUY_ROUND_START)

    def start_next_battle_turn(self):
        self.hurt_already = False

    def get_level(self):
        if self.sub_level == LEVEL_3_CUTOFF:
            return 3
        elif self.sub_level >= LEVEL_2_CUTOFF:
            return 2
        else:
            return 1

    def get_sub_level_progress(self):
        level = self.get_level()
        if level == 3:
            return 0
        elif level == 2:
            return self.sub_level - LEVEL_2_CUTOFF
        else:
            return self.sub_level

    def level_up(self, other_pet: 'PetState'):
        old_level = self.get_level() 

        self.sub_level += other_pet.sub_level + 1
        max_sub_level = LEVEL_2_CUTOFF + LEVEL_3_CUTOFF
        self.sub_level = min(self.sub_level, max_sub_level)

        new_level = self.get_level()

        self.perm_increase_health(1)
        self.perm_increase_attack(1)

        if old_level < new_level:
            self.player.add_level_up_shop_pet()
            self.proc_ability(AbilityType.LEVEL_UP)

    def damage_enemy_with_attack(self, enemy_pet: 'PetState'):
        self._damage_enemy(self.attack + self.get_bonus_attack(), enemy_pet)

    def damage_enemy_with_ability(self, attack, enemy_pet: 'PetState'):
        self._damage_enemy(attack, enemy_pet)

    def proc_ability(self, ability_type: AbilityType):
        if self.pet_config.ABILITY_TYPE == ability_type:
            self.pet_config.ABILITY_FUNC(self, self.player, self.state)

    def perm_increase_health(self, amount: int):
        self.health += amount
        self.perm_health += amount

    def perm_increase_attack(self, amount: int):
        self.attack += amount
        self.perm_attack += amount

    def get_bonus_attack(self) -> int:
        if self.carried_food == FOOD_CONFIG[FoodType.MEAT_BONE]:
            return 3
        else:
            return 0

    def is_alive(self) -> bool:
        return self.health > 0

    def get_view_for_self(self) -> dict:
        return {
            "type": self.pet_config.PET_NAME,
            "health": self.health,
            "attack": self.attack,
            "level": self.get_level(),
            "sub_level": self.get_sub_level_progress(),
            "carried_food": self.carried_food.FOOD_NAME if self.carried_food is not None else None
        }

    def get_view_for_shop(self) -> dict:
        return {
            "type": self.pet_config.PET_NAME,
            "health": self.health,
            "attack": self.attack,
            "is_frozen": self.is_frozen
        }

    def get_view_for_others(self) -> dict:
        return {
            "type": self.pet_config.PET_NAME,
            "health": self.prev_health,
            "attack": self.prev_attack,
            "level": self.prev_level,
            "carried_food": self.prev_carried_food.FOOD_NAME if self.prev_carried_food is not None else None
        }

    def on_death(self):
        self.proc_ability(AbilityType.FAINTED)
        if self.carried_food == FOOD_CONFIG[FoodType.HONEY]:
            # self.player.summon_pets()
            # TODO: summon beeeeeee
            pass

    def _damage_enemy(self, attack: int, enemy_pet: 'PetState'):
        enemy_was_alive = enemy_pet.is_alive()
        enemy_pet._take_damage(attack)
        if enemy_was_alive and not enemy_pet.is_alive():
            enemy_pet.on_death()
            self.proc_ability(AbilityType.KILLED_ENEMY)

    def _take_damage(self, amount: int):
        if self.carried_food == FOOD_CONFIG[FoodType.GARLIC]:
            amount = max(amount - 2, 1)

        self.health -= amount
        if not self.hurt_already:
            self.hurt_already = True
            self.proc_ability(AbilityType.HURT)
