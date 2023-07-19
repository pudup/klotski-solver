import pygame
import sys
from pygame_files import Blocks
from Board import Board
from Solver import solve_bfs
from pygame_files.AnimateSolution import animate_solution, clean_path

THIN_LINES_COL = (255, 161, 201)


def main():
    board = Board()
    path = clean_path(solve_bfs(board))

    pygame.init()
    clock = pygame.time.Clock()
    done = False

    surface = pygame.display.set_mode((512, 512 + 64))
    pygame.display.set_caption("Klotski Solver")
    mover = Blocks.Mover(surface)

    while True:
        pygame.display.update()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if not done:
            done = True
            animate_solution(mover, path)


if __name__ == "__main__":
    main()
