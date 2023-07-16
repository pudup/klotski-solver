from Board import Board
import copy
import os
from time import sleep

new_board = Board()


def pretty_matrix(array):
    print("_______________")
    for row in array:
        line = "| "
        for item in row:
            line += item
            line += " "
        line += "|"
        print(line)
    print("---------------")


def solve(Board):
    if Board.board[4][2] == 'd':
        pretty_matrix(Board.board)
        print(str(len(Board.hashes)) + " moves")
        return True
    new_hash = Board.hash()
    if new_hash not in Board.hashes:
        Board.hashes.append(new_hash)
    else:
        return False
    board_memo = copy.deepcopy(Board.board)

    moves = Board.get_possible_moves()
    while moves:
        next_move = moves.pop()
        for move in next_move[2]:
            Board.move_piece(piece_name=next_move[0], piece_coord=next_move[1], direction=move)
            new_hash = Board.hash()
            if new_hash in Board.hashes:
                Board.set_position(board_memo)
                continue
            if solve(Board):
                return True
        Board.set_position(board_memo)
        # sleep(0.005)
        # os.system('cls' if os.name == 'nt' else 'clear')
        # pretty_matrix(Board.board)
    return False
