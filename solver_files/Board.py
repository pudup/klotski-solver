import copy


class Board:
    def __init__(self, grid):
        self.board = []
        self.hashes = []

        self.set_board(grid)
        self.moves = self.get_possible_moves()

    def set_position(self, new):
        self.board = copy.deepcopy(new)

    def set_board(self, grid):
        self.set_position(grid)

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
                        can_move = True
                    # Down Check
                    if self.board[pos_i + 2][pos_j] == 'O':
                        piece[2].append("DOWN")
                        can_move = True
                    # Left Check
                    if self.board[pos_i][pos_j - 1] == 'O' and self.board[pos_i + 1][pos_j - 1] == 'O':
                        piece[2].append("LEFT")
                        can_move = True
                    # Right Check
                    if self.board[pos_i][pos_j + 1] == 'O' and self.board[pos_i + 1][pos_j + 1] == 'O':
                        piece[2].append("RIGHT")
                        can_move = True
                case 'b':
                    # Up Check
                    if self.board[pos_i - 1][pos_j] == 'O' and self.board[pos_i - 1][pos_j + 1] == 'O':
                        piece[2].append("UP")
                        can_move = True
                    # Down Check
                    if self.board[pos_i + 1][pos_j] == 'O' and self.board[pos_i + 1][pos_j + 1] == 'O':
                        piece[2].append("DOWN")
                        can_move = True
                    # Left Check
                    if self.board[pos_i][pos_j - 1] == 'O':
                        piece[2].append("LEFT")
                        can_move = True
                    # Right Check
                    if self.board[pos_i][pos_j + 2] == 'O':
                        piece[2].append("RIGHT")
                        can_move = True
                case 'c':
                    # Up Check
                    if self.board[pos_i - 1][pos_j] == 'O':
                        piece[2].append("UP")
                        can_move = True
                    # Down Check
                    if self.board[pos_i + 1][pos_j] == 'O':
                        piece[2].append("DOWN")
                        can_move = True
                    # Left Check
                    if self.board[pos_i][pos_j - 1] == 'O':
                        piece[2].append("LEFT")
                        can_move = True
                    # Right Check
                    if self.board[pos_i][pos_j + 1] == 'O':
                        piece[2].append("RIGHT")
                        can_move = True
                case 'd':
                    # Up Check
                    if self.board[pos_i - 1][pos_j] == 'O' and self.board[pos_i - 1][pos_j + 1] == 'O':
                        piece[2].append("UP")
                        can_move = True
                    # Down Check
                    if self.board[pos_i + 2][pos_j] == 'O' and self.board[pos_i + 2][pos_j + 1] == 'O':
                        piece[2].append("DOWN")
                        can_move = True
                    # Left Check
                    if self.board[pos_i][pos_j - 1] == 'O' and self.board[pos_i + 1][pos_j - 1] == 'O':
                        piece[2].append("LEFT")
                        can_move = True
                    # Right Check
                    if self.board[pos_i][pos_j + 2] == 'O' and self.board[pos_i + 1][pos_j + 2] == 'O':
                        piece[2].append("RIGHT")
                        can_move = True

            if can_move:
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
        string = ""
        for i in range(1, 6):
            for j in range(1, 5):
                string += self.board[i][j]
        return string
