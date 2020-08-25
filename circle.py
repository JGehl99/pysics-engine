import pygame as pg


class Circle:
    black = (0, 0, 0)

    # (surface, color, center, radius)
    def __init__(self, surface, color=black, center=(0, 0), radius=5):
        self.surface = surface
        self.color = color
        self.center = center
        self.radius = radius
        self.xVel = 0
        self.yVel = 0
        self.xAcc = 0
        self.yAcc = 1

    def drawCircle(self):
        pg.draw.circle(self.surface, self.color, self.center, self.radius)

    def updateSpeed(self):
        self.yVel += self.yAcc
        self.center = (self.center[0], self.center[1] + self.yVel)
