import pygame
import random

pygame.init()
screen = pygame.display.set_mode([600, 451])
background = pygame.image.load("flappyBirdBackground.png")
bird_image = pygame.image.load("flappyBirdBird.png")
pillar_image = pygame.image.load("flappyBirdPillar.png")
screen.blit(background, [0, 0])
screen.blit(bird_image, [50, 225])
screen.blit(pillar_image, [400, 0])

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
