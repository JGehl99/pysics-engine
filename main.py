import pygame
import funclib as fn
from circle import Circle
from line import Line

window = [1000, 750]

energyLoss = 0.90

pygame.init()

gameDisplay = pygame.display.set_mode((window[0], window[1]))
pygame.display.set_caption("Gravity")
gameDisplay.fill((255, 255, 255))

clock = pygame.time.Clock()

circleList = []
pressFlag = False
clickLoc = (0, 0)
line = Line(gameDisplay, (0, 0, 0), (0, 0), (0, 0), 2)

crashed = False

"""
Hold right click down
    Draw line from click point to mouse
    Calculate horizontal and vertical velocity from the angle of the drawn line and trig
    Adjust power accordingly
    Launch ball by letting go of right click
"""

while not crashed:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            line.x1y1 = event.pos
            line.x2y2 = event.pos
            print(event.pos)
            line.draw()
            pressFlag = True
            pygame.display.update()

        if event.type == pygame.MOUSEMOTION:
            if pressFlag:
                line.x2y2 = event.pos
                line.draw()
                pygame.display.update()

        if event.type == pygame.MOUSEBUTTONUP:
            pressFlag = False

            circleList.append(Circle(gameDisplay, center=event.pos, radius=20, xVel=-(line.x2y2[0]-line.x1y1[0])//20,
                                     yVel=-(line.x2y2[1]-line.x1y1[1])//16))

            line.x1y1 = -100, -100
            line.x2y2 = -100, -100
            pygame.display.update()

        print(event)

    clock.tick(30)
    gameDisplay.fill((255, 255, 255))

    for i, c in enumerate(list(circleList)):
        print(c.center, c.vel, c.acc)
        c.drawCircle()
        c.updateX()
        c.updateY()

        if len(circleList) > 1:
            for j, c2 in enumerate(list(circleList)):
                if c == c2:
                    continue

                if fn.dist(c.center, c2.center) < (c.radius + c2.radius + 1):

                    cvelx = c2.vel[0]
                    cvely = c2.vel[1]
                    c2velx = c.vel[0]
                    c2vely = c.vel[1]

                    c.vel[0] = cvelx
                    c.vel[1] = cvely
                    c2.vel[0] = c2velx
                    c2.vel[1] = c2vely

                    # crashed = True

        if c.center[0] <= (0+c.radius):
            c.center[0] = 0+c.radius
            c.vel[0] = -c.vel[0] * energyLoss

        if c.center[0] >= (window[0] - c.radius):
            c.center[0] = window[0] - c.radius
            c.vel[0] = -c.vel[0] * energyLoss

        if c.center[1] <= (0 + c.radius):
            c.center[1] = 0 + c.radius
            c.vel[1] = -c.vel[1] * energyLoss

        if c.center[1] >= (window[1] - c.radius):
            c.center[1] = window[1] - c.radius
            c.vel[1] = -c.vel[1] * energyLoss

        if c.center[0] < 0 or c.center[0] > 1250 or c.center[1] < -50 or c.center[1] > 950:
            circleList.remove(c)
            del c

    line.draw()
    pygame.display.update()

pygame.quit()
quit()
