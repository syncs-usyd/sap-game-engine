from typing import TYPE_CHECKING, Optional

from engine.config.foodconfig import FOOD_CONFIG, FoodConfig
from engine.config.foodtype import FoodType
from engine.config.gameconfig import LEVEL_2_CUTOFF, LEVEL_3_CUTOFF, PET_BUY_COST
from engine.config.petconfig import PET_CONFIG, PetConfig
from engine.config.pettype import PetType
from engine.game.abilitytype import AbilityType

if TYPE_CHECKING:
    from engine.state.gamestate import GameState
    from engine.state.playerstate import PlayerState


class PetState:
    def __init__(self, health: int, attack: int, pet_config: 'PetConfig', player: 'PlayerState', state: 'GameState'):
        self.player = player
        self.state = state

        self.id = self.state.get_id()
        self.pet_config = pet_config
        self._perm_health = health
        self._perm_attack = attack
        self._health = health
        self._attack = attack
        self.prev_health = health
        self.prev_attack = attack

        self.carried_food: Optional['FoodConfig'] = None
        self.prev_carried_food: Optional['FoodConfig'] = None

        self.sub_level = 0
        self.prev_level = 1

        self.is_frozen = False

    def start_new_round(self):
        self.prev_health = self._perm_health
        self.prev_attack = self._perm_attack
        self.prev_carried_food = self.carried_food
        self.prev_level = self.get_level()

        self._health = self._perm_health
        self._attack = self._perm_attack

        self.proc_on_demand_ability(AbilityType.BUY_ROUND_START)

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
            self.proc_on_demand_ability(AbilityType.LEVEL_UP)

    def damage_enemy_with_attack(self, enemy_pet: 'PetState'):
        enemy_pet._take_damage(self._attack + self.get_bonus_attack())

    def damage_enemy_with_ability(self, attack, enemy_pet: 'PetState'):
        enemy_pet._take_damage(attack)

    def proc_on_demand_ability(self, ability_type: AbilityType):
        if self.pet_config.ABILITY_TYPE == ability_type:
            self.pet_config.ABILITY_FUNC(self, self.player)

    def perm_increase_health(self, amount: int):
        self.change_health(amount)
        self._change_perm_health(amount)

    def perm_increase_attack(self, amount: int):
        self.change_attack(amount)
        self._change_perm_attack(amount)

    def change_health(self, amount: int):
        self._health += amount
        self._health = min(max(0, self._health), 50)

    def change_attack(self, amount: int):
        self._attack += amount
        self._attack = min(max(0, self._attack), 50)

    def get_bonus_attack(self) -> int:
        if self.carried_food == FOOD_CONFIG[FoodType.MEAT_BONE]:
            return 3
        else:
            return 0

    def get_health(self) -> int:
        return self._health

    def get_attack(self) -> int:
        return self._attack

    def get_perm_health(self) -> int:
        return self._perm_health

    def get_perm_attack(self) -> int:
        return self._perm_attack

    def is_alive(self) -> bool:
        return self._health > 0

    def get_view_for_self(self) -> dict:
        return {
            "id": self.id,
            "type": self.pet_config.PET_NAME,
            "health": self._health,
            "attack": self._attack,
            "level": self.get_level(),
            "sub_level": self.get_sub_level_progress(),
            "carried_food": self.carried_food.FOOD_NAME if self.carried_food is not None else None
        }

    def get_view_for_shop(self) -> dict:
        return {
            "id": self.id,
            "type": self.pet_config.PET_NAME,
            "health": self._health,
            "attack": self._attack,
            "is_frozen": self.is_frozen,
            "cost": PET_BUY_COST
        }

    def get_view_for_others(self) -> dict:
        return {
            "id": self.id,
            "type": self.pet_config.PET_NAME,
            "health": self.prev_health,
            "attack": self.prev_attack,
            "level": self.prev_level,
            "carried_food": self.prev_carried_food.FOOD_NAME if self.prev_carried_food is not None else None
        }

    def on_death(self):
        if self.pet_config.ABILITY_TYPE == AbilityType.FAINTED:
            self.player.battle.add_hurt_or_fainted(self)

        if self.carried_food == FOOD_CONFIG[FoodType.HONEY]:
            bee_config = PET_CONFIG[PetType.BEE]
            bee = PetState(bee_config.BASE_HEALTH, bee_config.BASE_ATTACK, bee_config, self.player, self.state)
            self.player.battle.bees.append((self, bee))

    def _change_perm_health(self, amount: int):
        self._perm_health += amount
        self._perm_health = min(max(0, self._perm_health), 50)

    def _change_perm_attack(self, amount: int):
        self._perm_attack += amount
        self._perm_attack = min(max(0, self._perm_attack), 50)

    def _take_damage(self, amount: int):
        if not self.is_alive(): return

        if self.carried_food == FOOD_CONFIG[FoodType.GARLIC]:
            amount = max(amount - 2, 1)

        self.change_health(-amount)

        if self.pet_config.ABILITY_TYPE == AbilityType.HURT:
            self.player.battle.add_hurt_or_fainted(self)

        if not self.is_alive():
            self.on_death()

    def __repr__(self) -> str:
        return f"{self.pet_config.PET_NAME}:{self.id}"
