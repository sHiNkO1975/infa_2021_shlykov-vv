import pygame
import pygame.gfxdraw
import pygame.draw
from random import randint


WHITE = (255, 255, 255)
YELLOW = (255, 255, 51)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIGHT_BLUE = (204, 255, 255)
BLUE = (0, 0, 255)
ORANGE = (255, 153, 51)
BROWN = (204, 102, 0)
LIGHT_BROWN = (255, 204, 153)
FPS = 30
scale_x = 600
scale_y = 600
normalize_x = scale_x / 800
normalize_y = scale_y / 800


def draw_ship(xx):
    
    '''Рисует корабль
    xx - int - позиция корабля'''
    
    pygame.draw.line(screen,
                     BROWN,
                     (round((399 + xx) * normalize_x), round(425 * normalize_y)),
                     (round((650 + xx) * normalize_x), round(425 * normalize_y)),
                     round(60 * normalize_y))
    
    pygame.draw.polygon(screen, BROWN,
                        [(round((650 + xx) * normalize_x), round(455 * normalize_y)),
                         (round((650 + xx) * normalize_x), round(396 * normalize_y)),
                         (round((750 + xx) * normalize_x), round(396 * normalize_y))])
    
    pygame.draw.line(screen,
                     BLACK,
                     (round((450 + xx) * normalize_x), round(395 * normalize_y)),                     
                     (round((450 + xx) * normalize_x), round(225 * normalize_y)),
                     round(10 * normalize_x))
    
    pygame.draw.polygon(screen,
                        LIGHT_BROWN,
                        [(round((455 + xx) * normalize_x), round(225 * normalize_y)),
                         (round((555 + xx) * normalize_x), round(310 * normalize_y)),
                         (round((455 + xx) * normalize_x), round(395 * normalize_y)),
                         (round((490 + xx) * normalize_x), round(310 * normalize_y))])
    
    pygame.draw.polygon(screen,
                        BLACK,
                        [(round((455 + xx) * normalize_x), round(225 * normalize_y)),
                         (round((555 + xx) * normalize_x), round(310 * normalize_y)),
                         (round((455 + xx) * normalize_x), round(395 * normalize_y)),
                         (round((490 + xx) * normalize_x), round(310 * normalize_y))],
                        1)
    
    pygame.draw.line(screen,
                     BLACK,
                     (round((490 + xx) * normalize_x), round(310 * normalize_y)),
                     (round((555 + xx) * normalize_x), round(310 * normalize_y)),
                     1)
    
    pygame.draw.circle(screen,
                       WHITE,
                       (round((650 + xx) * normalize_x), round(425 * normalize_y)),
                       round(25 * normalize_x))
    
    pygame.draw.circle(screen,
                       BLACK,
                       (round((650 + xx) * normalize_x), round(425 * normalize_y)),
                       round(25 * normalize_x),
                       5)
    
    pygame.draw.circle(screen,
                       BROWN,
                       (round((399 + xx) * normalize_x), round(395.5 * normalize_y)),
                       round(60 * normalize_x),
                       850,
                       draw_bottom_left=True)


def draw_umbrella():
    '''
    Рисует зонтик
    '''
    
    pygame.draw.line(screen,
                     ORANGE,
                     (round(150 * normalize_x), round(700 * normalize_y)),
                     (round(150 * normalize_x), round(430 * normalize_y)),
                     round(10 * normalize_x))
    
    pygame.draw.polygon(screen,
                        RED,
                        ((round(145 * normalize_x), round(430 * normalize_y)),
                         (round(35 * normalize_x), round(500 * normalize_y)),
                         (round(265 * normalize_x), round(500 * normalize_y)),
                         (round(155 * normalize_x), round(430 * normalize_y))))
    
    umbrella_lines = [x for x in range(0, round(90 * normalize_x), round(27 * normalize_x))]
    
    for j in umbrella_lines:
        pygame.draw.line(screen,
                         BLACK,
                         (round(145 * normalize_x), round(430 * normalize_y)),
                         (round(145 * normalize_x) - j, round(500 * normalize_y)),
                         1)
        
        pygame.draw.line(screen,
                         BLACK,
                         (round(155 * normalize_x), round(430 * normalize_y)),
                         (round(155 * normalize_x) + j, round(500 * normalize_y)),
                         1)
        
        
def draw_background():
    
    '''
    Рисует задний фон с солнцем и облаком
    '''
    
    pygame.draw.line(screen,
                     YELLOW,
                     (0, round(650 * normalize_y)),
                     (round(800 * normalize_x), round(650 * normalize_y)),
                     300)
    
    pygame.draw.line(screen,
                     BLUE,
                     (0, round(450 * normalize_y)),
                     (round(800 * normalize_x), round(450 * normalize_y)),
                     150)
    
    for i in range(15):
        cloud_x = randint(round(130 * normalize_x), round(261 * normalize_y))
        cloud_y = randint(round(70 * normalize_x), round(201 * normalize_y))
        
        pygame.draw.circle(screen,
                           WHITE,
                           (cloud_x, cloud_y),
                           round(25 * normalize_x))
        
        pygame.draw.circle(screen,
                           BLACK,
                           (cloud_x, cloud_y),
                           round(25 * normalize_x),
                           1)

        pygame.draw.circle(screen,
                           YELLOW,
                           (round(700 * normalize_x), round(100 * normalize_y)),
                           round(60 * normalize_x))
        

pygame.init()
screen = pygame.display.set_mode((scale_x, scale_y))
screen.fill(LIGHT_BLUE)
draw_background()
draw_ship(-100)
draw_umbrella()
pygame.display.update()

clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()