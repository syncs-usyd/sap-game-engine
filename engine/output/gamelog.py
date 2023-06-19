from typing import List, Optional

from engine.config.gameconfig import NUM_PLAYERS
from engine.input.movetype import MoveType
from engine.input.playerinput import PlayerInput
from engine.state.gamestate import GameState
from engine.state.petstate import PetState
from engine.state.playerstate import PlayerState


class GameLog:
    def __init__(self, state: 'GameState'):
        self.state = state

        # Per round, we store the starting state of each player
        self.start_state_logs: List[List[str]] = []

        # Per round, per player, we store the buy round moves
        self.buy_stage_logs: List[List[List[str]]] = []

        # Per round, we store the outcomes of each battle
        self.battle_stage_logs: List[List[str]] = []

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
                    log += f"{i + 1}. {self._write_pet_log(pet)}"
            logs_per_player.append(log)

        self.start_state_logs.append(logs_per_player)
        self.buy_stage_logs.append([[] for _ in range(NUM_PLAYERS)])
        self.battle_stage_logs.append([])

    def write_buy_stage_log(self, player: 'PlayerState', input: 'PlayerInput'):
        log = ""

        if input.move_type == MoveType.BUY_PET:
            log = ""
        elif input.move_type == MoveType.BUY_ITEM:
            log = ""
        elif input.move_type == MoveType.UPGRADE_PET:
            log = ""
        elif input.move_type == MoveType.SELL_PET:
            log = ""
        elif input.move_type == MoveType.REROLL:
            log = ""
        elif input.move_type == MoveType.FREEZE_PET:
            log = ""
        elif input.move_type == MoveType.FREEZE_ITEM:
            log = ""
        elif input.move_type == MoveType.SWAP_PET:
            log = ""
        elif input.move_type == MoveType.END_TURN:
            return
        else:
            raise Exception(f'Invalid move type: {input.move_type}')

        self.buy_stage_logs[self.state.round][player.player_num].append(log)

    def write_battle_stage_log(self, player: 'PlayerState', challenger: 'PlayerState', player_lost: Optional[bool], health_lost: int):
        log = ""

        if player_lost == True:
            log += f"P{player.player_num + 1} lost to P{challenger.player_num + 1}; "
            log += f"P{player.player_num + 1} lost {health_lost} health; "
            if player.is_alive():
                log += f"{player.health} health remaining"
            else:
                log += f"Eliminated :("

        elif player_lost is None:
            log += f"P{player.player_num + 1} tied with P{challenger.player_num + 1}; "
            log += f"P{player.player_num + 1} has {player.health} health remaining"

        else:
            log += f"P{player.player_num + 1} beat P{challenger.player_num + 1}; "
            log += f"P{player.player_num + 1} has {player.health} health remaining"

        self.battle_stage_logs[self.state.round].append(log)

    def _get_round_start_state_log(self, round: int, player: 'PlayerState'):
        log = f"## Starting State\n\n"

        for player_num in range(NUM_PLAYERS):
            log += f"### P{player_num + 1} "
            if player_num == player.player_num:
                log += "(self) "

            round_start_log = self.start_state_logs[round][player_num]
            log += round_start_log
            log += "\n\n"

        return log

    def _get_round_buy_stage_log(self, round: int, player: 'PlayerState'):
        log = f"## Buy Stage\n"

        for i, buy_log in enumerate(self.buy_stage_logs[round][player.player_num]):
            log += f"{i + 1}. "
            log += buy_log
            log += "\n"

        log += "\n"
        return log
    
    def _get_round_battle_stage_log(self, round: int, player: 'PlayerState'):
        log = f"## Battle Stage\n"

        for player_num in range(NUM_PLAYERS):
            log += "- "

            if player_num == player.player_num: log += "*"
            log += self.battle_stage_logs[round][player_num]
            if player_num == player.player_num: log += "*"

            log += "\n"

        log += "\n"
        return log

    def _write_pet_log(self, pet: 'PetState') -> str:
        log = ""

        if pet is None:
            log += "None"
        else:
            log += f"\"{pet.pet_config.PET_NAME}\"; "
            log += f"{pet.perm_health} health; "
            log += f"{pet.perm_attack} attack; "
            log += f"Level {pet.get_level()}; "
            log += f"Sublevel progress {pet.get_sub_level_progress()}; "

            if pet.carried_food is None:
                log += f"No carried food"
            else:
                log += f"Carrying \"{pet.carried_food.FOOD_NAME}\""

        return log
