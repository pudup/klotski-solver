from Board import Board
from Solver import solve
import sys

sys.setrecursionlimit(20000)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    board = Board()
    solve(board)
