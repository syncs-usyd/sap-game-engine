from typing import List

from engine.config.gameconfig import NUM_PLAYERS
from engine.state.playerstate import PlayerState


class GameState:
    def __init__(self):
        self.round = -1
        self.players = [PlayerState(i, self) for i in range(NUM_PLAYERS)]
        self.dead_players: List['PlayerState'] = []
        self._next_id = 0

    def start_new_round(self):
        self.round += 1
        for player in self.players:
            player.start_new_round()

    def start_battle_stage(self):
        for player in self.get_alive_players():
            player.start_battle_stage()

    def end_round(self):
        for player in self.players:
            if not player.is_alive() and player not in self.dead_players:
                self.dead_players.append(player)

    def get_alive_players(self) -> List['PlayerState']:
        return [player for player in self.players if player.is_alive()]

    def is_game_over(self) -> bool:
        alive_players = self.get_alive_players()
        num_alive = len(alive_players)
        return num_alive == 1

    def get_player_ranking(self) -> List[int]:
        player_ranking = []

        # Add the winning player
        player_ranking.append(self.get_alive_players()[0].player_num)

        # Add the dead players
        # Latest death is at the end of the list so we traverse in reverse
        for player in reversed(self.dead_players):
            player_ranking.append(player.player_num)

        return player_ranking

    def get_view(self, player: 'PlayerState', remaining_moves: int) -> dict:
        next_opponent = player.challenger
        other_players = [alive_player for alive_player in self.get_alive_players() if alive_player != player]

        return {
            "round": self.round + 1,
            "remaining_moves": remaining_moves,
            "player_info": player.get_view_for_self(),
            "next_opponent_index": other_players.index(next_opponent),
            "other_players_info": [other_player.get_view_for_others() for other_player in other_players] 
        }

    def get_id(self) -> int:
        id = self._next_id
        self._next_id += 1
        return id