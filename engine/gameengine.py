from engine.game.battlestagehelper import BattleStageHelper
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
        self.battle_stage_helper = BattleStageHelper(self.state, self.log)

    def run(self):
        while not self.state.is_game_over():
            print("New round!")
            self.state.start_new_round()
            self.log.write_start_state_logs()
            players = self.state.get_alive_players()

            print("Starting buy round")
            self.log.init_buy_stage_log()
            for player in players:
                print(f"Running buy round for {player.player_num}")
                self.buy_stage_helper.run(player)

            print("Starting battle round")
            self.state.start_battle_stage()
            self.log.init_battle_stage_log()
            for player in players:
                print(f"Running battle round for {player.player_num}")
                self.battle_stage_helper.run(player)

        self.output_handler.terminate_success(self.state.get_player_ranking())
