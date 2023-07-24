from pygame_files import Background
from pygame_files.Blocks import Block

positions = [
    [0, 0, 0, 0, 0, 0],  # Padding
    [0, (128, 128), (192, 128), (256, 128), (320, 128), 0],
    [0, (128, 192), (192, 192), (256, 192), (320, 192), 0],
    [0, (128, 256), (192, 256), (256, 256), (320, 256), 0],
    [0, (128, 320), (192, 320), (256, 320), (320, 320), 0],
    [0, (128, 384), (192, 384), (256, 384), (320, 384), 0],
    [0, 0, 0, 0, 0, 0],  # Also Padding
]


class Animator:
    def __init__(self, surface, grid):
        self.surface = surface
        self.blocks = create_blocks(grid)
        Background.draw(self.surface)
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
