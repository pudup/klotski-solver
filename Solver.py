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


def solve_recursive(klotski_board):
    if klotski_board.board[4][2] == 'd':
        pretty_matrix(klotski_board.board)
        print(str(len(klotski_board.hashes)) + " moves")
        return True
    new_hash = klotski_board.hash()
    if new_hash not in klotski_board.hashes:
        klotski_board.hashes.append(new_hash)
    else:
        return False
    board_memo = copy.deepcopy(klotski_board.board)

    moves = klotski_board.get_possible_moves()
    while moves:
        next_move = moves.pop()
        for move in next_move[2]:
            klotski_board.move_piece(piece_name=next_move[0], piece_coord=next_move[1], direction=move)
            new_hash = klotski_board.hash()
            if new_hash in klotski_board.hashes:
                klotski_board.set_position(board_memo)
                continue
            if solve_recursive(klotski_board):
                return True
        klotski_board.set_position(board_memo)
    return False


def solve_bfs(klotski_board):
    klotski_board = klotski_board
    queue = deque()
    curr_board = copy.deepcopy(klotski_board.board)
    queue.append([curr_board, []])
    klotski_board.hashes.append(klotski_board.hash())
    while queue:
        curr_board_and_moves_taken = queue.popleft()
        curr_board = copy.deepcopy(curr_board_and_moves_taken[0])
        moves_taken = copy.deepcopy(curr_board_and_moves_taken[1])
        klotski_board.set_position(curr_board)
        moves = klotski_board.get_possible_moves()
        while moves:
            next_move = moves.pop()
            for move in next_move[2]:
                klotski_board.move_piece(piece_name=next_move[0], piece_coord=next_move[1], direction=move)
                if klotski_board.board[4][2] == 'd':
                    curr_board_and_moves_taken[1].append([next_move[0], next_move[1], move])
                    count = 1
                    for path in curr_board_and_moves_taken[1]:
                        print(str(count) + ". " + str(path))
                        count += 1
                    print(str(len(curr_board_and_moves_taken[1])) + " moves")
                    return curr_board_and_moves_taken[1]
                new_hash = klotski_board.hash()
                if new_hash not in klotski_board.hashes:
                    klotski_board.hashes.append(new_hash)
                    new_board_position = copy.deepcopy(klotski_board.board)
                    moves_taken_new = copy.deepcopy(moves_taken)
                    moves_taken_new.append([next_move[0], next_move[1], move])
                    queue.append([new_board_position, moves_taken_new])
                    klotski_board.set_position(curr_board)
                else:
                    klotski_board.set_position(curr_board)


def view_solution(klotski_board, path):
    klotski_board = klotski_board
    for next_move in path:
        klotski_board.move_piece(piece_name=next_move[0], piece_coord=next_move[1], direction=next_move[2])
        sleep(0.25)
        os.system('cls' if os.name == 'nt' else 'clear')
        pretty_matrix(klotski_board.board)
