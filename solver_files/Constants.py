from enum import Enum


class Directions(str, Enum):
    UP = "UP"
    DOWN = "DOWN"
    LEFT = "LEFT"
    RIGHT = "RIGHT"

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value


class PieceNames(str, Enum):
    HORI_2 = 'a'
    VERT_2 = 'b'
    SINGL = 'c'
    BIG_BLOCK = 'd'
    TAIL = 'x'
    EMPTY = 'O'

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value
