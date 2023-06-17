from engine.game.battlehelper import BattleHelper
from engine.game.buyroundhelper import BuyRoundHelper
from engine.input.inputhelper import InputHelper
from engine.state.gamestate import GameState


class GameEngine:
    def __init__(self) -> 'GameEngine':
        self.state = GameState()
        self.buy_round_helper = BuyRoundHelper()
        self.battle_helper = BattleHelper()
        self.input_helper = InputHelper()

    def run(self):
        while not self.state.is_game_over():
            self.state.start_new_round()
            players = self.state.get_alive_players()

            for player in players:
                self.buy_round_helper.run(player)

            for player in players:
                self.battle_helper.run(player)

        # TODO: return winner