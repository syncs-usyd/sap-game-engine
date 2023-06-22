from typing import Dict, List

from submissionhelper.info.otherplayerinfo import OtherPlayerInfo
from submissionhelper.info.playerinfo import PlayerInfo


class GameInfo:
    def __init__(self, dict: Dict):
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
