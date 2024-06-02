import pygame

pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill("white")
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(screen, "red", [250, 150, 300, 200], 3)
    pygame.display.flip()
pygame.quit()
