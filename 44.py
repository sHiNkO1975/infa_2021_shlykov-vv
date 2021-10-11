import pygame
import pygame.gfxdraw
from pygame.draw import *
from random import randint
from math import pi

def ship(xx):
    pygame.draw.line(screen, BROWN, (round((399 + xx) * s_x), round(425 * s_y)),
                     (round((650 + xx) * s_x), round(425 * s_y)), round(60 * s_y))
    pygame.draw.polygon(screen, BROWN,
                        [(round((650 + xx) * s_x), round(455 * s_y)), (round((650 + xx) * s_x), round(396 * s_y)),
                         (round((750 + xx) * s_x), round(396 * s_y))])
    pygame.draw.line(screen, BLACK, (round((450 + xx) * s_x), round(395 * s_y)),
                     (round((450 + xx) * s_x), round(225 * s_y)), round(10 * s_x))
    pygame.draw.polygon(screen, LIGHT_BROWN,
                        [(round((455 + xx) * s_x), round(225 * s_y)), (round((555 + xx) * s_x), round(310 * s_y)),
                         (round((455 + xx) * s_x), round(395 * s_y)), (round((490 + xx) * s_x), round(310 * s_y))])
    pygame.draw.polygon(screen, BLACK,
                        [(round((455 + xx) * s_x), round(225 * s_y)), (round((555 + xx) * s_x), round(310 * s_y)),
                         (round((455 + xx) * s_x), round(395 * s_y)), (round((490 + xx) * s_x), round(310 * s_y))], 1)
    pygame.draw.line(screen, BLACK, (round((490 + xx) * s_x), round(310 * s_y)),
                     (round((555 + xx) * s_x), round(310 * s_y)), 1)
    pygame.draw.circle(screen, WHITE, (round((650 + xx) * s_x), round(425 * s_y)), round(25 * s_x))  # xxx
    pygame.draw.circle(screen, BLACK, (round((650 + xx) * s_x), round(425 * s_y)), round(25 * s_x), 5)  # xxx
    pygame.draw.circle(screen, BROWN, (round((399 + xx) * s_x), round(395.5 * s_y)), round(60 * s_x), 850,
                       draw_bottom_left=True)  # xxx

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
scale_x = 600
scale_y = 600
screen = pygame.display.set_mode((scale_x, scale_y))
screen.fill(LIGHT_BLUE)
s_x = scale_x / 800
s_y = scale_y / 800

#background
pygame.draw.line(screen, YELLOW, (0, round(650 * s_y)), (round(800 * s_x), round(650 * s_y)), 300)
pygame.draw.line(screen, BLUE, (0, round(450 * s_y)), (round(800 * s_x), round(450 * s_y)), 150)

# clouds and sun
for i in range(15):
    cloud_x = randint(round(130 * s_x), round(261 * s_y))
    cloud_y = randint(round(70 * s_x), round(201 * s_y))
    pygame.draw.circle(screen, WHITE, (cloud_x, cloud_y), round(25 * s_x)) #xxx
    pygame.draw.circle(screen, BLACK, (cloud_x, cloud_y), round(25 * s_x), 1) #xxx
pygame.draw.circle(screen, YELLOW, (round(700 * s_x), round(100 * s_y)), round(60 * s_x)) #xxx

# umbrella
pygame.draw.line(screen, ORANGE, (round(150 * s_x), round(700 * s_y)), (round(150 * s_x), round(430 * s_y)), round(10 * s_x))
pygame.draw.polygon(screen, RED, ((round(145 * s_x), round(430 * s_y)), (round(35 * s_x), round(500 * s_y)), (round(265 * s_x), round(500 * s_y)), (round(155 * s_x), round(430 * s_y))))
umbrella_lines = [x for x in range(0, round(90 * s_x), round(27 * s_x))] #xxx
for j in umbrella_lines:
    pygame.draw.line(screen, BLACK, (round(145 * s_x), round(430 * s_y)), (round(145 * s_x) - j, round(500 * s_y)), 1)
    pygame.draw.line(screen, BLACK, (round(155 * s_x), round(430 * s_y)), (round(155 * s_x) + j, round(500 * s_y)), 1)

#ship
ship(-100)








pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
