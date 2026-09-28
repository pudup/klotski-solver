import copy
import random
from solver_files.Constants import Directions, PieceNames

zobrist_hash_table = [[[random.randint(1, 2 ** 64 - 1) for i in range(4)] for j in range(5)] for k in range(6)]


class Board:
    def __init__(self, grid):
        self.board = []
        self.hashes = []

        self.set_position(grid)
        self.moves = self.get_possible_moves()

    def set_position(self, new):
        self.board = copy.deepcopy(new)

    def get_piece_positions(self):

        pieces = []
        piece_names = {PieceNames.HORI_2, PieceNames.VERT_2, PieceNames.SINGL, PieceNames.BIG_BLOCK}

        for i in range(1, 6):
            for j in range(1, 5):
                if self.board[i][j] in piece_names:
                    pieces.append([self.board[i][j], (i, j)])

        return pieces

    def get_possible_moves(self):
        pieces = self.get_piece_positions()
        piece_moves = []

        for piece in pieces:
            it = piece[0]
            pos_i, pos_j = piece[1]
            piece.append([])

            match it:
                case PieceNames.HORI_2:
                    # Up Check
                    if self.board[pos_i - 1][pos_j] == PieceNames.EMPTY:
                        piece[2].append(Directions.UP)
                    # Down Check
                    if self.board[pos_i + 2][pos_j] == PieceNames.EMPTY:
                        piece[2].append(Directions.DOWN)
                    # Left Check
                    if self.board[pos_i][pos_j - 1] == PieceNames.EMPTY and self.board[pos_i + 1][
                        pos_j - 1] == PieceNames.EMPTY:
                        piece[2].append(Directions.LEFT)
                    # Right Check
                    if self.board[pos_i][pos_j + 1] == PieceNames.EMPTY and self.board[pos_i + 1][
                        pos_j + 1] == PieceNames.EMPTY:
                        piece[2].append(Directions.RIGHT)
                case PieceNames.VERT_2:
                    # Up Check
                    if self.board[pos_i - 1][pos_j] == PieceNames.EMPTY and self.board[pos_i - 1][
                        pos_j + 1] == PieceNames.EMPTY:
                        piece[2].append(Directions.UP)
                    # Down Check
                    if self.board[pos_i + 1][pos_j] == PieceNames.EMPTY and self.board[pos_i + 1][
                        pos_j + 1] == PieceNames.EMPTY:
                        piece[2].append(Directions.DOWN)
                    # Left Check
                    if self.board[pos_i][pos_j - 1] == PieceNames.EMPTY:
                        piece[2].append(Directions.LEFT)
                    # Right Check
                    if self.board[pos_i][pos_j + 2] == PieceNames.EMPTY:
                        piece[2].append(Directions.RIGHT)
                case PieceNames.SINGL:
                    # Up Check
                    if self.board[pos_i - 1][pos_j] == PieceNames.EMPTY:
                        piece[2].append(Directions.UP)
                    # Down Check
                    if self.board[pos_i + 1][pos_j] == PieceNames.EMPTY:
                        piece[2].append(Directions.DOWN)
                    # Left Check
                    if self.board[pos_i][pos_j - 1] == PieceNames.EMPTY:
                        piece[2].append(Directions.LEFT)
                    # Right Check
                    if self.board[pos_i][pos_j + 1] == PieceNames.EMPTY:
                        piece[2].append(Directions.RIGHT)
                case PieceNames.BIG_BLOCK:
                    # Up Check
                    if self.board[pos_i - 1][pos_j] == PieceNames.EMPTY and self.board[pos_i - 1][
                        pos_j + 1] == PieceNames.EMPTY:
                        piece[2].append(Directions.UP)
                    # Down Check
                    if self.board[pos_i + 2][pos_j] == PieceNames.EMPTY and self.board[pos_i + 2][
                        pos_j + 1] == PieceNames.EMPTY:
                        piece[2].append(Directions.DOWN)
                    # Left Check
                    if self.board[pos_i][pos_j - 1] == PieceNames.EMPTY and self.board[pos_i + 1][
                        pos_j - 1] == PieceNames.EMPTY:
                        piece[2].append(Directions.LEFT)
                    # Right Check
                    if self.board[pos_i][pos_j + 2] == PieceNames.EMPTY and self.board[pos_i + 1][
                        pos_j + 2] == PieceNames.EMPTY:
                        piece[2].append(Directions.RIGHT)

            if piece[2]:
                piece_moves.append(piece)

        return piece_moves

    def move_piece(self, piece_name, piece_coord, direction):
        it = piece_name
        pos_i, pos_j = piece_coord

        match it:
            case PieceNames.HORI_2:
                match direction:
                    case Directions.UP:
                        self.board[pos_i - 1][pos_j] = PieceNames.HORI_2
                        self.board[pos_i][pos_j] = PieceNames.TAIL
                        self.board[pos_i + 1][pos_j] = PieceNames.EMPTY
                    case Directions.DOWN:
                        self.board[pos_i + 1][pos_j] = PieceNames.HORI_2
                        self.board[pos_i + 2][pos_j] = PieceNames.TAIL
                        self.board[pos_i][pos_j] = PieceNames.EMPTY
                    case Directions.LEFT:
                        self.board[pos_i][pos_j - 1] = PieceNames.HORI_2
                        self.board[pos_i + 1][pos_j - 1] = PieceNames.TAIL
                        self.board[pos_i][pos_j] = PieceNames.EMPTY
                        self.board[pos_i + 1][pos_j] = PieceNames.EMPTY
                    case Directions.RIGHT:
                        self.board[pos_i][pos_j + 1] = PieceNames.HORI_2
                        self.board[pos_i + 1][pos_j + 1] = PieceNames.TAIL
                        self.board[pos_i][pos_j] = PieceNames.EMPTY
                        self.board[pos_i + 1][pos_j] = PieceNames.EMPTY
            case PieceNames.VERT_2:
                match direction:
                    case Directions.UP:
                        self.board[pos_i - 1][pos_j] = PieceNames.VERT_2
                        self.board[pos_i - 1][pos_j + 1] = PieceNames.TAIL
                        self.board[pos_i][pos_j] = PieceNames.EMPTY
                        self.board[pos_i][pos_j + 1] = PieceNames.EMPTY
                    case Directions.DOWN:
                        self.board[pos_i + 1][pos_j] = PieceNames.VERT_2
                        self.board[pos_i + 1][pos_j + 1] = PieceNames.TAIL
                        self.board[pos_i][pos_j] = PieceNames.EMPTY
                        self.board[pos_i][pos_j + 1] = PieceNames.EMPTY
                    case Directions.LEFT:
                        self.board[pos_i][pos_j - 1] = PieceNames.VERT_2
                        self.board[pos_i][pos_j] = PieceNames.TAIL
                        self.board[pos_i][pos_j + 1] = PieceNames.EMPTY
                    case Directions.RIGHT:
                        self.board[pos_i][pos_j + 1] = PieceNames.VERT_2
                        self.board[pos_i][pos_j + 2] = PieceNames.TAIL
                        self.board[pos_i][pos_j] = PieceNames.EMPTY
            case PieceNames.SINGL:
                match direction:
                    case Directions.UP:
                        self.board[pos_i - 1][pos_j] = PieceNames.SINGL
                        self.board[pos_i][pos_j] = PieceNames.EMPTY
                    case Directions.DOWN:
                        self.board[pos_i + 1][pos_j] = PieceNames.SINGL
                        self.board[pos_i][pos_j] = PieceNames.EMPTY
                    case Directions.LEFT:
                        self.board[pos_i][pos_j - 1] = PieceNames.SINGL
                        self.board[pos_i][pos_j] = PieceNames.EMPTY
                    case Directions.RIGHT:
                        self.board[pos_i][pos_j + 1] = PieceNames.SINGL
                        self.board[pos_i][pos_j] = PieceNames.EMPTY
            case PieceNames.BIG_BLOCK:
                match direction:
                    case Directions.UP:
                        self.board[pos_i - 1][pos_j] = PieceNames.BIG_BLOCK
                        self.board[pos_i - 1][pos_j + 1] = PieceNames.TAIL
                        self.board[pos_i][pos_j] = PieceNames.TAIL
                        self.board[pos_i][pos_j + 1] = PieceNames.TAIL
                        self.board[pos_i + 1][pos_j] = PieceNames.EMPTY
                        self.board[pos_i + 1][pos_j + 1] = PieceNames.EMPTY
                    case Directions.DOWN:
                        self.board[pos_i + 1][pos_j] = PieceNames.BIG_BLOCK
                        self.board[pos_i + 1][pos_j + 1] = PieceNames.TAIL
                        self.board[pos_i + 2][pos_j] = PieceNames.TAIL
                        self.board[pos_i + 2][pos_j + 1] = PieceNames.TAIL
                        self.board[pos_i][pos_j] = PieceNames.EMPTY
                        self.board[pos_i][pos_j + 1] = PieceNames.EMPTY
                    case Directions.LEFT:
                        self.board[pos_i][pos_j - 1] = PieceNames.BIG_BLOCK
                        self.board[pos_i][pos_j] = PieceNames.TAIL
                        self.board[pos_i + 1][pos_j - 1] = PieceNames.TAIL
                        self.board[pos_i + 1][pos_j] = PieceNames.TAIL
                        self.board[pos_i][pos_j + 1] = PieceNames.EMPTY
                        self.board[pos_i + 1][pos_j + 1] = PieceNames.EMPTY
                    case Directions.RIGHT:
                        self.board[pos_i][pos_j + 1] = PieceNames.BIG_BLOCK
                        self.board[pos_i][pos_j + 2] = PieceNames.TAIL
                        self.board[pos_i + 1][pos_j + 1] = PieceNames.TAIL
                        self.board[pos_i + 1][pos_j + 2] = PieceNames.TAIL
                        self.board[pos_i][pos_j] = PieceNames.EMPTY
                        self.board[pos_i + 1][pos_j] = PieceNames.EMPTY

    def hash(self):
        board_hash = 0
        for i in range(1, 6):
            for j in range(1, 5):
                if self.board[i][j] != PieceNames.TAIL and self.board[i][j] != PieceNames.EMPTY:
                    part = self.indexer(self.board[i][j])
                    board_hash ^= zobrist_hash_table[i][j][part]
        return board_hash

    @staticmethod
    def indexer(part):
        match part:
            case PieceNames.HORI_2:
                return 0
            case PieceNames.VERT_2:
                return 1
            case PieceNames.SINGL:
                return 2
            case PieceNames.BIG_BLOCK:
                return 3

    def update_hash(self, board_hash, piece, position, direction):
        piece_index = self.indexer(piece)
        old_i, old_j = position
        new_hash = board_hash ^ zobrist_hash_table[old_i][old_j][piece_index]
        match direction:
            case 'UP':
                posi_i = -1
                posi_j = 0
            case 'DOWN':
                posi_i = 1
                posi_j = 0
            case 'LEFT':
                posi_i = 0
                posi_j = -1
            case 'RIGHT':
                posi_i = 0
                posi_j = 1
            case _:
                posi_i = 0
                posi_j = 0
        old_i += posi_i
        old_j += posi_j
        final_hash = new_hash ^ zobrist_hash_table[old_i][old_j][piece_index]
        return final_hash

    def hash_mirror(self, board_hash):
        for i in range(1, 6):
            for j in range(1, 5):
                piece = self.board[i][j]
                part = self.indexer(self.board[i][j])
                if piece == PieceNames.BIG_BLOCK or piece == PieceNames.VERT_2:
                    if j == 1:
                        board_hash ^= zobrist_hash_table[i][j][part]
                        board_hash ^= zobrist_hash_table[i][j + 2][part]
                    if j == 3:
                        board_hash ^= zobrist_hash_table[i][j][part]
                        board_hash ^= zobrist_hash_table[i][j - 2][part]
                elif piece == PieceNames.HORI_2 or piece == PieceNames.SINGL:
                    if j == 1:
                        board_hash ^= zobrist_hash_table[i][j][part]
                        board_hash ^= zobrist_hash_table[i][j + 3][part]
                    elif j == 2:
                        board_hash ^= zobrist_hash_table[i][j][part]
                        board_hash ^= zobrist_hash_table[i][j + 1][part]
                    elif j == 3:
                        board_hash ^= zobrist_hash_table[i][j][part]
                        board_hash ^= zobrist_hash_table[i][j - 1][part]
                    else:
                        board_hash ^= zobrist_hash_table[i][j][part]
                        board_hash ^= zobrist_hash_table[i][j - 3][part]
        return board_hash
