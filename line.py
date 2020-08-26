import pygame


class Line:
    # constructor
    def __init__(self, surface, color=(0, 0, 0), x1y1=(0, 0), x2y2=(0, 0), width=2):
        self.surface = surface
        self.x1y1 = x1y1
        self.x2y2 = x2y2
        self.color = color
        self.width = width

    # draws line from self values
    def draw(self):
        pygame.draw.line(self.surface, self.color, self.x1y1, self.x2y2, self.width)
