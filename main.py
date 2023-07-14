from Board import Board


def pretty_matrix(array):
    for row in array:
        line = ""
        for item in row:
            line += item
            line += " "
        print(line)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    board = Board()
    print(board.get_possible_moves())


