import pygame
import random

pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill("white")
pygame.display.flip()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in range(100):
        x = random.randint(0, 500)
        y = random.randint(0, 400)
        width = random.randint(0, 250)
        height = random.randint(0, 100)

        pygame.draw.rect(screen, "white", [x, y, width, height], 2)
    pygame.display.flip()

pygame.quit()
