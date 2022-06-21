import pygame
import time
from colors import colors
from pacman import pacman
from board import board

CELL_SIZE = 20
DELAY = 150
pygame.init()
screen = pygame.display.set_mode((CELL_SIZE*40, CELL_SIZE*30), depth=32)
board = board.Board(CELL_SIZE)
col = colors.Colors()
pacman = pacman.Pacman(radios=CELL_SIZE//2)
clock = pygame.time.Clock()

while True:
    # Regras
    pacman.move(screen)
    pacman.open_mouth = time.time() % 0.2 < 0.1

    # Pinta
    screen.fill(col.black)
    board.draw(screen)
    pacman.draw(screen)
    pygame.display.update()

    loop_time = clock.tick()
    if loop_time < DELAY:
        pygame.time.delay(DELAY-loop_time)

    # Eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
        elif e.type == pygame.KEYDOWN:
            dict_directions = {'97': 'L', '276': 'L', '119': 'U', '273': 'U', '100': 'R', '275': 'R', '115': 'D', '274':'D'}
            if str(e.key) in dict_directions.keys():
                pacman.set_direction(dict_directions[str(e.key)])
