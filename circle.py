import pygame as pg
import numpy as np

# tuple for the color black
black = (0, 0, 0)


class Circle:

    # constructor
    def __init__(self, surface, color=black, center=[0, 0], radius=10, xVel=0, yVel=0, xAcc=0, yAcc=1):
        self.surface = surface
        self.color = color
        self.center = list(center)
        self.radius = radius
        self.vel = np.array([xVel, yVel], int)
        self.acc = np.array([xAcc, yAcc], int)

    # draws circle based on self values
    def drawCircle(self):
        pg.draw.circle(self.surface, self.color, tuple(self.center), self.radius)

    # updates x location based on x velocity and updates x velocity based on x acceleration
    def updateX(self):
        self.center[0] += self.vel[0]
        self.vel[0] += self.acc[0]

    # updates y location based on y velocity and updates y velocity based on y acceleration
    def updateY(self):
        self.center[1] += self.vel[1]
        self.vel[1] += self.acc[1]
