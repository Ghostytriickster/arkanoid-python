import pygame
from pygame.locals import *

WHITE = (255,255,255)
LACK = (0,0,0)
SIZE = (600, 400)
color = pygame.Color('lightskyblue3')
screen = pygame.display.set_mode(SIZE)
screen.fill(WHITE)
lock = True

input_rect = pygame.Rect(200, 200, 140, 32)

while lock :
    for event in pygame.event.get() :
        if event.type == QUIT :
            lock = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                
                pygame.draw.rect(screen, LACK, input_rect)
                
            else:
                active = False
    pygame.display.update()


# draw rectangle and argument passed which should
    # be on screen
    pygame.draw.rect(screen, LACK, input_rect)
  












pygame.quit()