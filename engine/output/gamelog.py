from typing import TYPE_CHECKING, List, Optional, Tuple

from engine.config.gameconfig import NUM_PLAYERS

if TYPE_CHECKING:
    from engine.state.gamestate import GameState
    from engine.state.petstate import PetState
    from engine.state.playerstate import PlayerState


class GameLog:
    def __init__(self, state: 'GameState'):
        self.state = state

        # Per round, we store the starting state of each player
        self.start_state_logs: List[List[str]] = []

        # Per round, per player, we store the shop log + buy round moves
        self.buy_stage_logs: List[List[Tuple[bool, str, List[str]]]] = []

        # Per round, we store the outcomes of each battle
        self.battle_stage_logs: List[List[('PlayerState', str)]] = []

    def get_game_log(self, player: 'PlayerState') -> str:
        game_log = ""

        for round in range(self.state.round + 1):
            game_log += f"# Round {round + 1}\n\n"
            game_log += self._get_round_start_state_log(round, player)
            game_log += self._get_round_buy_stage_log(round, player)
            game_log += self._get_round_battle_stage_log(round, player)

        return game_log

    def write_start_state_logs(self):
        logs_per_player = []

        for player in self.state.players:
            log = ""
            if not player.is_alive():
                log += "- Eliminated"
            else:
                log += f"- {player.health} health remaining\n"
                for i, pet in enumerate(player.pets):
                    log += f"{i + 1}. {self._write_pet_log(pet)}\n"
            logs_per_player.append(log)

        self.start_state_logs.append(logs_per_player)

    def init_buy_stage_log(self):
        buy_stage_log = [(self.state.players[player_num].is_alive(), self._write_shop_log(self.state.players[player_num]), []) for player_num in range(NUM_PLAYERS)]
        self.buy_stage_logs.append(buy_stage_log)

    def write_buy_stage_log(self, player: 'PlayerState', log: str):
        _, _, logs = self.buy_stage_logs[self.state.round][player.player_num]
        logs.append(log)

    def init_battle_stage_log(self):
        self.battle_stage_logs.append([])

    def write_battle_stage_log(self, player: 'PlayerState', challenger: 'PlayerState', player_lost: Optional[bool], health_lost: int):
        log = ""

        if player_lost == True:
            log += f"P{player.player_num + 1} lost to P{challenger.player_num + 1}; "
            log += f"P{player.player_num + 1} lost {health_lost} health; "
            if player.is_alive():
                log += f"{player.health} health remaining"
            else:
                log += f"Eliminated"

        elif player_lost is None:
            log += f"P{player.player_num + 1} tied with P{challenger.player_num + 1}; "
            log += f"P{player.player_num + 1} has {player.health} health remaining"

        else:
            log += f"P{player.player_num + 1} beat P{challenger.player_num + 1}; "
            log += f"P{player.player_num + 1} has {player.health} health remaining"

        self.battle_stage_logs[self.state.round].append((player, log))

    def _get_round_start_state_log(self, round: int, player: 'PlayerState'):
        log = f"## Starting State\n\n"

        if round >= len(self.start_state_logs):
            log += f"Did not reach round {round + 1}\n\n"
            return log

        for player_num in range(NUM_PLAYERS):
            log += f"### "

            if player_num == player.player_num: log += "**"
            log += f"P{player_num + 1} "
            if player_num == player.player_num: log += "(self)** "

            round_start_log = self.start_state_logs[round][player_num]
            log += round_start_log
            log += "\n\n"

        return log

    def _get_round_buy_stage_log(self, round: int, player: 'PlayerState'):
        log = f"## Buy Stage\n"

        if round >= len(self.buy_stage_logs):
            log += f"Did not reach round {round + 1}\n\n"
            return log

        player_alive, shop_log, buy_logs = self.buy_stage_logs[round][player.player_num]

        # Return nothing if the player is already eliminated
        if not player_alive:
            return ""

        log += "### Shop\n"
        log += shop_log
        log += "\n"

        log += "### Moves\n"
        for i, buy_log in enumerate(buy_logs):
            log += f"{i + 1}. "
            log += buy_log
            log += "\n"

        log += "\n"
        return log
    
    def _get_round_battle_stage_log(self, round: int, player: 'PlayerState'):
        log = f"## Battle Stage\n"

        if round >= len(self.battle_stage_logs):
            log += f"Did not reach round {round + 1}\n\n"
            return log

        for _player, _log in self.battle_stage_logs[round]:
            log += "- "

            if _player == player: log += "**"
            log += _log
            if _player == player: log += "**"

            log += "\n"

        log += "\n"
        return log

    def _write_shop_log(self, player: 'PlayerState'):
        log = ""

        log += "Shop pets:\n"
        for i, pet in enumerate(player.shop_pets):
            log += f"{i + 1}. "
            log += f"\"{pet.pet_config.PET_NAME}\"; "
            log += f"{pet.get_perm_health()} health; "
            log += f"{pet.get_perm_attack()} attack\n"

        log += "\nShop foods:\n"
        for i, food in enumerate(player.shop_foods):
            log += f"{i + 1}. "
            log += f"\"{food.food_config.FOOD_NAME}\"\n"

        return log

    def _write_pet_log(self, pet: 'PetState') -> str:
        log = ""

        if pet is None:
            log += "None"
        else:
            log += f"\"{pet.pet_config.PET_NAME}\"; "
            log += f"{pet.get_perm_health()} health; "
            log += f"{pet.get_perm_attack()} attack; "
            log += f"Level {pet.get_level()}; "
            log += f"Sublevel progress {pet.get_sub_level_progress()}; "

            if pet.carried_food is None:
                log += f"No carried food"
            else:
                log += f"Carrying \"{pet.carried_food.FOOD_NAME}\""

        return log
