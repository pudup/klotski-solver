import copy
import random

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
        piece_names = ['a', 'b', 'c', 'd']

        for i in range(1, 6):
            for j in range(1, 5):
                if self.board[i][j] in piece_names:
                    pieces.append([self.board[i][j], (i, j)])

        return pieces

    def get_possible_moves(self):
        pieces = self.get_piece_positions()
        piece_moves = []

        for piece in pieces:
            can_move = False
            it = piece[0]
            pos_i, pos_j = piece[1]
            piece.append([])

            match it:
                case 'a':
                    # Up Check
                    if self.board[pos_i - 1][pos_j] == 'O':
                        piece[2].append("UP")
                    # Down Check
                    if self.board[pos_i + 2][pos_j] == 'O':
                        piece[2].append("DOWN")
                    # Left Check
                    if self.board[pos_i][pos_j - 1] == 'O' and self.board[pos_i + 1][pos_j - 1] == 'O':
                        piece[2].append("LEFT")
                    # Right Check
                    if self.board[pos_i][pos_j + 1] == 'O' and self.board[pos_i + 1][pos_j + 1] == 'O':
                        piece[2].append("RIGHT")
                case 'b':
                    # Up Check
                    if self.board[pos_i - 1][pos_j] == 'O' and self.board[pos_i - 1][pos_j + 1] == 'O':
                        piece[2].append("UP")
                    # Down Check
                    if self.board[pos_i + 1][pos_j] == 'O' and self.board[pos_i + 1][pos_j + 1] == 'O':
                        piece[2].append("DOWN")
                    # Left Check
                    if self.board[pos_i][pos_j - 1] == 'O':
                        piece[2].append("LEFT")
                    # Right Check
                    if self.board[pos_i][pos_j + 2] == 'O':
                        piece[2].append("RIGHT")
                case 'c':
                    # Up Check
                    if self.board[pos_i - 1][pos_j] == 'O':
                        piece[2].append("UP")
                    # Down Check
                    if self.board[pos_i + 1][pos_j] == 'O':
                        piece[2].append("DOWN")
                    # Left Check
                    if self.board[pos_i][pos_j - 1] == 'O':
                        piece[2].append("LEFT")
                    # Right Check
                    if self.board[pos_i][pos_j + 1] == 'O':
                        piece[2].append("RIGHT")
                case 'd':
                    # Up Check
                    if self.board[pos_i - 1][pos_j] == 'O' and self.board[pos_i - 1][pos_j + 1] == 'O':
                        piece[2].append("UP")
                    # Down Check
                    if self.board[pos_i + 2][pos_j] == 'O' and self.board[pos_i + 2][pos_j + 1] == 'O':
                        piece[2].append("DOWN")
                    # Left Check
                    if self.board[pos_i][pos_j - 1] == 'O' and self.board[pos_i + 1][pos_j - 1] == 'O':
                        piece[2].append("LEFT")
                    # Right Check
                    if self.board[pos_i][pos_j + 2] == 'O' and self.board[pos_i + 1][pos_j + 2] == 'O':
                        piece[2].append("RIGHT")

            if piece[2]:
                piece_moves.append(piece)

        return piece_moves

    def move_piece(self, piece_name, piece_coord, direction):
        it = piece_name
        pos_i, pos_j = piece_coord

        match it:
            case 'a':
                match direction:
                    case "UP":
                        self.board[pos_i - 1][pos_j] = 'a'
                        self.board[pos_i][pos_j] = 'x'
                        self.board[pos_i + 1][pos_j] = 'O'
                    case "DOWN":
                        self.board[pos_i + 1][pos_j] = 'a'
                        self.board[pos_i + 2][pos_j] = 'x'
                        self.board[pos_i][pos_j] = 'O'
                    case "LEFT":
                        self.board[pos_i][pos_j - 1] = 'a'
                        self.board[pos_i + 1][pos_j - 1] = 'x'
                        self.board[pos_i][pos_j] = 'O'
                        self.board[pos_i + 1][pos_j] = 'O'
                    case "RIGHT":
                        self.board[pos_i][pos_j + 1] = 'a'
                        self.board[pos_i + 1][pos_j + 1] = 'x'
                        self.board[pos_i][pos_j] = 'O'
                        self.board[pos_i + 1][pos_j] = 'O'
            case 'b':
                match direction:
                    case "UP":
                        self.board[pos_i - 1][pos_j] = 'b'
                        self.board[pos_i - 1][pos_j + 1] = 'x'
                        self.board[pos_i][pos_j] = 'O'
                        self.board[pos_i][pos_j + 1] = 'O'
                    case "DOWN":
                        self.board[pos_i + 1][pos_j] = 'b'
                        self.board[pos_i + 1][pos_j + 1] = 'x'
                        self.board[pos_i][pos_j] = 'O'
                        self.board[pos_i][pos_j + 1] = 'O'
                    case "LEFT":
                        self.board[pos_i][pos_j - 1] = 'b'
                        self.board[pos_i][pos_j] = 'x'
                        self.board[pos_i][pos_j + 1] = 'O'
                    case "RIGHT":
                        self.board[pos_i][pos_j + 1] = 'b'
                        self.board[pos_i][pos_j + 2] = 'x'
                        self.board[pos_i][pos_j] = 'O'
            case 'c':
                match direction:
                    case "UP":
                        self.board[pos_i - 1][pos_j] = 'c'
                        self.board[pos_i][pos_j] = 'O'
                    case "DOWN":
                        self.board[pos_i + 1][pos_j] = 'c'
                        self.board[pos_i][pos_j] = 'O'
                    case "LEFT":
                        self.board[pos_i][pos_j - 1] = 'c'
                        self.board[pos_i][pos_j] = 'O'
                    case "RIGHT":
                        self.board[pos_i][pos_j + 1] = 'c'
                        self.board[pos_i][pos_j] = 'O'
            case 'd':
                match direction:
                    case "UP":
                        self.board[pos_i - 1][pos_j] = 'd'
                        self.board[pos_i - 1][pos_j + 1] = 'x'
                        self.board[pos_i][pos_j] = 'x'
                        self.board[pos_i][pos_j + 1] = 'x'
                        self.board[pos_i + 1][pos_j] = 'O'
                        self.board[pos_i + 1][pos_j + 1] = 'O'
                    case "DOWN":
                        self.board[pos_i + 1][pos_j] = 'd'
                        self.board[pos_i + 1][pos_j + 1] = 'x'
                        self.board[pos_i + 2][pos_j] = 'x'
                        self.board[pos_i + 2][pos_j + 1] = 'x'
                        self.board[pos_i][pos_j] = 'O'
                        self.board[pos_i][pos_j + 1] = 'O'
                    case "LEFT":
                        self.board[pos_i][pos_j - 1] = 'd'
                        self.board[pos_i][pos_j] = 'x'
                        self.board[pos_i + 1][pos_j - 1] = 'x'
                        self.board[pos_i + 1][pos_j] = 'x'
                        self.board[pos_i][pos_j + 1] = 'O'
                        self.board[pos_i + 1][pos_j + 1] = 'O'
                    case "RIGHT":
                        self.board[pos_i][pos_j + 1] = 'd'
                        self.board[pos_i][pos_j + 2] = 'x'
                        self.board[pos_i + 1][pos_j + 1] = 'x'
                        self.board[pos_i + 1][pos_j + 2] = 'x'
                        self.board[pos_i][pos_j] = 'O'
                        self.board[pos_i + 1][pos_j] = 'O'

    def hash(self):
        board_hash = 0
        for i in range(1, 6):
            for j in range(1, 5):
                if self.board[i][j] != 'x' and self.board[i][j] != 'O':
                    part = self.indexer(self.board[i][j])
                    board_hash ^= zobrist_hash_table[i][j][part]
        return board_hash

    @staticmethod
    def indexer(part):
        match part:
            case 'a':
                return 0
            case 'b':
                return 1
            case 'c':
                return 2
            case 'd':
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
                if piece == 'd' or piece == 'b':
                    if j == 1:
                        board_hash ^= zobrist_hash_table[i][j][part]
                        board_hash ^= zobrist_hash_table[i][j + 2][part]
                    if j == 3:
                        board_hash ^= zobrist_hash_table[i][j][part]
                        board_hash ^= zobrist_hash_table[i][j - 2][part]
                elif piece == 'a' or piece == 'c':
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
