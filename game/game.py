import pygame
import time
from colors import colors
from pacman import pacman

pygame.init()
screen = pygame.display.set_mode((800, 600), depth=32)
col = colors.Colors()
pacman = pacman.Pacman(screen, radios=20)

while True:
    # Regras

    pacman.move(screen)
    pacman.open_mouth = time.time() % 0.2 < 0.1

    # Pinta
    screen.fill(col.black)
    pacman.draw(screen)
    pygame.display.update()

    # Eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
        elif e.type == pygame.KEYDOWN:
            dict_directions = {'97': 'L', '276': 'L', '119': 'U', '273': 'U', '100': 'R', '275': 'R', '115': 'D', '274': 'D'}
            if str(e.key) in dict_directions.keys():
                pacman.set_direction(dict_directions[str(e.key)])
            print(e)
