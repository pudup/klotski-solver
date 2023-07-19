import pygame
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
