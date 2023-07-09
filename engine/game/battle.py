from copy import copy
from typing import TYPE_CHECKING, List, Optional

from engine.config.foodconfig import FOOD_CONFIG
from engine.config.foodtype import FoodType
from engine.config.roundconfig import RoundConfig
from engine.game.abilitytype import AbilityType

if TYPE_CHECKING:
    from engine.output.gamelog import GameLog
    from engine.state.gamestate import GameState
    from engine.state.petstate import PetState
    from engine.state.playerstate import PlayerState


class Battle:
    def __init__(self, player: 'PlayerState', challenger: 'PlayerState', state: 'GameState', log: 'GameLog'):
        self.player = player
        self.challenger = challenger
        self.state = state
        self.log = log

        self.hurt_and_faint_and_bee: List['PetState'] = []
        self.knockout: Optional['PetState'] = None

    def run(self):
        self._setup_battle()

        # End early if one of the players has no pets
        if len(self.player.battle_pets) == 0 or len(self.challenger.battle_pets) == 0:
            self._end_battle()
            return

        self._run_start_battle()
        while len(self.player.battle_pets) > 0 and len(self.challenger.battle_pets) > 0:
            self._run_attack_turn()

        self._end_battle()

    def add_hurt_or_fainted_or_bee(self, pet: 'PetState'):
        if pet not in self.hurt_and_faint_and_bee:
            self.hurt_and_faint_and_bee.append(pet)

    def _setup_battle(self):
        # Set opponent + create copy of pets (player.battle_pets)
        self.player.start_battle(self.challenger)
        self.challenger.start_battle(self.player)
        self._cleanup_battle_pets()

    def _run_start_battle(self):
        self._proc_battle_round_start()
        self._proc_hurt_and_faint()
        self._cleanup_battle_pets()

    def _run_attack_turn(self):
        self.hurt_and_faint_and_bee = []
        self.knockout = None

        player_front = self.player.battle_pets[0]
        challenger_front = self.challenger.battle_pets[0]

        self._proc_before_attack(player_front, challenger_front)

        player_front.damage_enemy_with_attack(challenger_front)
        challenger_front.damage_enemy_with_attack(player_front)
        self._add_to_knockout(player_front, challenger_front)

        self._proc_after_attack(player_front, challenger_front)
        self._proc_friend_ahead_attacked()
        self._proc_knockout()
        self._proc_hurt_and_faint()

        self._cleanup_battle_pets()

    def _end_battle(self):
        round_config = RoundConfig.get_round_config(self.state.round)

        player_lost = self._determine_winner()
        if player_lost:
            self.player.health -= round_config.HEALTH_LOST

        self.log.write_battle_stage_log(self.player, self.challenger, player_lost, round_config.HEALTH_LOST)

    # Remove dead pets and empty slots
    def _cleanup_battle_pets(self):
        self.player.battle_pets = [pet for pet in self.player.battle_pets if pet is not None and (pet.is_alive() or pet in self.hurt_and_faint_and_bee)]
        self.challenger.battle_pets = [pet for pet in self.challenger.battle_pets if pet is not None and (pet.is_alive() or pet in self.hurt_and_faint_and_bee)]

    # Higher level and stat pets get to go first
    def _priority_sort(self, pets: List['PetState']) -> List['PetState']:
        pets.sort(key = lambda pet: (pet.sub_level, pet.get_health() + pet.get_attack()), reverse = True)
        return pets

    def _determine_winner(self) -> bool:
        if len(self.player.battle_pets) == 0 and len(self.challenger.battle_pets) == 0:
            return None # Tied
        elif len(self.player.battle_pets) == 0:
            return True # Lost
        else:
            return False # Won

    def _proc_battle_round_start(self):
        battle_round_start: List['PetState'] = []
        battle_round_start += [pet for pet in self.player.battle_pets if pet.pet_config.ABILITY_TYPE == AbilityType.BATTLE_ROUND_START]
        battle_round_start += [pet for pet in self.challenger.battle_pets if pet.pet_config.ABILITY_TYPE == AbilityType.BATTLE_ROUND_START]

        for pet in self._priority_sort(battle_round_start):
            pet.pet_config.ABILITY_FUNC(pet, pet.player)

    def _proc_hurt_and_faint(self):
        while len(self.hurt_and_faint_and_bee) > 0:
            hurt_and_faint_and_bee = self._priority_sort(copy(self.hurt_and_faint_and_bee))
            self.hurt_and_faint_and_bee = [] # Clear the list so second-order events trigger

            for pet in hurt_and_faint_and_bee:
                if pet.pet_config.ABILITY_TYPE in [AbilityType.HURT, AbilityType.FAINTED]:
                    pet.pet_config.ABILITY_FUNC(pet, pet.player)
                if not pet.is_alive() and pet.carried_food == FOOD_CONFIG[FoodType.HONEY]:
                    pet.player.summon_bee(pet)

            self._cleanup_battle_pets()

    def _proc_before_attack(self, player_front: 'PetState', challenger_front: 'PetState'):
        before_attack: List['PetState'] = []
        if player_front.pet_config.ABILITY_TYPE == AbilityType.BEFORE_ATTACK:
            before_attack.append(player_front)
        if challenger_front.pet_config.ABILITY_TYPE == AbilityType.BEFORE_ATTACK:
            before_attack.append(challenger_front)

        for pet in self._priority_sort(before_attack):
            pet.pet_config.ABILITY_FUNC(pet, pet.player)

    def _proc_after_attack(self, player_front: 'PetState', challenger_front: 'PetState'):
        after_attack: List['PetState'] = []
        if player_front.pet_config.ABILITY_TYPE == AbilityType.AFTER_ATTACK:
            after_attack.append(player_front)
        if challenger_front.pet_config.ABILITY_TYPE == AbilityType.AFTER_ATTACK:
            after_attack.append(challenger_front)

        for pet in self._priority_sort(after_attack):
            pet.pet_config.ABILITY_FUNC(pet, pet.player)

    def _proc_friend_ahead_attacked(self):
        friend_ahead_attack: List['PetState'] = []
        if len(self.player.battle_pets) >= 2:
            pet = self.player.battle_pets[1]
            if pet.pet_config.ABILITY_TYPE == AbilityType.FRIEND_AHEAD_ATTACK:
                friend_ahead_attack.append(pet)
        if len(self.challenger.battle_pets) >= 2:
            pet = self.challenger.battle_pets[1]
            if pet.pet_config.ABILITY_TYPE == AbilityType.FRIEND_AHEAD_ATTACK:
                friend_ahead_attack.append(pet)

        for pet in self._priority_sort(friend_ahead_attack):
            pet.pet_config.ABILITY_FUNC(pet, pet.player)

    def _add_to_knockout(self, player_front: 'PetState', challenger_front: 'PetState'):
        if player_front.is_alive() and not challenger_front.is_alive():
            self.knockout = player_front
        elif challenger_front.is_alive() and not player_front.is_alive():
            self.knockout = challenger_front

    def _proc_knockout(self):
        if self.knockout is not None and self.knockout.pet_config.ABILITY_TYPE == AbilityType.KNOCKOUT:
            self.knockout.pet_config.ABILITY_FUNC(self.knockout, self.knockout.player)
