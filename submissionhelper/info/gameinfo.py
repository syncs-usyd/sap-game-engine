from typing import Dict, List

from submissionhelper.info.otherplayerinfo import OtherPlayerInfo
from submissionhelper.info.playerinfo import PlayerInfo


class GameInfo:
    def __init__(self, dict: Dict):
        self.dict = dict

        # Refers to which round it is. Starts at 1
        self.round_num: int = int(dict["round"])

        # Refers to the number of moves you are allowed to make
        # for the current buy round.
        # Note: this resets at the start of each buy round
        self.remaining_moves: int = int(dict["remaining_moves"])

        # Includes your pet & shop info as well as remaining health
        self.player_info: 'PlayerInfo' = PlayerInfo(dict["player_info"])

        # Contains the info of the remaining alive players
        self.other_players_info: List['OtherPlayerInfo'] = [OtherPlayerInfo(other_player_dict) for other_player_dict in dict["other_players_info"]]

        # A reference to your opponent in the next battle round
        self.next_opponent_info: 'OtherPlayerInfo' = self.other_players_info[int(dict["next_opponent_index"])]

    def __repr__(self) -> str:
        printable = "Game Info:\n"
        printable += "------------\n"

        printable += f"Round Num: {self.round_num}\n"
        printable += f"Remaining Moves: {self.remaining_moves}\n"

        printable += "Player Info: {\n"
        for line in repr(self.player_info).splitlines():
            printable += f"    {line}\n"
        printable += "}\n"

        printable += "Other Players Info: {\n"
        for i, other_player_info in enumerate(self.other_players_info):
            printable += f"    Player {i}"
            if other_player_info == self.next_opponent_info: printable += f" (next opponent)"
            printable += ": "
            printable += "{\n"
            for line in repr(other_player_info).splitlines():
                printable += f"        {line}\n"
            printable += "    }\n"
        printable += "}\n"

        printable += "------------"

        return printable
