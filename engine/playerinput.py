from enum import Enum
from json import dumps
from signal import SIGALRM, alarm, signal
from engine.config import CORE_DIRECTORY, OPEN_PIPE_TIMEOUT_SECONDS, READ_PIPE_TIMEOUT_SECONDS, WRITE_PIPE_TIMEOUT_SECONDS
from engine.gamestate import GameState
from engine.inputvalidator import InputValidator
from engine.playerstate import PlayerState


class MoveType(Enum):
    BuyPet = 1
    BuyItem = 2
    UpgradePet = 3
    SellPet = 4
    Reroll = 5
    FreezePet = 6
    FreezeItem = 7
    SwapPet = 8
    EndTurn = 9

class InputHelper:
    def __init__(self) -> 'InputHelper':
        curr_player_num = 0

        # Setup timeout handler
        def open_pipe_timeout_handler(a, b):
            print(f"Terminate game for timeout...Submission {curr_player_num} is faulty")
        signal(SIGALRM, open_pipe_timeout_handler)

        # Open pipes
        self.from_engine_pipes = []
        self.to_engine_pipes = []
        for curr_player_num in range(5):
            alarm(OPEN_PIPE_TIMEOUT_SECONDS) # Enable timer
            self.from_engine_pipes.append(open(self.get_pipe_path(curr_player_num, from_engine = True), 'w'))
            self.to_engine_pipes.append(open(self.get_pipe_path(curr_player_num, from_engine = False), 'r'))
            alarm(0) # Disable timer

    def get_pipe_path(player_num, from_engine: bool) -> str:
        ending = "from_engine.pipe" if from_engine else "to_engine.pipe"
        return f"{CORE_DIRECTORY}/submission{player_num}/io/{ending}"

    def get_player_input(self, player: 'PlayerState', state: 'GameState', remaining_moves: int) -> 'PlayerInput':
        self.send_view_to_player(player, state.get_view(player, remaining_moves))
        input = self.receive_input_from_player(player)

        valid, reason = InputValidator.validate_input(input, player, state)
        if not valid:
            # TODO: terminate
            pass

        return input

    def send_view_to_player(self, player: 'PlayerState', view: dict):
        json =  dumps(view)
        json += ";"

        # Setup timeout handler
        def write_pipe_timeout_handler(a, b):
            print(f"Terminate game for timeout...Submission {player.player_num} is faulty")
        signal(SIGALRM, write_pipe_timeout_handler)

        alarm(WRITE_PIPE_TIMEOUT_SECONDS) # Enable timer
        self.from_engine_pipes[player.player_num].write(json)
        self.from_engine_pipes[player.player_num].flush()
        alarm(0) # Disable timer

    def receive_input_from_player(self, player: 'PlayerState') -> 'PlayerInput':
        # Setup timeout handler
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

class PlayerInput:
    def __init__(self, move_type: 'MoveType', input_dict: dict) -> 'PlayerInput':
        self.move_type = move_type

        if move_type == MoveType.BuyPet:
            self.parse_buy_pet(input_dict)
        elif move_type == MoveType.BuyItem:
            self.parse_buy_item(input_dict)
        elif move_type == MoveType.UpgradePet:
            self.parse_upgrade_pet(input_dict)
        elif move_type == MoveType.SellPet:
            self.parse_sell_pet(input_dict)
        elif move_type == MoveType.Reroll:
            self.parse_reroll(input_dict)
        elif move_type == MoveType.FreezePet:
            self.parse_freeze_pet(input_dict)
        elif move_type == MoveType.FreezeItem:
            self.parse_freeze_item(input_dict)
        elif move_type == MoveType.SwapPet:
            self.parse_swap_pet(input_dict)
        elif move_type == MoveType.EndTurn:
            self.parse_end_turn(input_dict)
        else:
            raise Exception(f'Invalid move type: {move_type}')

    def parse_buy_pet(self, input_dict):
        pass

    def parse_buy_item(self, input_dict):
        pass

    def parse_upgrade_pet(self, input_dict):
        pass

    def parse_sell_pet(self, input_dict):
        pass

    def parse_reroll(self, input_dict):
        pass

    def parse_freeze_pet(self, input_dict):
        pass

    def parse_freeze_item(self, input_dict):
        pass

    def parse_swap_pet(self, input_dict):
        pass

    def parse_end_turn(self, input_dict):
        pass