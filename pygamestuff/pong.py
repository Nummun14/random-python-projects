import pygame

pygame.init()
screen = pygame.display.set_mode([600, 400])
screen.fill("black")

running = True
player1_x = 290
player1_y = 350
player2_x = 290
player2_y = 70
player_width = 50
player_height = 20
ball_radius = 10
ball_x = 300
ball_y = 200
player_speed = 10
ball_speed = 10

pygame.draw.rect(screen, "white", [player1_x, player1_y, player_width, player_height])
pygame.draw.rect(screen, "white", [player2_x, player2_y, player_width, player_height])
pygame.draw.circle(screen, "white", [ball_x, ball_y], ball_radius)
pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            pygame.draw.rect(screen, "black", [player1_x, player1_y, player_width, player_height])
            pygame.draw.rect(screen, "black", [player2_x, player2_y, player_width, player_height])
            if event.key == pygame.K_RIGHT:
                player1_x += player_speed
                if player1_x > screen.get_width() - player_width:
                    player1_x = 0
            if event.key == pygame.K_LEFT:
                player1_x -= player_speed
                if player1_x < 0:
                    player1_x = screen.get_width() - player_width

            if event.key == pygame.K_d:
                player2_x += player_speed
                if player2_x > screen.get_width() - player_width:
                    player2_x = 0
            if event.key == pygame.K_a:
                player2_x -= player_speed
                if player2_x < 0:
                    player2_x = screen.get_width() - player_width

    pygame.draw.rect(screen, "white", [player1_x, player1_y, player_width, player_height])
    pygame.draw.rect(screen, "white", [player2_x, player2_y, player_width, player_height])
    pygame.draw.circle(screen, "white", [ball_x, ball_y], ball_radius)
    pygame.display.flip()

pygame.quit()
