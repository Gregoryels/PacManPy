import pygame
import time
from colors import colors
from pacman import pacman

pygame.init()
screen = pygame.display.set_mode((800, 600), depth=32)
col = colors.Colors()
pacman = pacman.Pacman(screen, radios=20)
vel_x = 0.2
vel_y = 0.3
while True:
    # Regras

    if pacman.x_center+pacman.radios >= screen.get_width():
        vel_x *= -1
        pacman.direction = 'L'
    elif pacman.x_center-pacman.radios <= 0:
        vel_x *= -1
        pacman.direction = 'R'
    if pacman.y_center+pacman.radios >= screen.get_height():
        vel_y *= -1
        pacman.direction = 'U'
    elif pacman.y_center-pacman.radios <= 0:
        vel_y *= -1
        pacman.direction = 'D'

    pacman.x_center += vel_x
    pacman.y_center += vel_y

    # Abre e fecha a boca a cada 0.1 s
    pacman.open_mouth = time.time() % 0.2 < 0.1

    # Pinta
    screen.fill(col.black)
    pacman.draw(screen)
    pygame.display.update()

    # Eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()