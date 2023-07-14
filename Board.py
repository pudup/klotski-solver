import copy


class Board():
    def __init__(self):
        self.board = [
            ['0', '0', '0', '0', '0', '0'],
            ['0', 'a', 'd', 'x', 'a', '0'],
            ['0', 'x', 'x', 'x', 'x', '0'],
            ['0', 'a', 'b', 'x', 'a', '0'],
            ['0', 'x', 'c', 'c', 'x', '0'],
            ['0', 'c', 'O', 'O', 'c', '0'],
            ['0', '0', '0', '0', '0', '0'],
        ]

        self.hashes = []

        self.moves = self.get_possible_moves()

    def set_position(self, new):
        self.board = copy.deepcopy(new)

    def get_piece_positions(self):

        pieces = []
        piece_names = ['a', 'b', 'c', 'd']

        for i in range(7):
            for j in range(6):
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

            if it == 'a':
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

            elif it == 'b':
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

            elif it == 'c':
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

            elif it == 'd':
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

        if it == 'a':
            # Up Move
            if direction == "UP":
                self.board[pos_i - 1][pos_j] = 'a'
                self.board[pos_i][pos_j] = 'x'
                self.board[pos_i + 1][pos_j] = 'O'

            # Down Move
            if direction == "DOWN":
                self.board[pos_i + 1][pos_j] = 'a'
                self.board[pos_i + 2][pos_j] = 'x'
                self.board[pos_i][pos_j] = 'O'

            # Left Move
            if direction == "LEFT":
                self.board[pos_i][pos_j - 1] = 'a'
                self.board[pos_i + 1][pos_j - 1] = 'x'
                self.board[pos_i][pos_j] = 'O'
                self.board[pos_i + 1][pos_j] = 'O'

            # Right Move
            if direction == "RIGHT":
                self.board[pos_i][pos_j + 1] = 'a'
                self.board[pos_i + 1][pos_j + 1] = 'x'
                self.board[pos_i][pos_j] = 'O'
                self.board[pos_i + 1][pos_j] = 'O'

        if it == 'b':
            # Up Move
            if direction == "UP":
                self.board[pos_i - 1][pos_j] = 'b'
                self.board[pos_i - 1][pos_j + 1] = 'x'
                self.board[pos_i][pos_j] = 'O'
                self.board[pos_i][pos_j + 1] = 'O'

            # Down Move
            if direction == "DOWN":
                self.board[pos_i + 1][pos_j] = 'b'
                self.board[pos_i + 1][pos_j + 1] = 'x'
                self.board[pos_i][pos_j] = 'O'
                self.board[pos_i][pos_j + 1] = 'O'

            # Left Move
            if direction == "LEFT":
                self.board[pos_i][pos_j - 1] = 'b'
                self.board[pos_i][pos_j] = 'x'
                self.board[pos_i][pos_j + 1] = 'O'

            # Right Move
            if direction == "RIGHT":
                self.board[pos_i][pos_j + 1] = 'b'
                self.board[pos_i][pos_j + 2] = 'x'
                self.board[pos_i][pos_j] = 'O'
        #
        if it == 'c':
            # Up Move
            if direction == "UP":
                self.board[pos_i - 1][pos_j] = 'c'
                self.board[pos_i][pos_j] = 'O'

            # Down Move
            if direction == "DOWN":
                self.board[pos_i + 1][pos_j] = 'c'
                self.board[pos_i][pos_j] = 'O'

            # Left Move
            if direction == "LEFT":
                self.board[pos_i][pos_j - 1] = 'c'
                self.board[pos_i][pos_j] = 'O'

            # Right Move
            if direction == "RIGHT":
                self.board[pos_i][pos_j + 1] = 'c'
                self.board[pos_i][pos_j] = 'O'

        if it == 'd':
            # Up Move
            if direction == "UP":
                self.board[pos_i - 1][pos_j] = 'd'
                self.board[pos_i - 1][pos_j + 1] = 'x'
                self.board[pos_i][pos_j] = 'x'
                self.board[pos_i][pos_j + 1] = 'x'
                self.board[pos_i + 1][pos_j] = 'O'
                self.board[pos_i + 1][pos_j + 1] = 'O'

            # Down Move
            if direction == "DOWN":
                self.board[pos_i + 1][pos_j] = 'd'
                self.board[pos_i + 1][pos_j + 1] = 'x'
                self.board[pos_i + 2][pos_j] = 'x'
                self.board[pos_i + 2][pos_j + 1] = 'x'
                self.board[pos_i][pos_j] = 'O'
                self.board[pos_i][pos_j + 1] = 'O'

            # Left Move
            if direction == "LEFT":
                self.board[pos_i][pos_j - 1] = 'd'
                self.board[pos_i][pos_j] = 'x'
                self.board[pos_i + 1][pos_j - 1] = 'x'
                self.board[pos_i + 1][pos_j] = 'x'
                self.board[pos_i][pos_j + 1] = 'O'
                self.board[pos_i + 1][pos_j + 1] = 'O'

            # Right Move
            if direction == "RIGHT":
                self.board[pos_i][pos_j + 1] = 'd'
                self.board[pos_i][pos_j + 2] = 'x'
                self.board[pos_i + 1][pos_j + 1] = 'x'
                self.board[pos_i + 1][pos_j + 2] = 'x'
                self.board[pos_i][pos_j] = 'O'
                self.board[pos_i + 1][pos_j] = 'O'

    def hash(self):
        string = ""
        for i in range(7):
            for j in range(6):
                if self.board[i][j] != "0":
                    string += self.board[i][j]
        return string
