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