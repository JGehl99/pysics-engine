import pygame as pg
import numpy as np


class Circle:
    black = (0, 0, 0)

    # (surface, color, center, radius)
    def __init__(self, surface, color=black, center=[0, 0], radius=10, xVel=0, yVel=0, xAcc=0, yAcc=1):
        self.surface = surface
        self.color = color
        self.center = list(center)
        self.radius = radius
        self.vel = np.array([xVel, yVel], int)
        self.acc = np.array([xAcc, yAcc], int)

    def drawCircle(self):
        pg.draw.circle(self.surface, self.color, tuple(self.center), self.radius)

    def updateX(self):
        self.center[0] += self.vel[0]
        self.vel[0] += self.acc[0]

    def updateY(self):
        self.center[1] += self.vel[1]
        self.vel[1] += self.acc[1]


