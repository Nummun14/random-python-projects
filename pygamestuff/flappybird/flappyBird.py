import pygame
import random


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([600, 451])
background = pygame.image.load("flappyBirdBackground.png")
bird_image = pygame.image.load("flappyBirdBird.png")
pillar_image = pygame.image.load("flappyBirdPillar.png")
screen.blit(background, [0, 0])
screen.blit(bird_image, [50, 225])
screen.blit(pillar_image, [400, 0])
pygame.display.flip()

pillar_speed = 2
pillar_spawn_point = [screen.get_width(), 0]
pillars = [[400, 0]]
last_pillar_time = 0
running = True


def spawn_pillar():
    screen.blit(pillar_image, pillar_spawn_point)
    pillars.append(pillar_spawn_point)


while running:
    screen.blit(background, [0, 0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.time.get_ticks() - last_pillar_time > 200:
        last_pillar_time = pygame.time.get_ticks()
        spawn_pillar()

    for pillar in pillars:
        pillar[0] -= pillar_speed
        if pillar[0] < 0:
            pillars.remove(pillar)
            continue
        screen.blit(pillar_image, pillar)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
