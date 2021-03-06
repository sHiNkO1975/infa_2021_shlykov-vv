import pygame
from pygame.draw import *
from random import randint
from numpy import pi



WHITE = (255, 255, 255)
YELLOW = (255, 255, 51)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIGHT_BLUE = (204, 255, 255)
BLUE = (0, 0, 255)
ORANGE = (255, 153, 51)
BROWN = (204, 102, 0)
LIGHT_BROWN = (255, 204, 153)

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))
screen.fill(LIGHT_BLUE)

#background
pygame.draw.line(screen, YELLOW, (0, 480), (600, 480), 240)
pygame.draw.line(screen, BLUE, (0, 338), (600, 338), 113)

# clouds and sun
for i in range(15):
    cloud_x = randint(98, 200)
    cloud_y = randint(53, 151)
    pygame.draw.circle(screen, WHITE, (cloud_x, cloud_y), 25)
    pygame.draw.circle(screen, BLACK, (cloud_x, cloud_y), 25, 1)
pygame.draw.circle(screen, YELLOW, (525, 75), 45)

# umbrella
pygame.draw.line(screen, ORANGE, (113, 525), (113, 323), 8)
pygame.draw.polygon(screen, RED, ((109, 323), (26, 375), (199, 375), (116, 323)))
umbrella_lines = [x for x in range(0, 68, 20)]
for j in umbrella_lines:
    pygame.draw.line(screen, BLACK, (109, 323), (109 - j, 375), 1)
    pygame.draw.line(screen, BLACK, (116, 323), (116 + j, 375), 1)

#ship
pygame.draw.line(screen, BROWN, (399, 425), (650, 425), 60)
pygame.draw.polygon(screen, BROWN, [(650, 455), (650, 396), (750, 396)])
for f in range(0, 61, 3):
    pygame.draw.arc(screen, BROWN, (340 + f, 336 + f, 120 - 2 * f, 120 - 2 * f), pi, 3 / 2 * pi, 3)
pygame.draw.line(screen, BLACK, (450, 395), (450, 225), 10)
pygame.draw.polygon(screen, LIGHT_BROWN, [(455, 225), (555, 310), (455, 395), (490, 310)])
pygame.draw.polygon(screen, BLACK, [(455, 225), (555, 310), (455, 395), (490, 310)], 1)
pygame.draw.line(screen, BLACK, (490, 310), (555, 310), 1)
pygame.draw.circle(screen, WHITE, (650, 425), 25)
pygame.draw.circle(screen, BLACK, (650, 425), 25, 5)








pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()