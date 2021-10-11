import pygame
from pygame.draw import *

pygame.init()

FPS = 30
pi = 3.14
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
BROWN = (101, 67, 33)
HEAD3 = (238, 238, 238)
HEAD1 = (225, 223, 196)

screen = pygame.display.set_mode((600, 1000))

rect(screen, WHITE, (0, 0, 600, 600))


def create_surface():
    surface0 = pygame.Surface((300, 300))
    surface0.fill((255, 255, 255))
    surface0.set_colorkey((255, 255, 255))
    return surface0


def under(high, weight, colour):
    surf = create_surface()
    pygame.draw.rect(surf, colour, (0, 0, weight, high))
    new_image = pygame.transform.scale(surf, (150, 100))
    screen.blit(new_image, (470, 650))


def body(high, weight, colour):
    surf = create_surface()
    pygame.draw.ellipse(surf, colour, (50, 10, weight, high))
    rect(surf, BLACK, (70, 35, weight/2+10, high/2+15))
    new_image = pygame.transform.scale(surf, (300, 300))
    screen.blit(new_image, (400, 500))


def lefthand(high, weight, colour):
    surf = create_surface()
    pygame.draw.ellipse(surf, colour, (0, 0, weight, high))
    new_image = pygame.transform.scale(surf, (400, 50))
    screen.blit(new_image, (395, 540))


def righthand(high, weight, colour):
    surf = create_surface()
    pygame.draw.ellipse(surf, colour, (0, 0, weight, high))
    new_image = pygame.transform.scale(surf, (400, 50))
    new_image_2 = pygame.transform.rotate(new_image, 120)
    screen.blit(new_image_2, (360, 230))


def arca(radius, colour):
    surf = create_surface()
    circle(surf, colour, (150, 150), radius)
    circle(surf, BLACK, (150, 150), radius, 3)
    x1 = 150 - radius
    y1 = 150 + 1
    N = 3
    h = radius//(N+1)
    y = y1 - h
    x = x1 + h
    line(surf, BLACK, (x1, 149), (x1+2*radius, 149))
    for i in range(N):
        line(surf, BLACK, (x-25, y), (2*radius - x + 40, y))
        y-=h
        x+=h
    rect(surf, GRAY, (0, 150, 300, 150))
    new_image = pygame.transform.scale(surf, (300, 300))
    screen.blit(new_image, (20, 400))


def head3(radius, colour):
    surf = create_surface()
    circle(surf, colour, (100, 100), radius)
    new_image = pygame.transform.scale(surf, (120, 120))
    screen.blit(new_image, (460, 450))


def head2(radius, colour):
    surf = create_surface()
    circle(surf, colour, (100, 100), radius)
    new_image = pygame.transform.scale(surf, (120, 120))
    screen.blit(new_image, (460, 460))


def head1(radius, colour):
    surf = create_surface()
    circle(surf, colour, (100, 100), radius)
    new_image = pygame.transform.scale(surf, (120, 120))
    screen.blit(new_image, (460, 465))


def leftleg(colour):
    surf = create_surface()
    ellipse(surf, colour, (100, 0, 50, 100))
    ellipse(surf, colour, (20, 60, 100, 50))
    new_image = pygame.transform.scale(surf, (85, 85))
    screen.blit(new_image, (440, 650))


def rightleg(colour):
    surf = create_surface()
    ellipse(surf, colour, (0, 0, 50, 100))
    ellipse(surf, colour, (0, 60, 100, 50))
    new_image = pygame.transform.scale(surf, (85, 85))
    screen.blit(new_image, (510, 650))


def fish():
    surf = create_surface()
    polygon(surf, (102, 99, 112), ((160, 60), (171, 58), (196, 73), (168, 88)), width=0)
    arc(surf, (71, 136, 147), (65, 33, 148, 50), 0.4, 2.74, 30)
    arc(surf, (71, 136, 147), (65, 13, 148, 50), 3.44, 6, 30)
    polygon(surf, (71, 136, 147), ((67, 45), (14, 80), (4, 35)), width=0)
    polygon(surf, (102, 99, 112), ((135, 33), (94, 0), (164, 15), (172, 24), (171, 35)), width=0)
    polygon(surf, (102, 99, 112), ((97, 59), (80, 79), (112, 84), (114, 62)), width=0)
    circle(surf, (2, 57, 147), (170, 47), 7, width=0)
    circle(surf, (5, 64, 85), (170, 47), 5, width=0)
    screen.blit(surf, (50, 700))


def face():
    line(screen, BLACK, (485, 500), (495, 505))
    line(screen, BLACK, (505, 505), (515, 495))
    line(screen, BLACK, (490, 520), (510, 520))
    line(screen, BLACK, (445, 650), (398, 500))


def person():
    body(200, 100, BROWN)
    lefthand(150, 50, BROWN)
    righthand(150, 50, BROWN)
    rect(screen, GRAY, (0, 650, 600, 300))
    rect(screen, WHITE, (0, 700, 600, 300))
    head3(100, HEAD3)
    head2(70, GRAY)
    head1(50, HEAD1)
    leftleg(BROWN)
    rightleg(BROWN)
    face()


arca(130, GRAY)

rect(screen, WHITE, (0, 720, 600, 300))
rect(screen, GRAY, (0, 510, 600, 210))

person()
fish()



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()