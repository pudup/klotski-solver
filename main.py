from solver_files.Board import Board
from solver_files.Solver import *
import sys
import time
import json

sys.setrecursionlimit(5000)

def main():
    print("Calculating solutions...")
    with open("boards/default.json", 'r') as f:
        board_grid = json.load(f)
    board = Board(board_grid)
    start = time.time()
    path = find_all_bfs(board)
    end = time.time()
    print(str(end - start) + " seconds")

    print("Number of unique solutions = " + str(path[1]))
    print("Minimum number of moves = " + str(path[2]))
    print("Maximum number of moves without repeating = " + str(path[3]))
    print(f"Shortest solution is -> {path[4]}")
    print("a is a long vertical block\n"
          "b is a long horizontal block\n"
          "c is a single blocks\n"
          "d is the goal block\n"
          "Co-ordinates are the top left part of the block (Y,X)")

if __name__ == '__main__':
    main()