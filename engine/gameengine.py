from engine.config import MAX_MOVES_PER_ROUND
from engine.gamestate import GameState
from engine.playerinput import MoveType, PlayerInput
from engine.playerstate import PlayerState


class GameEngine:
    def __init__(self) -> 'GameEngine':
        self.state = GameState()

    def run(self):
        while not self.state.is_game_over():
            self.state.start_new_round()
            players = self.state.get_alive_players()

            for player in players:
                self.run_buy_round(player)

            for player in players:
                self.run_battle(player)

        # TODO: return winner

    def run_buy_round(self, player: 'PlayerState'):
        for moves in range(MAX_MOVES_PER_ROUND):
            input = PlayerInput.get_player_input(player, self.state, MAX_MOVES_PER_ROUND - moves)
            if input.move_type == MoveType.BuyPet:
                self.buy_pet()
            elif input.move_type == MoveType.BuyItem:
                self.buy_item()
            elif input.move_type == MoveType.UpgradePet:
                self.upgrade_pet()
            elif input.move_type == MoveType.SellPet:
                self.sell_pet()
            elif input.move_type == MoveType.Reroll:
                self.reroll()
            elif input.move_type == MoveType.FreezePet:
                self.freeze_pet()
            elif input.move_type == MoveType.FreezeItem:
                self.freeze_item()
            elif input.move_type == MoveType.SwapPet:
                self.swap_pet()
            elif input.move_type == MoveType.EndTurn:
                return
            else:
                raise Exception(f'Invalid move type: {input.move_type}')

        # TODO: end the game if we get here because the player
        # has used up its allocated number of turns

    def run_battle(self, player: 'PlayerState'):
        challenger = player.get_challenger(self.state)
        # TODO
        # Figure out who won the battle
        # if the player lost
        # reduce player health (Note: you lose more health in later rounds)

    def buy_pet(player: 'PlayerState', input: 'PlayerInput'):
        pass

    def buy_item(player: 'PlayerState', input: 'PlayerInput'):
        pass

    def upgrade_pet(player: 'PlayerState', input: 'PlayerInput'):
        pass

    def sell_pet(player: 'PlayerState', input: 'PlayerInput'):
        pass

    def reroll(player: 'PlayerState', input: 'PlayerInput'):
        pass

    def freeze_pet(player: 'PlayerState', input: 'PlayerInput'):
        pass

    def freeze_item(player: 'PlayerState', input: 'PlayerInput'):
        pass

    def swap_pet(player: 'PlayerState', input: 'PlayerInput'):
        pass
