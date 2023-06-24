from json import dumps, loads
from signal import SIGALRM, alarm, signal
from typing import TYPE_CHECKING

from engine.config.gameconfig import NUM_PLAYERS
from engine.config.ioconfig import CORE_DIRECTORY, OPEN_PIPE_TIMEOUT_SECONDS, READ_PIPE_TIMEOUT_SECONDS, WRITE_PIPE_TIMEOUT_SECONDS
from engine.input.inputvalidator import InputValidator
from engine.input.movetype import MoveType
from engine.output.terminationtype import TerminationType
from engine.input.playerinput import PlayerInput

if TYPE_CHECKING:
    from engine.output.outputhandler import OutputHandler
    from engine.state.gamestate import GameState
    from engine.state.playerstate import PlayerState


class InputHelper:
    def __init__(self, state: 'GameState', output_handler: 'OutputHandler'):
        self.state = state
        self.output_handler = output_handler

        curr_player_num = 0

        def open_pipe_timeout_handler(a, b):
            self.output_handler.terminate_fail(TerminationType.OPEN_TIMEOUT, self.state.players[curr_player_num])
        signal(SIGALRM, open_pipe_timeout_handler)

        self.from_engine_pipes = []
        self.to_engine_pipes = []

        for curr_player_num in range(NUM_PLAYERS):
            alarm(OPEN_PIPE_TIMEOUT_SECONDS) # Enable timer
            self.from_engine_pipes.append(open(self._get_pipe_path(curr_player_num, from_engine = True), 'w'))
            self.to_engine_pipes.append(open(self._get_pipe_path(curr_player_num, from_engine = False), 'r'))
            alarm(0) # Disable timer

    def get_player_input(self, player: 'PlayerState', remaining_moves: int) -> 'PlayerInput':
        self._send_view_to_player(player, self.state.get_view(player, remaining_moves))
        input = self._receive_input_from_player(player)

        valid, reason = InputValidator.validate_input(input, player, self.state)
        if not valid:
            self.output_handler.terminate_fail(TerminationType.INVALID_MOVE, player, reason = reason)

        return input

    def _get_pipe_path(self, player_num, from_engine: bool) -> str:
        ending = "from_engine.pipe" if from_engine else "to_engine.pipe"
        return f"{CORE_DIRECTORY}/submission{player_num}/io/{ending}"

    def _send_view_to_player(self, player: 'PlayerState', view: dict):
        def write_pipe_timeout_handler(a, b):
            self.output_handler.terminate_fail(TerminationType.WRITE_TIMEOUT, player)
        signal(SIGALRM, write_pipe_timeout_handler)

        json = dumps(view)
        json += ";"

        alarm(WRITE_PIPE_TIMEOUT_SECONDS) # Enable timer
        self.from_engine_pipes[player.player_num].write(json)
        self.from_engine_pipes[player.player_num].flush()
        alarm(0) # Disable timer

    def _receive_input_from_player(self, player: 'PlayerState') -> 'PlayerInput':
        def read_pipe_timeout_handler(a, b):
            self.output_handler.terminate_fail(TerminationType.READ_TIMEOUT, player)
        signal(SIGALRM, read_pipe_timeout_handler)

        json = ''

        alarm(READ_PIPE_TIMEOUT_SECONDS) # Enable timer
        while not json or json[-1] != ';':
            json += self.to_engine_pipes[player.player_num].read(1)
        alarm(0) # Disable timer

        # Remove ";"
        json = json[:-1]

        try:
            input_dict = loads(json)
            move_type = MoveType[input_dict["move_type"]]
            return PlayerInput(move_type, input_dict)
        except Exception as exception:
            self.output_handler.terminate_fail(TerminationType.CANNOT_PARSE_INPUT, player, exception = exception)
