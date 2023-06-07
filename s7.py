# import pygame
# import random
# number = random.randint(1,20)
# print(number)

# i = 0
# while i < 10:
#     print(i)
#     i += 1


import pygame
from pygame.locals import QUIT
pygame.init()

display_surface = pygame.display.set_mode((400, 300))

pygame.display.set_caption('Hello world')

RED = (255, 0, 0)
GREEN = (0, 255, 0)  # (0, 255,0,255)
BLUE = (0, 0, 255)
CUSTOM = (255, 15, 10, 0)
BLACK = (0, 0, 0, 100)

display_surface.fill(BLACK)
pygame.draw.rect(display_surface, CUSTOM, (10, 20, 200, 300))
pygame.draw.polygon(display_surface, GREEN, ((146, 0),
                    (291, 106), (236, 277), (56, 277), (0, 106)))
pygame.draw.line(display_surface, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(display_surface, BLUE, (120, 60), (60, 120), 4)
pygame.draw.line(display_surface, BLUE, (60, 120), (120, 120), 4)
pygame.draw.circle(display_surface, RED, (300, 250), 20, 0)
pygame.draw.circle(display_surface, RED, (300, 250), 50, 2)
pygame.draw.ellipse(display_surface, RED, (100, 100, 100, 200), 2)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
