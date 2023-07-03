from engine.config.gameconfig import MAX_ROUNDS
from engine.game.battle import Battle
from engine.game.buystagehelper import BuyStageHelper
from engine.output.gamelog import GameLog
from engine.output.outputhandler import OutputHandler
from engine.state.gamestate import GameState


class GameEngine:
    def __init__(self):
        self.state = GameState()
        self.log = GameLog(self.state)
        self.output_handler = OutputHandler(self.state, self.log)
        self.buy_stage_helper = BuyStageHelper(self.state, self.log, self.output_handler)

    def run(self):
        while not self.state.is_game_over():
            if self.state.round >= MAX_ROUNDS or len(self.state.get_alive_players()) == 0:
                self.output_handler.terminate_cancel()

            print(f"New round {self.state.round + 1}")
            self.state.start_new_round()
            self.log.write_start_state_logs()
            players = self.state.get_alive_players()

            self.log.init_buy_stage_log()
            for player in players:
                self.buy_stage_helper.run(player)

            self.state.start_battle_stage()
            self.log.init_battle_stage_log()
            for player in players:
                battle = Battle(player, player.challenger, self.state, self.log)
                player.battle = battle
                player.challenger.battle = battle
                battle.run()

            self.state.end_round()

        self.output_handler.terminate_success(self.state.get_player_ranking())
