from colors import colors
import pygame

class Pacman:
    def __init__(self, radios):
        self.radios = radios
        self.cell_size = 2*radios
        self.x_center = self.cell_size + self.radios
        self.y_center = self.cell_size + self.radios

        self.color = colors.Colors().yellow

        self.x_vel = 0
        self.y_vel = 0
        self.direction = 'R'
        self.open_mouth = True


    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x_center), int(self.y_center)), self.radios, 0)

        if self.open_mouth:
            mouth_center = (int(self.x_center), int(self.y_center))
            if self.direction == 'R':
                mouth_corner_1 = (int(self.x_center + self.radios), int(self.y_center - self.radios))
                mouth_corner_2 = (int(self.x_center + self.radios), int(self.y_center + self.radios))
            elif self.direction == 'L':
                mouth_corner_1 = (int(self.x_center - self.radios), int(self.y_center - self.radios))
                mouth_corner_2 = (int(self.x_center - self.radios), int(self.y_center + self.radios))
            elif self.direction == 'U':
                mouth_corner_1 = (int(self.x_center + self.radios), int(self.y_center - self.radios))
                mouth_corner_2 = (int(self.x_center - self.radios), int(self.y_center - self.radios))
            else:
                mouth_corner_1 = (int(self.x_center + self.radios), int(self.y_center + self.radios))
                mouth_corner_2 = (int(self.x_center - self.radios), int(self.y_center + self.radios))
            mouth = [mouth_center, mouth_corner_1, mouth_corner_2]
            pygame.draw.polygon(screen, colors.Colors().black, mouth, 0)

    def move(self, screen):
        if self.x_center + self.radios >= screen.get_width():
            self.x_vel *= -1
            self.direction = 'L'
        elif self.x_center - self.radios <= 0:
            self.x_vel *= -1
            self.direction = 'R'

        if self.y_center + self.radios >= screen.get_height():
            self.y_vel *= -1
            self.direction = 'U'
        elif self.y_center - self.radios <= 0:
            self.y_vel *= -1
            self.direction = 'D'

        self.x_center += (self.x_vel*self.cell_size)
        self.y_center += (self.y_vel*self.cell_size)

    def set_direction(self, direction):
        dict_directions = {'L': (-1, 0), 'U': (0, -1), 'R': (1, 0), 'D': (0, 1)}
        self.direction = direction
        self.x_vel, self.y_vel = dict_directions[direction]
