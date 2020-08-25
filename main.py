import pygame
from circle import Circle

pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Gravity")
gameDisplay.fill((255, 255, 255))

clock = pygame.time.Clock()

clickCircle = Circle(surface=gameDisplay, radius=25, center=(50, 50))

crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.MOUSEBUTTONUP:
            del clickCircle
            clickCircle = Circle(surface=gameDisplay, radius=25, center=(50, 50))
            clickCircle.center = event.pos
            clickCircle.drawCircle()
            pygame.display.update()

        print(event)

    gameDisplay.fill((255, 255, 255))
    clickCircle.drawCircle()
    clickCircle.updateSpeed()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
