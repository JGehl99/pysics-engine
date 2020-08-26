import pygame
import funclib as fn
from circle import Circle
from line import Line

# size of window
window = [1000, 750]

# percentage of velocity kept after colliding with something
energyLoss = 0.90

# create window and fill it with white
pygame.init()
gameDisplay = pygame.display.set_mode((window[0], window[1]))
pygame.display.set_caption("Gravity")
gameDisplay.fill((255, 255, 255))

# game clock
clock = pygame.time.Clock()

# holds all circles
circleList = []

# True if mouse is pressed
pressFlag = False

# default valies for line
line = Line(gameDisplay, (0, 0, 0), (0, 0), (0, 0), 2)

# boolean to exit game loop
crashed = False

# game loop
while not crashed:

    # loop over events
    for event in pygame.event.get():

        # close window
        if event.type == pygame.QUIT:
            crashed = True

        # click left or right
        if event.type == pygame.MOUSEBUTTONDOWN:
            # get position of first click, set both line points to it
            line.x1y1 = event.pos
            line.x2y2 = event.pos
            # draw and update
            line.draw()
            pygame.display.update()
            # mouse is now pressed
            pressFlag = True

        # mouse movement
        if event.type == pygame.MOUSEMOTION:
            if pressFlag:
                # set second line point, draw and update
                line.x2y2 = event.pos
                line.draw()
                pygame.display.update()

        # release left or right
        if event.type == pygame.MOUSEBUTTONUP:
            pressFlag = False

            # create a circle at the release point of the mouse, x and y velocity based on length of line
            # velocities are divided by a static value since its too fast without it
            circleList.append(Circle(gameDisplay, center=event.pos, radius=20, xVel=-(line.x2y2[0]-line.x1y1[0])//20,
                                     yVel=-(line.x2y2[1]-line.x1y1[1])//16))

            # move line off screen since its reused, update
            line.x1y1 = -100, -100
            line.x2y2 = -100, -100
            pygame.display.update()

    # adds delay to make this run at 60fps
    clock.tick(60)

    # fill screen with white
    gameDisplay.fill((255, 255, 255))

    # for each circle in circleList
    for i, c in enumerate(list(circleList)):

        # draw the circle and apply the current frame's x and y velocity
        c.drawCircle()
        c.updateX()
        c.updateY()

        # if theres more than 1 circle on the screen, loop over circles again to check collision
        if len(circleList) > 1:
            for j, c2 in enumerate(list(circleList)):

                # if its the same circle, skip
                if c == c2:
                    continue

                # if the distance between the circle's centers is less than combined radii + 1, then they're colliding
                if fn.dist(c.center, c2.center) < (c.radius + c2.radius + 1):

                    # since mass is not considered (yet), swap around the horiz and vert velocity components
                    cvelx = c2.vel[0]
                    cvely = c2.vel[1]
                    c2velx = c.vel[0]
                    c2vely = c.vel[1]

                    # assign the new components
                    c.vel[0] = cvelx
                    c.vel[1] = cvely
                    c2.vel[0] = c2velx
                    c2.vel[1] = c2vely

                    # crashed = True

        # if ball hits a wall, rebound off wall at %5 less velocity in the opposite direction
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

        # if circle ends up off screen, remove from list and delete object
        if c.center[0] < 0 or c.center[0] > 1250 or c.center[1] < -50 or c.center[1] > 950:
            circleList.remove(c)
            del c

    # draw line and update
    line.draw()
    pygame.display.update()

# quits game and program
pygame.quit()
quit()
