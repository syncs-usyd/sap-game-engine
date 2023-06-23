from enum import Enum


class TerminationType(Enum):
    SUCCESS = 1
    OPEN_TIMEOUT = 2
    WRITE_TIMEOUT = 3
    READ_TIMEOUT = 4
    INVALID_MOVE = 5
    CANNOT_PARSE_INPUT = 6
