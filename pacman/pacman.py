from colors import colors
import pygame

class Pacman:
    def __init__(self, screen, radios):
        self.x_center = int(0.2*screen.get_width())
        self.y_center = int(0.8*screen.get_height())
        self.radios = radios
        self.color = colors.Colors().yellow

        self.x_velocity = 0
        self.y_velocity = 0
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
