import pygame
import random

pygame.init()
pygame.display.set_caption("pong")
screen = pygame.display.set_mode([600, 400])
screen.fill("black")
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

running = True
has_winner = False
player1_x = 290
player1_y = 350
player2_x = 290
player2_y = 70
player_width = 50
player_height = 20
ball_radius = 10
ball_x = 300
ball_y = 200
player_speed = 5
ball_y_speed = 2 * random.randint(-1, 1)
ball_x_speed = 2 * random.randint(-1, 1)

pygame.draw.rect(screen, "white", [player1_x, player1_y, player_width, player_height])
pygame.draw.rect(screen, "white", [player2_x, player2_y, player_width, player_height])
pygame.draw.circle(screen, "white", [ball_x, ball_y], ball_radius)
pygame.display.flip()

if ball_x_speed == 0:
    ball_x_speed += 2
if ball_y_speed == 0:
    ball_y_speed += 2

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    pygame.draw.rect(screen, "black", [player1_x, player1_y, player_width, player_height])
    pygame.draw.rect(screen, "black", [player2_x, player2_y, player_width, player_height])
    pygame.draw.circle(screen, "black", [ball_x, ball_y], ball_radius)
    if keys[pygame.K_RIGHT]:
        player1_x += player_speed
        if player1_x > screen.get_width() - player_width:
            player1_x = 0
    if keys[pygame.K_LEFT]:
        player1_x -= player_speed
        if player1_x < 0:
            player1_x = screen.get_width() - player_width

    if keys[pygame.K_d]:
        if player2_x > screen.get_width() - player_width:
            player2_x = 0
    if keys[pygame.K_a]:
        player2_x -= player_speed
        if player2_x < 0:
            player2_x = screen.get_width() - player_width

    ball_y += ball_y_speed
    ball_x += ball_x_speed
    if player1_x <= ball_x <= player1_x + player_width and player1_y <= ball_y + ball_radius <= player1_y + player_height:
        ball_y_speed *= -1
        ball_y = player1_y - ball_radius
    if player2_x <= ball_x <= player2_x + player_width and player2_y <= ball_y - ball_radius <= player2_y + player_height:
        ball_y_speed *= -1
        ball_y = player2_y + player_height + ball_radius
    if ball_x < ball_radius or ball_x > screen.get_width() - ball_radius:
        ball_x_speed *= -1

    if ball_y > screen.get_height():
        text = font.render("top player won!", True, "red", "black")
        has_winner = True
    if ball_y < 0:
        text = font.render("bottom player won!", True, "red", "black")
        has_winner = True

    pygame.draw.rect(screen, "white", [player1_x, player1_y, player_width, player_height])
    pygame.draw.rect(screen, "white", [player2_x, player2_y, player_width, player_height])
    pygame.draw.circle(screen, "white", [ball_x, ball_y], ball_radius)
    pygame.display.flip()

    if has_winner:
        text_rect = text.get_rect()
        text_rect.center = (screen.get_width() // 2, screen.get_height() // 2)
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.delay(5000)
        running = False

    clock.tick(60)

pygame.quit()
