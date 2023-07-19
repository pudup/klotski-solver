from solver_files.Board import Board
from solver_files.Solver import *
import sys
import time

sys.setrecursionlimit(5000)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Calculating solutions...")
    board = Board()
    start = time.time()
    path = find_all_bfs(board)
    end = time.time()
    print(str(end - start) + " seconds")

    print("Number of unique solutions = " + str(path[1]))
    print("Minimum number of moves = " + str(path[2]))
    print("Maximum number of moves without repeating = " + str(path[3]))
    print(f"Shortest solution is -> {path[4]}")
    print("a is a long vertical block\n"
          "b blocks is a long horizontal block\n"
          "c is a single blocks\n"
          "d is the goal block\n"
          "Co-ordinates are the top left part of the block (Y,X)")