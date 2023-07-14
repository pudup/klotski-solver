from Board import Board
from Solver import solve
import sys
import time

sys.setrecursionlimit(20000)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    board = Board()
    start = time.time()
    solve(board)
    end = time.time()
    print(str(end-start) + " seconds")