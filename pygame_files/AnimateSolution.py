import pygame
from time import sleep
import sys

def animate_solution(mover, path):
    for move in path:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        posi_i = 0
        posi_j = 0
        match move[2]:
            case 'UP':
                posi_i = -1
                posi_j = 0
            case 'DOWN':
                posi_i = 1
                posi_j = 0
            case 'LEFT':
                posi_i = 0
                posi_j = -1
            case 'RIGHT':
                posi_i = 0
                posi_j = 1
        direction_i, direction_j = move[1][0] + posi_i, move[1][1] + posi_j
        mover.move(move[1], (direction_i, direction_j))
        pygame.display.update()
        sleep(0.25)
