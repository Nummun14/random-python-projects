import pygame

pygame.init()
screen = pygame.display.set_mode([300, 600])
screen.fill((0, 0, 0))
pygame.draw.circle(screen, (255, 0, 0), (100, 100), 30, 0)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
