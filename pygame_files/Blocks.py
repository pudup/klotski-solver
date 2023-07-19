import pygame
from pygame_files import Background

positions = [
    [0, 0, 0, 0, 0, 0], # Padding
    [0, (128, 128), (192, 128), (256, 128), (320, 128), 0],
    [0, (128, 192), (192, 192), (256, 192), (320, 192), 0],
    [0, (128, 256), (192, 256), (256, 256), (320, 256), 0],
    [0, (128, 320), (192, 320), (256, 320), (320, 320), 0],
    [0, (128, 384), (192, 384), (256, 384), (320, 384), 0],
]

original_board = [
    ['0', '0', '0', '0', '0', '0'],
    ['0', 'a', 'd', 'x', 'a', '0'],
    ['0', 'x', 'x', 'x', 'x', '0'],
    ['0', 'a', 'b', 'x', 'a', '0'],
    ['0', 'x', 'c', 'c', 'x', '0'],
    ['0', 'c', 'O', 'O', 'c', '0'],
    ['0', '0', '0', '0', '0', '0'],
]


class Block(pygame.sprite.Sprite):
    def __init__(self, name, num=0, posi_i=0, posi_j=0):
        super().__init__()
        self.posi_i = posi_i
        self.posi_j = posi_j
        self.num = num
        match name:
            case "goal":
                self.block = pygame.image.load("assets/blocks/goal.gif")
            case "vert":
                self.block = pygame.image.load("assets/blocks/vert.gif")
            case "hori":
                self.block = pygame.image.load("assets/blocks/hori.gif")
            case "sing":
                self.block = pygame.image.load("assets/blocks/sing.gif")
            case _:
                self.block = None
                self.num = None

        self.rect = self.block.get_rect()

    def draw(self, surface, position):
        surface.blit(self.block, position)


class Mover:
    def __init__(self, surface):
        self.surface = surface
        self.blocks = create_blocks(original_board)
        self.starting_position()

    def starting_position(self):
        for block in self.blocks:
            block.draw(self.surface, positions[block.posi_i][block.posi_j])

    def move(self, current_position, destination_position):
        Background.draw(self.surface)
        for block in self.blocks:
            if block.posi_i == current_position[0] and block.posi_j == current_position[1]:
                block.posi_i = destination_position[0]
                block.posi_j = destination_position[1]
        for block in self.blocks:
            block.draw(self.surface, positions[block.posi_i][block.posi_j])


def create_blocks(grid):
    blocks = []
    for i in range(1, 6):
        for j in range(1, 5):
            match grid[i][j]:
                case 'a':
                    block = Block(name="vert", posi_i=i, posi_j=j)
                    blocks.append(block)
                case 'b':
                    block = Block(name="hori", posi_i=i, posi_j=j)
                    blocks.append(block)
                case 'c':
                    block = Block(name="sing", posi_i=i, posi_j=j)
                    blocks.append(block)
                case 'd':
                    block = Block(name="goal", posi_i=i, posi_j=j)
                    blocks.append(block)

    return blocks
