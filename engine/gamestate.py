from typing import List
from engine.config import NUM_PLAYERS
from engine.playerstate import PlayerState


class GameState:
    def __init__(self) -> 'GameState':
        self.round = -1
        self.players = [PlayerState(i) for i in range(NUM_PLAYERS)]

    def start_new_round(self):
        self.round += 1
        for player in self.players:
            player.start_new_round(self.round)

    def get_alive_players(self) -> List['PlayerState']:
        return [player for player in self.players if player.is_alive()]

    def is_game_over(self) -> bool:
        alive_players = self.get_alive_players()
        num_alive = len(alive_players)
        assert num_alive > 0
        return num_alive == 1

    def get_view(self, player: 'PlayerState', remaining_moves: int) -> dict:
        next_opponent = player.get_challenger(self, increment_index = False)
        other_players = [player for player in self.get_alive_players() if self.player != player]

        return {
            "remaining_moves": remaining_moves,
            "player_info": player.get_view_for_self(),
            "next_opponent_index": other_players.index(next_opponent),
            "other_players_info": [player.get_view_for_others() for player in other_players] 
        }
    