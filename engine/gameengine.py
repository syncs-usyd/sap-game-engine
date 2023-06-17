from engine.game.battlehelper import BattleHelper
from engine.game.buyroundhelper import BuyRoundHelper
from engine.output.outputhandler import OutputHandler
from engine.state.gamestate import GameState


class GameEngine:
    def __init__(self):
        self.state = GameState()
        self.output_handler = OutputHandler(self.state)
        self.buy_round_helper = BuyRoundHelper(self.state, self.output_handler)
        self.battle_helper = BattleHelper(self.state)

    def run(self):
        while not self.state.is_game_over():
            self.state.start_new_round()
            players = self.state.get_alive_players()

            for player in players:
                self.buy_round_helper.run(player)

            for player in players:
                self.battle_helper.run(player)

        self.output_handler.terminate_success(self.state.get_player_ranking())
