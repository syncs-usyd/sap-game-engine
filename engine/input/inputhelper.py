from json import dumps
from signal import SIGALRM, alarm, signal

from engine.config.ioconfig import CORE_DIRECTORY, OPEN_PIPE_TIMEOUT_SECONDS, READ_PIPE_TIMEOUT_SECONDS, WRITE_PIPE_TIMEOUT_SECONDS
from engine.input.inputvalidator import InputValidator
from engine.input.movetype import MoveType
from engine.input.playerinput import PlayerInput
from engine.output.outputhandler import OutputHandler
from engine.state.gamestate import GameState
from engine.state.playerstate import PlayerState


class InputHelper:
    def __init__(self, output_handler: 'OutputHandler'):
        self.output_handler = output_handler

        curr_player_num = 0

        def open_pipe_timeout_handler(a, b):
            print(f"Terminate game for timeout...Submission {curr_player_num} is faulty")
        signal(SIGALRM, open_pipe_timeout_handler)

        self.from_engine_pipes = []
        self.to_engine_pipes = []

        for curr_player_num in range(5):
            alarm(OPEN_PIPE_TIMEOUT_SECONDS) # Enable timer
            self.from_engine_pipes.append(open(self._get_pipe_path(curr_player_num, from_engine = True), 'w'))
            self.to_engine_pipes.append(open(self._get_pipe_path(curr_player_num, from_engine = False), 'r'))
            alarm(0) # Disable timer

    def get_player_input(self, player: 'PlayerState', state: 'GameState', remaining_moves: int) -> 'PlayerInput':
        self._send_view_to_player(player, state.get_view(player, remaining_moves))
        input = self._receive_input_from_player(player)

        valid, reason = InputValidator.validate_input(input, player, state)
        if not valid:
            # TODO: terminate
            pass

        return input

    def _get_pipe_path(self, player_num, from_engine: bool) -> str:
        ending = "from_engine.pipe" if from_engine else "to_engine.pipe"
        return f"{CORE_DIRECTORY}/submission{player_num}/io/{ending}"

    def _send_view_to_player(self, player: 'PlayerState', view: dict):
        def write_pipe_timeout_handler(a, b):
            print(f"Terminate game for timeout...Submission {player.player_num} is faulty")
        signal(SIGALRM, write_pipe_timeout_handler)

        json =  dumps(view)
        json += ";"

        alarm(WRITE_PIPE_TIMEOUT_SECONDS) # Enable timer
        self.from_engine_pipes[player.player_num].write(json)
        self.from_engine_pipes[player.player_num].flush()
        alarm(0) # Disable timer

    def _receive_input_from_player(self, player: 'PlayerState') -> 'PlayerInput':
        def read_pipe_timeout_handler(a, b):
            print(f"Terminate game for timeout...Submission {player.player_num} is faulty")
        signal(SIGALRM, read_pipe_timeout_handler)

        json = ''

        alarm(READ_PIPE_TIMEOUT_SECONDS) # Enable timer
        while not json or json[-1] != ';':
            json += self.to_engine_pipes[player.player_num].read(1)
        alarm(0) # Disable timer

        # Remove ";"
        json = json[:-1]

        try:
            input_dict = json.loads(json)
            move_type = MoveType[input_dict["move_type"]]
            input = PlayerInput(move_type, input_dict)
        except:
            # TODO terminate
            pass

        return input
