import pygame
import sys
import json
from pygame_files import Animator
from solver_files.Board import Board
from solver_files.Solver import solve_bfs
from pygame_files.AnimateSolution import animate_solution


def main():
    with open("boards/default.json", 'r') as f:
        board_grid = json.load(f)
    board = Board(board_grid)

    pygame.init()
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Verdana", 32)
    solving_text = font.render('Solving...', True, (44, 54, 57))

    done = False

    surface = pygame.display.set_mode((512, 512 + 64))
    pygame.display.set_caption("Klotski Solver")
    mover = Animator.Animator(surface, board_grid)
    surface.blit(solving_text, ((256 + 128) / 2, 64 + 32 / 2))

    pygame.display.update()
    path = solve_bfs(board)

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
