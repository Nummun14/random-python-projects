import pygame

pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill("black")
image = pygame.image.load("dvdimage.png")
x = 50
y = 50
x_speed = 2
y_speed = 2
screen.blit(image, [x, y])
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(20)
    pygame.draw.rect(screen, "black", [x, y, 100, 100], 0)
    x += x_speed
    y += y_speed
    if x > screen.get_width() - 100 or x < 0:
        x_speed *= -1
    if y > screen.get_height() - 100 or y < 0:
        y_speed *= -1

    screen.blit(image, [x, y])
    pygame.display.flip()

pygame.quit()
