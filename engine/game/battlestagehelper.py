from copy import deepcopy
from typing import List, Optional
from engine.config.roundconfig import RoundConfig

from engine.output.gamelog import GameLog
from engine.state.gamestate import GameState
from engine.state.petstate import PetState
from engine.state.playerstate import PlayerState


class BattleStageHelper:
    def __init__(self, state: 'GameState', log: 'GameLog'):
        self.state = state
        self.log = log

    def run(self, player: 'PlayerState'):
        challenger = player.get_challenger()
        player_lost = self._determine_winner(player, challenger)

        round_config = RoundConfig.get_round_config(self.state.round)
        if player_lost:
            player.health -= round_config.HEALTH_LOST

        self.log.write_battle_stage_log(player, challenger, player_lost, round_config.HEALTH_LOST)

    def _determine_winner(self, player: 'PlayerState', challenger: 'PlayerState') -> Optional[bool]:
        player_pets = self._clear_dead_and_empty(deepcopy(player.pets))
        challenger_pets = self._clear_dead_and_empty(deepcopy(challenger.pets))

        # TODO: go through battle start abilities

        # Go round by round until someone has no pets
        while len(player_pets) > 0 or len(challenger_pets) > 0:
            player_front = player_pets[0]
            challenger_front = challenger_pets[0]

            # go through before attack abilities

            # Probably move this into a method on pet state
            # to better handle attacking non-infront enemies

            player_front.health -= challenger_front.attack
            challenger_front.health -= player_front.attack

            # go through hurt abilities

            # go through knockout abilities

            # go through player in front attacked abilities

            # Cleanup pets
            player_pets = self._clear_dead_and_empty(player_pets)
            challenger_pets = self._clear_dead_and_empty(challenger_pets)

        if len(player_pets) == 0 and len(challenger_pets) == 0:
            return None # Tied
        elif len(player_pets) == 0:
            return True # Lost
        else:
            return False # Won

    def _clear_dead_and_empty(self, pets: List[Optional['PetState']]) -> List['PetState']:
        return [pet for pet in pets if pet is not None and pet.is_alive()]