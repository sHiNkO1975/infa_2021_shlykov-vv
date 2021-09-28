import pygame
from pygame.draw import *

WHITE = (255, 255, 255)
YELLOW = (255, 255, 51)
BLACK = (0, 0, 0)
RED = (255, 0, 0)



pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))
screen.fill(WHITE)

pygame.draw.circle(screen, YELLOW, (300, 300), 100) #face
pygame.draw.circle(screen, BLACK, (300, 300), 100, 1) #face
pygame.draw.circle(screen, RED, (330, 274), 18)
pygame.draw.circle(screen, BLACK, (330, 274), 18, 1)        #right eye
pygame.draw.circle(screen, BLACK, (330, 274), 7)   #right eye center
pygame.draw.circle(screen, RED, (270, 274), 12)
pygame.draw.circle(screen, BLACK, (270, 274), 12, 1)  #left eye
pygame.draw.circle(screen, BLACK, (270, 274), 7)   #left eye center
pygame.draw.line(screen, BLACK, (236, 343), (364, 343), 15) #smile
pygame.draw.polygon(screen, BLACK, ((309, 270), (360, 236), (357, 231), (305, 265))) #right brow
pygame.draw.polygon(screen, BLACK, ((283, 271), (240, 237), (245, 231), (288, 266))) #left brow




pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()