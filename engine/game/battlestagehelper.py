from copy import deepcopy
from typing import Optional

from engine.config.roundconfig import RoundConfig
from engine.game.abilitytype import AbilityType
from engine.output.gamelog import GameLog
from engine.state.gamestate import GameState
from engine.state.petstate import PetState
from engine.state.playerstate import PlayerState


class BattleStageHelper:
    def __init__(self, state: 'GameState', log: 'GameLog'):
        self.state = state
        self.log = log

    def run(self, player: 'PlayerState'):
        player.start_battle(player.challenger)
        player.challenger.start_battle(player)

        # Actually run the battle
        player_lost = self._determine_winner(player, player.challenger)

        round_config = RoundConfig.get_round_config(self.state.round)
        if player_lost:
            player.health -= round_config.HEALTH_LOST

        self.log.write_battle_stage_log(player, player.challenger, player_lost, round_config.HEALTH_LOST)

    def _determine_winner(self, player: 'PlayerState', challenger: 'PlayerState') -> Optional[bool]:
        self._check_battle_round_start(player)
        self._check_battle_round_start(challenger)

        # Go round by round until someone has no pets
        while len(player.battle_pets) > 0 or len(challenger.battle_pets) > 0:
            self._start_next_battle_turn(player)
            self._start_next_battle_turn(challenger)

            player_front = player.battle_pets[0]
            challenger_front = challenger.battle_pets[0]

            player_front.proc_ability(AbilityType.BEFORE_ATTACK)
            challenger_front.proc_ability(AbilityType.BEFORE_ATTACK)

            player_front.take_damage(challenger_front.attack)
            challenger_front.take_damage(player_front.attack)

            self._check_after_attack(player_front)
            self._check_after_attack(challenger_front)

            self._check_friend_ahead_attacked(player)
            self._check_friend_ahead_attacked(challenger)

            player.cleanup_battle_pets()
            challenger.cleanup_battle_pets()

        if len(player.battle_pets) == 0 and len(challenger.battle_pets) == 0:
            return None # Tied
        elif len(player.battle_pets) == 0:
            return True # Lost
        else:
            return False # Won

    def _start_next_battle_turn(self, player: 'PlayerState'):
        for pet in player.battle_pets:
            pet.start_next_battle_turn()

    def _check_battle_round_start(self, player: 'PlayerState'):
        for pet in player.battle_pets:
            pet.proc_ability(AbilityType.BATTLE_ROUND_START)

    def _check_after_attack(self, pet: 'PetState'):
        if pet.is_alive():
            pet.proc_ability(AbilityType.AFTER_ATTACK)

    def _check_friend_ahead_attacked(self, player: 'PlayerState'):
        if len(player.battle_pets) > 1:
            player.battle_pets[1].proc_ability(AbilityType.FRIEND_AHEAD_ATTACK)
