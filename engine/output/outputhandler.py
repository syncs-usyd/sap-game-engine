import json
import shutil
import sys
from traceback import TracebackException
from typing import TYPE_CHECKING, List, Optional

from engine.config.ioconfig import CORE_DIRECTORY
from engine.output.terminationtype import TerminationType

if TYPE_CHECKING:
    from engine.output.gamelog import GameLog
    from engine.state.gamestate import GameState
    from engine.state.playerstate import PlayerState


class OutputHandler:
    def __init__(self, state: 'GameState', log: 'GameLog'):
        self.state = state
        self.log = log

    def terminate_success(self, player_ranking: List[int]):
        print(f"Player {player_ranking[0] + 1} won!")
        self._write_results(TerminationType.SUCCESS, player_ranking = player_ranking)

        # Write the game log for each player
        for player in self.state.players:
            self._write_game_log(player.player_num, self.log.get_game_log(player))

        # Copy all the players stdout so they can see debug info
        for player in self.state.players:
            self._copy_player_stdout(player.player_num)

        #End the game
        sys.exit(0)

    def terminate_cancel(self):
        self._write_results(TerminationType.CANCELLED_MATCH)
        sys.exit(0) # End the game

    def terminate_fail(self, termination_type: 'TerminationType', player: 'PlayerState', exception: Optional[Exception] = None, reason: Optional[str] = None):
        self._write_results(termination_type, faulty_player_num = player.player_num)

        # Write the game log for the faulty player
        self._write_game_log(player.player_num, self.log.get_game_log(player))

        # If we're given an exception or reason, we will populate the stderr with it
        error: str = None
        if exception is not None:
            error = "".join(TracebackException.from_exception(exception).format())
        elif reason is not None:
            error = reason

        # If no error is given, we will just copy stderr from
        # their submission in case it contains valuable information
        if error is not None:
            self._write_player_stderr(player.player_num, error)
        else:
            self._copy_player_stderr(player.player_num)

        self._copy_player_stdout(player.player_num)

        # End the game
        sys.exit(0)

    def _write_results(self, termination_type: 'TerminationType', faulty_player_num: Optional[int] = None, player_ranking: Optional[List[int]] = None):
        results: dict = None

        if termination_type == TerminationType.SUCCESS:
            results = {
                "result_type": termination_type.name,
                "ranking": player_ranking
            }

        elif termination_type == TerminationType.CANCELLED_MATCH:
            results = {
                "result_type": termination_type.name
            }

        else:
            results = {
                "result_type": termination_type.name,
                "submission_responsible": faulty_player_num
            }

        # TODO add json schema
        # jsonschema.validate(data, RESULTS_SCHEMA)

        with open(f"{CORE_DIRECTORY}/output/results.json", 'w') as file:
            json.dump(results, file)

    def _write_game_log(self, player_num: int, game_log: str):
        with open(f"{CORE_DIRECTORY}/output/game_{player_num}.md", 'w') as file:
            file.write(game_log)

    def _write_player_stderr(self, player_num: int, error: str):
        with open(f"{CORE_DIRECTORY}/output/submission_{player_num}.err", 'w') as file:
            file.write(error)

    def _copy_player_stderr(self, player_num: int):
        submission_path = f"{CORE_DIRECTORY}/submission{player_num}/io/submission.err"
        output_path = f"{CORE_DIRECTORY}/output/submission_{player_num}.err"

        try:
            shutil.copy(submission_path, output_path, follow_symlinks = False)
        except (FileNotFoundError, IsADirectoryError, FileExistsError):
            with open(output_path, 'w') as file:
                file.write("Nice try. Please don't delete your submission.err file")

    def _copy_player_stdout(self, player_num: int):
        submission_path = f"{CORE_DIRECTORY}/submission{player_num}/io/submission.log"
        output_path = f"{CORE_DIRECTORY}/output/submission_{player_num}.log"

        try:
            shutil.copy(submission_path, output_path, follow_symlinks = False)
        except (FileNotFoundError, IsADirectoryError, FileExistsError):
            with open(output_path, 'w') as file:
                file.write("Nice try. Please don't delete your submission.log file")
