# https://www.iconarchive.com/

import pygame

pygame.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Feed the dragon")

FPS = 60
clock = pygame.time.Clock()
PLAYER_STARTING_LIVES = 5
PLAYER_VELOCITY = 10
COIN_STARTING_VELOCITY = 10


score = 0

player_lives = PLAYER_STARTING_LIVES
coin_velocity = COIN_STARTING_VELOCITY

GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.Font("AttackGraffiti.ttf", 32)

score_text = font.render("Score: "+ str(score), True, GREEN, DARKGREEN)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

title_text = font.render("Feed The dragon", True, GREEN, WHITE)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH//2
title_rect.y = 10

lives_text = font.render("Lives: "+ str(player_lives), True, GREEN, DARKGREEN)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 10, 10)



player_image = pygame.image.load("dragon_right.png")
player_rect = player_image.get_rect()
# player_rect.left = 64
# player_rect.centery = WINDOW_HEIGHT//2
player_rect.x = 100
player_rect.y = 100

# TODO اضافه کردن سکه
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and player_rect.top > 64:
                player_rect.y -= PLAYER_VELOCITY
        # TODO اضافه کردن جهت پائین

    # keys = pygame.key.get_pressed()  
    # if keys[pygame.K_UP] and player_rect.top > 64:
    #     player_rect.y -= PLAYER_VELOCITY

    # TODO همین روش برای جهت پائین

    display_surface.fill(BLACK)
        

    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text,title_rect)
    display_surface.blit(lives_text, lives_rect)
    pygame.draw.line(display_surface, WHITE, (0,64), (WINDOW_WIDTH,64), 2)



    display_surface.blit(player_image, player_rect)
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
