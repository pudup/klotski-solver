from Board import Board
from Solver import solve_recursive, solve_BFS
import sys
import time

sys.setrecursionlimit(5000)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("a blocks are long vertical\n"
          "b blocks are long horizontal\n"
          "c blocks are the single blocks\n"
          "d block is the goal block\n"
          "Co-ordinates are the top left part of the block (Y,X)")
    board = Board()
    start = time.time()
    solve_BFS(board)
    end = time.time()
    print(str(end-start) + " seconds")