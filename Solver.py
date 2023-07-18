from Board import Board
import copy
import os
from time import sleep
from collections import deque


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


def solve_recursive(Board):
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
            if solve_recursive(Board):
                return True
        Board.set_position(board_memo)
        # sleep(0.005)
        # os.system('cls' if os.name == 'nt' else 'clear')
        # pretty_matrix(Board.board)
    return False


def solve_BFS(Board):
    Board = Board
    queue = deque()
    curr_board = copy.deepcopy(Board.board)
    queue.append([curr_board, []])
    Board.hashes.append(Board.hash())
    while queue:
        curr_board_and_moves_taken = queue.popleft()
        curr_board = copy.deepcopy(curr_board_and_moves_taken[0])
        moves_taken = copy.deepcopy(curr_board_and_moves_taken[1])
        Board.set_position(curr_board)
        moves = Board.get_possible_moves()
        while moves:
            next_move = moves.pop()
            for move in next_move[2]:
                Board.move_piece(piece_name=next_move[0], piece_coord=next_move[1], direction=move)
                if Board.board[4][2] == 'd':
                    curr_board_and_moves_taken[1].append([next_move[0], next_move[1], move])
                    count = 1
                    for path in curr_board_and_moves_taken[1]:
                        print(str(count) + ". " + str(path))
                        count += 1
                    print(str(len(curr_board_and_moves_taken[1])) + " moves")
                    return
                new_hash = Board.hash()
                if new_hash not in Board.hashes:
                    Board.hashes.append(new_hash)
                    new_board_posi = copy.deepcopy(Board.board)
                    moves_taken_new = copy.deepcopy(moves_taken)
                    moves_taken_new.append([next_move[0], next_move[1], move])
                    queue.append([new_board_posi, moves_taken_new])
                    Board.set_position(curr_board)
                else:
                    Board.set_position(curr_board)
