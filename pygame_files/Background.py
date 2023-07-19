import pygame

THICC_LINES_COL = (44, 54, 57)
BACKGROUND_COL = (245, 245, 245)


def draw(surface):
    # Background
    surface.fill(BACKGROUND_COL)

    # Left
    pygame.draw.line(surface, THICC_LINES_COL, (124, 121), (124, 455), 8)

    # Top
    pygame.draw.line(surface, THICC_LINES_COL, (128, 124), (384, 124), 8)

    # Right
    pygame.draw.line(surface, THICC_LINES_COL, (387, 121), (387, 455), 8)

    # Bottom
    pygame.draw.line(surface, THICC_LINES_COL, (384, 451), (128, 451), 8)

    # Exit
    pygame.draw.line(surface, BACKGROUND_COL, (320, 451), (192, 451), 8)
