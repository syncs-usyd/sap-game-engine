from engine.output.gamelog import GameLog
from engine.state.gamestate import GameState
from engine.state.playerstate import PlayerState


class BattleStageHelper:
    def __init__(self, state: 'GameState', log: 'GameLog'):
        self.state = state
        self.log = log

    def run(self, player: 'PlayerState'):
        challenger = player.get_challenger(self.state)
        # TODO
        # Figure out who won the battle
        # if the player lost
        # reduce player health (Note: you lose more health in later rounds)

        player_lost = False
        health_lost = 0
        self.log.write_battle_stage_log(player, challenger, player_lost, health_lost)
