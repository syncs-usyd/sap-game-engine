from engine.state.gamestate import GameState
from engine.state.playerstate import PlayerState


class BattleHelper:
    def __init__(self, state: 'GameState'):
        self.state = state

    def run(self, player: 'PlayerState'):
        challenger = player.get_challenger(self.state)
        # TODO
        # Figure out who won the battle
        # if the player lost
        # reduce player health (Note: you lose more health in later rounds)