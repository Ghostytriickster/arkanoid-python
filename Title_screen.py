import pygame
from pygame.locals import *

# en attente de finition 
# bouton fonctionel

WHITE = (255,255,255)
GREEN = (0,255,0)
LACK = (0,0,0)
SIZE = (600, 400)
color = pygame.Color('lightskyblue3')
screen = pygame.display.set_mode(SIZE)
screen.fill(WHITE)
lock = True

input_rect = pygame.Rect(200, 200, 140, 32)
pygame.draw.rect(screen,GREEN,input_rect)

while lock :
    for event in pygame.event.get() :
        if event.type == QUIT :
            lock = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if input_rect.collidepoint(mouse_pos):
                pass
                pygame.draw.rect(screen, LACK, input_rect)
                
            else:
                active = False
    pygame.display.update()
  
pygame.quit()












pygame.quit()
